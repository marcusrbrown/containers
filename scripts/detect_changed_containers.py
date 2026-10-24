#!/usr/bin/env python3
"""Select the image build contexts affected by a change.

An image context is any directory that contains a ``Dockerfile`` outside the
excluded top-level directories. A context is *affected* when any changed file
lies inside its directory (lockfile, ``package.json``, source, entrypoint, the
Dockerfile itself, ...), because the whole directory is the Docker build
context.

Both ``build-publish.yaml`` and ``test.yaml`` call this CLI, so the rule lives
in one place. It is stdlib-only on purpose: workflows run it with the runner's
system ``python3`` before any dependency install.

Output is ``key=value`` lines on stdout (``$GITHUB_OUTPUT`` format); progress
and diagnostics go to stderr. Any failure exits non-zero. A git error must
never degrade into "no changes".
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections.abc import Iterable, Sequence
from pathlib import Path

# Top-level directories that never hold active image contexts. Keep in sync with
# the negated patterns in the workflow ``paths`` filters.
EXCLUDED_TOP_LEVEL_DIRS = frozenset(
    {"archived", "templates", ".devcontainer", ".github"}
)

# Directories never worth descending into when discovering Dockerfiles.
_PRUNED_DIRS = frozenset({".git", "node_modules", ".venv"})

DOCKERFILE_NAME = "Dockerfile"

# Image names must be valid registry repository names.
IMAGE_NAME_RE = re.compile(r"^[a-z0-9][a-z0-9_.-]*$")
SHA_RE = re.compile(r"^[0-9a-fA-F]{7,64}$")
ZERO_SHA_RE = re.compile(r"^0+$")

FORMAT_BUILD_MATRIX = "build-matrix"
FORMAT_TEST_CONTAINERS = "test-containers"
EVENT_PULL_REQUEST = "pull_request"
EVENT_PUSH = "push"
EVENT_DISPATCH = "workflow_dispatch"


class DetectionError(RuntimeError):
    """Raised when change detection cannot produce a trustworthy answer."""


def _normalize(path: str) -> str:
    """Strip a leading ``./`` so ``./node/x`` and ``node/x`` compare equal."""
    while path.startswith("./"):
        path = path[2:]
    return path


def is_active_dockerfile(path: str) -> bool:
    """True for a ``Dockerfile`` that defines an active (non-excluded) context."""
    path = _normalize(path)
    parts = path.split("/")
    # A root-level Dockerfile has no context directory of its own: it would make
    # every change select it, and "." is not a valid image name.
    if len(parts) < 2 or parts[-1] != DOCKERFILE_NAME:
        return False
    return parts[0] not in EXCLUDED_TOP_LEVEL_DIRS


def discover_dockerfiles(root: Path) -> list[str]:
    """Return sorted active Dockerfile paths relative to ``root``."""
    found: list[str] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in _PRUNED_DIRS]
        if DOCKERFILE_NAME not in filenames:
            continue
        rel = Path(dirpath, DOCKERFILE_NAME).relative_to(root).as_posix()
        if is_active_dockerfile(rel):
            found.append(rel)
    return sorted(found)


def select_changed_dockerfiles(
    changed_files: Iterable[str], dockerfiles: Iterable[str]
) -> list[str]:
    """Return the active Dockerfiles whose context contains a changed file.

    Pure function. ``dockerfiles`` is filtered through the exclusion rules so a
    caller can pass raw paths; excluded ones are never selected.
    """
    changed = [_normalize(p) for p in changed_files if p]
    selected: list[str] = []
    for dockerfile in sorted({_normalize(d) for d in dockerfiles}):
        if not is_active_dockerfile(dockerfile):
            continue
        context = dockerfile.rsplit("/", 1)[0]
        prefix = context + "/"
        if any(path.startswith(prefix) for path in changed):
            selected.append(dockerfile)
    return selected


def build_matrix(dockerfiles: Iterable[str]) -> dict[str, list[dict[str, str]]]:
    """Build the ``build-publish.yaml`` matrix for the given Dockerfiles.

    Field values and image naming (``<parent>-<name>``) are what the workflow
    has always produced; downstream registry image names depend on them.
    """
    include: list[dict[str, str]] = []
    for dockerfile in dockerfiles:
        dockerfile = _normalize(dockerfile)
        context = dockerfile.rsplit("/", 1)[0]
        name = context.rsplit("/", 1)[-1]
        parent = os.path.basename(os.path.dirname(context)) or "."
        image = name if parent == "." else f"{parent}-{name}"
        if not IMAGE_NAME_RE.match(image):
            print(
                f"Skipping invalid image name: {image} (from {dockerfile})",
                file=sys.stderr,
            )
            continue
        include.append(
            {
                "dockerfile": dockerfile,
                "context": context,
                "image": image,
                "name": name,
                "category": parent,
            }
        )
    matrix = {"include": include}
    # Final guard: archived contexts must never reach the build matrix.
    if "archived" in json.dumps(matrix):
        raise DetectionError("Archived containers detected in build matrix")
    return matrix


def test_job_containers(dockerfiles: Iterable[str]) -> list[dict[str, str]]:
    """Build the ``test.yaml`` container list (``[{path, name}]``)."""
    contexts = sorted({_normalize(d).rsplit("/", 1)[0] for d in dockerfiles})
    return [{"path": ctx, "name": "-".join(ctx.split("/"))} for ctx in contexts]


def _compact(value: object) -> str:
    return json.dumps(value, separators=(",", ":"))


def render_outputs(fmt: str, dockerfiles: Sequence[str]) -> list[str]:
    """Render ``key=value`` lines for one workflow's expected outputs."""
    if fmt == FORMAT_BUILD_MATRIX:
        matrix = build_matrix(dockerfiles)
        return [
            f"has_changes={'true' if matrix['include'] else 'false'}",
            f"matrix={_compact(matrix)}",
        ]
    if fmt == FORMAT_TEST_CONTAINERS:
        containers = test_job_containers(dockerfiles)
        return [
            f"containers={_compact(containers)}",
            f"has-containers={'true' if containers else 'false'}",
        ]
    raise DetectionError(f"Unknown format: {fmt}")


def git_changed_files(base: str, head: str, event: str, cwd: Path) -> list[str]:
    """List files changed between ``base`` and ``head``; raise on any failure.

    Pull requests use ``base...head`` (merge-base diff, what the PR shows).
    Pushes use ``base..head``. Renames are reported as delete+add so both the
    old and new locations count as changed.
    """
    for label, sha in (("base", base), ("head", head)):
        if not SHA_RE.match(sha):
            raise DetectionError(f"Invalid {label} SHA: {sha!r}")
    separator = "..." if event == EVENT_PULL_REQUEST else ".."
    cmd = [
        "git",
        "diff",
        "--name-only",
        "--no-renames",
        "-z",
        f"{base}{separator}{head}",
        "--",
    ]
    try:
        result = subprocess.run(
            cmd, cwd=cwd, check=False, capture_output=True, text=True
        )
    except OSError as exc:
        raise DetectionError(f"Could not run git: {exc}") from exc
    if result.returncode != 0:
        raise DetectionError(
            f"{' '.join(cmd)} failed ({result.returncode}): {result.stderr.strip()}"
        )
    return [p for p in result.stdout.split("\0") if p]


def detect(event: str, base: str, head: str, root: Path) -> tuple[list[str], str]:
    """Return ``(selected_dockerfiles, reason)`` for a workflow event."""
    dockerfiles = discover_dockerfiles(root)
    if event == EVENT_DISPATCH:
        return dockerfiles, "workflow_dispatch: all active containers"
    if event == EVENT_PUSH and (not base or ZERO_SHA_RE.match(base)):
        return dockerfiles, "push without a usable 'before' SHA: all active containers"
    if event not in (EVENT_PUSH, EVENT_PULL_REQUEST):
        raise DetectionError(f"Unsupported event: {event!r}")
    if not base or not head:
        raise DetectionError(f"{event} requires both --base and --head")
    changed = git_changed_files(base, head, event, root)
    print(f"Changed files ({len(changed)}):", file=sys.stderr)
    for path in changed:
        print(f"  {path}", file=sys.stderr)
    return select_changed_dockerfiles(changed, dockerfiles), f"{event}: {base}..{head}"


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--format",
        required=True,
        choices=[FORMAT_BUILD_MATRIX, FORMAT_TEST_CONTAINERS],
    )
    parser.add_argument(
        "--event",
        required=True,
        help="GitHub event name (pull_request, push, workflow_dispatch)",
    )
    parser.add_argument("--base", default="", help="base SHA (PR base / push before)")
    parser.add_argument("--head", default="", help="head SHA (PR head / push after)")
    parser.add_argument("--root", default=".", help="repository root (default: .)")
    args = parser.parse_args(argv)

    try:
        dockerfiles, reason = detect(
            args.event, args.base.strip(), args.head.strip(), Path(args.root)
        )
        lines = render_outputs(args.format, dockerfiles)
    except DetectionError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(f"Detection mode: {reason}", file=sys.stderr)
    print(f"Containers selected: {dockerfiles or 'none'}", file=sys.stderr)
    for line in lines:
        print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())

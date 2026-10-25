"""Tests for scripts/detect_changed_containers.py and its workflow wiring."""

import json
import os
import re
import subprocess
from pathlib import Path

import pytest
import yaml

from scripts import detect_changed_containers as dcc

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOWS = REPO_ROOT / ".github" / "workflows"

ACTIVE = [
    "node/alpine/Dockerfile",
    "node/release/Dockerfile",
]

# Every Dockerfile that exists in the repo today, active or not.
ALL_DOCKERFILES = ACTIVE + [
    "archived/parity/branch/Dockerfile",
    "archived/parity/release/Dockerfile",
    "templates/base/alpine/Dockerfile",
    "templates/apps/nodejs/express/Dockerfile",
    ".devcontainer/Dockerfile",
]

ZERO_SHA = "0" * 40


# ---------------------------------------------------------------------------
# Pure selection
# ---------------------------------------------------------------------------


@pytest.mark.parametrize(
    "changed, expected",
    [
        pytest.param(
            ["node/alpine/package-lock.json", "node/release/package-lock.json"],
            ["node/alpine/Dockerfile", "node/release/Dockerfile"],
            id="lockfile-only-both-contexts-824",
        ),
        pytest.param(
            ["node/alpine/package-lock.json"],
            ["node/alpine/Dockerfile"],
            id="lockfile-only-one-context",
        ),
        pytest.param(
            ["node/release/package.json"],
            ["node/release/Dockerfile"],
            id="package-json-only",
        ),
        pytest.param(
            ["node/alpine/index.js"], ["node/alpine/Dockerfile"], id="source-only"
        ),
        pytest.param(
            ["node/release/docker-entrypoint.sh"],
            ["node/release/Dockerfile"],
            id="entrypoint-only",
        ),
        pytest.param(
            ["node/alpine/Dockerfile"], ["node/alpine/Dockerfile"], id="dockerfile-only"
        ),
        pytest.param(
            [
                "node/alpine/index.js",
                "node/alpine/package.json",
                "node/release/docker-entrypoint.sh",
                "README.md",
            ],
            ["node/alpine/Dockerfile", "node/release/Dockerfile"],
            id="multi-file-multi-context",
        ),
        pytest.param(
            ["node/alpine/src/deep/nested/file.js"],
            ["node/alpine/Dockerfile"],
            id="deeply-nested-file",
        ),
        pytest.param(["README.md"], [], id="readme-only"),
        pytest.param(
            ["docs/guide.md", "CHANGELOG.md", "pyproject.toml"], [], id="docs-only"
        ),
        pytest.param(
            [".github/workflows/test.yaml", "scripts/containers_cli.py"],
            [],
            id="workflow-and-scripts-only",
        ),
        pytest.param(
            ["templates/base/alpine/Dockerfile", "templates/base/alpine/x.sh"],
            [],
            id="templates-excluded",
        ),
        pytest.param(
            ["archived/parity/branch/Dockerfile", "archived/parity/release/x"],
            [],
            id="archived-excluded",
        ),
        pytest.param([".devcontainer/Dockerfile"], [], id="devcontainer-excluded"),
        pytest.param(
            ["node/foo/templates/Dockerfile", "x/archived/Dockerfile"],
            [],
            id="nested-excluded-segments",
        ),
        pytest.param(
            ["node/alpine-sibling/index.js"], [], id="sibling-prefix-is-not-contained"
        ),
        pytest.param(["node/index.js"], [], id="parent-dir-file-is-not-contained"),
        pytest.param(
            ["./node/alpine/index.js"], ["node/alpine/Dockerfile"], id="dot-slash"
        ),
        pytest.param([], [], id="nothing-changed"),
    ],
)
def test_select_changed_dockerfiles(changed, expected):
    assert dcc.select_changed_dockerfiles(changed, ALL_DOCKERFILES) == expected


def test_select_never_returns_excluded_dockerfiles_even_if_passed_in():
    selected = dcc.select_changed_dockerfiles(
        ["templates/base/alpine/Dockerfile", "archived/parity/branch/x"],
        ALL_DOCKERFILES,
    )
    assert selected == []


def test_select_ignores_root_level_dockerfile():
    assert dcc.select_changed_dockerfiles(["anything"], ["Dockerfile"]) == []


def test_is_active_dockerfile():
    assert dcc.is_active_dockerfile("node/alpine/Dockerfile")
    assert dcc.is_active_dockerfile("./node/alpine/Dockerfile")
    assert dcc.is_active_dockerfile("newdir/img/Dockerfile")
    assert not dcc.is_active_dockerfile("node/alpine/Dockerfile.dev")
    assert not dcc.is_active_dockerfile("node/alpine/index.js")
    assert not dcc.is_active_dockerfile("Dockerfile")
    for excluded in ("archived", "templates", ".devcontainer", ".github"):
        assert not dcc.is_active_dockerfile(f"{excluded}/x/Dockerfile")
        # Any path segment counts, not just the top-level directory.
        assert not dcc.is_active_dockerfile(f"node/foo/{excluded}/Dockerfile")
        assert not dcc.is_active_dockerfile(f"x/{excluded}/y/Dockerfile")
    # Segment equality, not substring: these names are legitimate contexts.
    assert dcc.is_active_dockerfile("node/archived-x/Dockerfile")
    assert dcc.is_active_dockerfile("node/my-templates/Dockerfile")
    assert dcc.is_active_dockerfile("node/foo-archived/Dockerfile")


# ---------------------------------------------------------------------------
# Output compatibility (golden values captured from the previous shell logic)
# ---------------------------------------------------------------------------

GOLDEN_MATRIX = (
    '{"include":['
    '{"dockerfile":"node/alpine/Dockerfile","context":"node/alpine",'
    '"image":"node-alpine","name":"alpine","category":"node"},'
    '{"dockerfile":"node/release/Dockerfile","context":"node/release",'
    '"image":"node-release","name":"release","category":"node"}'
    "]}"
)
GOLDEN_TEST_CONTAINERS = (
    '[{"path":"node/alpine","name":"node-alpine"},'
    '{"path":"node/release","name":"node-release"}]'
)


def test_build_matrix_matches_previous_output():
    lines = dcc.render_outputs(dcc.FORMAT_BUILD_MATRIX, ACTIVE)
    assert lines == ["has_changes=true", f"matrix={GOLDEN_MATRIX}"]


def test_build_matrix_field_order_is_stable():
    entry = dcc.build_matrix(["node/alpine/Dockerfile"])["include"][0]
    assert list(entry) == ["dockerfile", "context", "image", "name", "category"]


def test_build_matrix_empty():
    assert dcc.render_outputs(dcc.FORMAT_BUILD_MATRIX, []) == [
        "has_changes=false",
        'matrix={"include":[]}',
    ]


def test_build_matrix_top_level_context_uses_bare_name():
    entry = dcc.build_matrix(["solo/Dockerfile"])["include"][0]
    assert entry["image"] == "solo"
    assert entry["category"] == "."


def test_build_matrix_skips_invalid_image_names(capsys):
    assert dcc.build_matrix(["node/Bad_Name/Dockerfile"]) == {"include": []}
    assert "Skipping invalid image name" in capsys.readouterr().err


@pytest.mark.parametrize(
    "dockerfile",
    [
        "archived/parity/Dockerfile",
        "node/archived/Dockerfile",
        "node/foo/templates/Dockerfile",
        ".github/x/y/Dockerfile",
    ],
)
def test_build_matrix_rejects_excluded_segments(dockerfile):
    with pytest.raises(dcc.DetectionError, match="Excluded"):
        dcc.build_matrix([dockerfile])


def test_build_matrix_allows_names_that_merely_contain_archived():
    matrix = dcc.build_matrix(["node/archived-x/Dockerfile"])
    assert [e["image"] for e in matrix["include"]] == ["node-archived-x"]


def test_test_job_containers_match_previous_output():
    lines = dcc.render_outputs(dcc.FORMAT_TEST_CONTAINERS, ACTIVE)
    assert lines == [f"containers={GOLDEN_TEST_CONTAINERS}", "has-containers=true"]


def test_test_job_containers_empty():
    assert dcc.render_outputs(dcc.FORMAT_TEST_CONTAINERS, []) == [
        "containers=[]",
        "has-containers=false",
    ]


def test_render_outputs_rejects_unknown_format():
    with pytest.raises(dcc.DetectionError):
        dcc.render_outputs("nope", ACTIVE)


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------


def test_discover_dockerfiles_skips_excluded_and_pruned(tmp_path):
    for rel in [
        "node/alpine/Dockerfile",
        "node/release/Dockerfile",
        "node/alpine/Dockerfile.bak",
        "templates/base/Dockerfile",
        "archived/old/Dockerfile",
        ".devcontainer/Dockerfile",
        ".github/x/Dockerfile",
        "node/alpine/node_modules/pkg/Dockerfile",
        "Dockerfile",
        "newtop/img/Dockerfile",
    ]:
        path = tmp_path / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("FROM scratch\n")
    assert dcc.discover_dockerfiles(tmp_path) == [
        "newtop/img/Dockerfile",
        "node/alpine/Dockerfile",
        "node/release/Dockerfile",
    ]


# ---------------------------------------------------------------------------
# Git-backed detection and the CLI
# ---------------------------------------------------------------------------


def _git(repo: Path, *args: str) -> str:
    env = {
        **os.environ,
        "GIT_AUTHOR_NAME": "t",
        "GIT_AUTHOR_EMAIL": "t@example.com",
        "GIT_COMMITTER_NAME": "t",
        "GIT_COMMITTER_EMAIL": "t@example.com",
        "GIT_CONFIG_GLOBAL": os.devnull,
        "GIT_CONFIG_SYSTEM": os.devnull,
    }
    return subprocess.run(
        ["git", *args],
        cwd=repo,
        env=env,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def _commit(repo: Path, files: dict[str, str], message: str = "c") -> str:
    for rel, content in files.items():
        path = repo / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
    _git(repo, "add", "-A")
    _git(repo, "commit", "-q", "-m", message)
    return _git(repo, "rev-parse", "HEAD")


@pytest.fixture
def repo(tmp_path):
    root = tmp_path / "repo"
    root.mkdir()
    _git(root, "init", "-q", "-b", "main")
    _commit(
        root,
        {
            "node/alpine/Dockerfile": "FROM scratch\n",
            "node/alpine/package-lock.json": "{}\n",
            "node/alpine/index.js": "1\n",
            "node/release/Dockerfile": "FROM scratch\n",
            "node/release/package-lock.json": "{}\n",
            "templates/base/Dockerfile": "FROM scratch\n",
            "archived/old/Dockerfile": "FROM scratch\n",
            "README.md": "hi\n",
        },
        "base",
    )
    return root


def _run_cli(repo: Path, fmt: str, event: str, base: str, head: str):
    return dcc.main(
        [
            "--format",
            fmt,
            "--event",
            event,
            "--base",
            base,
            "--head",
            head,
            "--root",
            str(repo),
        ]
    )


def _outputs(capsys) -> dict[str, str]:
    out = capsys.readouterr().out
    return dict(line.split("=", 1) for line in out.splitlines())


def test_push_lockfile_only_change_selects_that_context(repo, capsys):
    before = _git(repo, "rev-parse", "HEAD")
    after = _commit(repo, {"node/alpine/package-lock.json": '{"v":2}\n'})
    assert _run_cli(repo, "build-matrix", "push", before, after) == 0
    outputs = _outputs(capsys)
    assert outputs["has_changes"] == "true"
    matrix = json.loads(outputs["matrix"])
    assert [e["image"] for e in matrix["include"]] == ["node-alpine"]


def test_push_covers_multi_commit_range(repo, capsys):
    before = _git(repo, "rev-parse", "HEAD")
    _commit(repo, {"node/alpine/index.js": "2\n"})
    after = _commit(repo, {"node/release/package-lock.json": '{"v":2}\n'})
    assert _run_cli(repo, "test-containers", "push", before, after) == 0
    outputs = _outputs(capsys)
    paths = [c["path"] for c in json.loads(outputs["containers"])]
    assert paths == ["node/alpine", "node/release"]


def test_push_docs_only_selects_nothing(repo, capsys):
    before = _git(repo, "rev-parse", "HEAD")
    after = _commit(
        repo,
        {
            "README.md": "changed\n",
            "templates/base/new.txt": "x\n",
            "archived/old/y": "x",
        },
    )
    assert _run_cli(repo, "build-matrix", "push", before, after) == 0
    assert _outputs(capsys) == {
        "has_changes": "false",
        "matrix": '{"include":[]}',
    }


def test_push_deleting_a_context_selects_nothing_for_it(repo, capsys):
    before = _git(repo, "rev-parse", "HEAD")
    _git(repo, "rm", "-rq", "node/release")
    _git(repo, "commit", "-q", "-m", "drop")
    after = _git(repo, "rev-parse", "HEAD")
    assert _run_cli(repo, "test-containers", "push", before, after) == 0
    assert _outputs(capsys)["has-containers"] == "false"


def test_push_rename_counts_old_and_new_locations(repo, capsys):
    before = _git(repo, "rev-parse", "HEAD")
    _git(repo, "mv", "node/alpine/index.js", "node/release/index.js")
    _git(repo, "commit", "-q", "-m", "mv")
    after = _git(repo, "rev-parse", "HEAD")
    assert _run_cli(repo, "test-containers", "push", before, after) == 0
    paths = [c["path"] for c in json.loads(_outputs(capsys)["containers"])]
    assert paths == ["node/alpine", "node/release"]


@pytest.mark.parametrize("before", [ZERO_SHA, "0" * 64, ""])
def test_push_new_branch_selects_all(repo, capsys, before):
    head = _git(repo, "rev-parse", "HEAD")
    assert _run_cli(repo, "build-matrix", "push", before, head) == 0
    images = [e["image"] for e in json.loads(_outputs(capsys)["matrix"])["include"]]
    assert images == ["node-alpine", "node-release"]


def test_workflow_dispatch_selects_all_without_git_refs(repo, capsys):
    assert _run_cli(repo, "test-containers", "workflow_dispatch", "", "") == 0
    paths = [c["path"] for c in json.loads(_outputs(capsys)["containers"])]
    assert paths == ["node/alpine", "node/release"]


def test_pull_request_uses_merge_base_diff(repo, capsys):
    base = _git(repo, "rev-parse", "HEAD")
    # main moves on with a change to node/release after the PR branched off.
    _git(repo, "checkout", "-q", "-b", "feature")
    head = _commit(repo, {"node/alpine/package.json": "{}\n"})
    _git(repo, "checkout", "-q", "main")
    new_base = _commit(repo, {"node/release/index.js": "main-only\n"})
    # Three-dot: only the PR's own change (alpine) counts, not main's (release).
    assert _run_cli(repo, "test-containers", "pull_request", new_base, head) == 0
    paths = [c["path"] for c in json.loads(_outputs(capsys)["containers"])]
    assert paths == ["node/alpine"]
    assert base != new_base


def test_git_failure_is_loud_not_empty(repo, capsys):
    head = _git(repo, "rev-parse", "HEAD")
    missing = "1" * 40
    assert _run_cli(repo, "build-matrix", "push", missing, head) == 1
    captured = capsys.readouterr()
    assert captured.out == ""
    assert "ERROR" in captured.err


@pytest.mark.parametrize("bad", ["HEAD~1", "not a sha", "abc;rm"])
def test_non_sha_refs_are_rejected(repo, capsys, bad):
    head = _git(repo, "rev-parse", "HEAD")
    assert _run_cli(repo, "build-matrix", "pull_request", bad, head) == 1
    assert "Invalid base SHA" in capsys.readouterr().err


def test_pull_request_requires_base_and_head(repo, capsys):
    assert _run_cli(repo, "build-matrix", "pull_request", "", "") == 1
    assert "requires both" in capsys.readouterr().err


def test_unsupported_event_fails(repo, capsys):
    assert _run_cli(repo, "build-matrix", "schedule", "", "") == 1
    assert "Unsupported event" in capsys.readouterr().err


# ---------------------------------------------------------------------------
# Workflow wiring: triggers and shared detector usage
# ---------------------------------------------------------------------------


def _glob_to_regex(pattern: str) -> re.Pattern:
    out, i = "", 0
    while i < len(pattern):
        if pattern.startswith("**/", i):
            out += "(?:.*/)?"
            i += 3
        elif pattern.startswith("**", i):
            out += ".*"
            i += 2
        elif pattern[i] == "*":
            out += "[^/]*"
            i += 1
        else:
            out += re.escape(pattern[i])
            i += 1
    return re.compile(f"^{out}$")


def _path_filter_matches(patterns: list[str], path: str) -> bool:
    """GitHub `paths` semantics: the last matching pattern decides."""
    matched = False
    for pattern in patterns:
        negated = pattern.startswith("!")
        if _glob_to_regex(pattern.lstrip("!")).match(path):
            matched = not negated
    return matched


def _load_workflow(name: str) -> dict:
    return yaml.safe_load((WORKFLOWS / name).read_text())


def _trigger_paths(event: str) -> list[str]:
    workflow = _load_workflow("build-publish.yaml")
    return workflow[True][event]["paths"]  # PyYAML parses the `on` key as True


@pytest.mark.parametrize("event", ["push", "pull_request"])
@pytest.mark.parametrize(
    "name",
    [
        "package-lock.json",
        "package.json",
        "index.js",
        "docker-entrypoint.sh",
        "Dockerfile",
        "src/new/file.ts",
    ],
)
def test_build_publish_triggers_cover_every_active_context(event, name):
    """A new image context under a new top-level dir fails here until its glob
    is added to build-publish.yaml's `paths`."""
    patterns = _trigger_paths(event)
    for dockerfile in dcc.discover_dockerfiles(REPO_ROOT):
        context = dockerfile.rsplit("/", 1)[0]
        assert _path_filter_matches(
            patterns, f"{context}/{name}"
        ), f"{event} paths do not trigger for {context}/{name}"


@pytest.mark.parametrize("event", ["push", "pull_request"])
def test_build_publish_triggers_keep_exclusions(event):
    patterns = _trigger_paths(event)
    for excluded in (
        "archived/parity/branch/Dockerfile",
        "templates/base/alpine/Dockerfile",
        ".devcontainer/Dockerfile",
    ):
        assert not _path_filter_matches(patterns, excluded)
    assert not _path_filter_matches(patterns, "README.md")


@pytest.mark.parametrize("workflow", ["build-publish.yaml", "test.yaml"])
def test_workflows_use_the_shared_detector(workflow):
    text = (WORKFLOWS / workflow).read_text()
    assert "scripts/detect_changed_containers.py" in text
    assert 'grep "Dockerfile$"' not in text
    assert "git diff --name-only" not in text


def test_test_workflow_detection_is_not_gated_on_the_python_path_filter():
    detect = _load_workflow("test.yaml")["jobs"]["detect-containers"]
    assert "needs" not in detect
    assert "if" not in detect


@pytest.mark.parametrize("workflow", ["build-publish.yaml", "test.yaml"])
def test_workflows_pass_pr_and_push_ranges_to_the_detector(workflow):
    text = (WORKFLOWS / workflow).read_text()
    assert "github.event.pull_request.base.sha || github.event.before" in text
    assert "github.event.pull_request.head.sha || github.sha" in text


def test_test_workflow_prepare_filter_counts_context_changes():
    steps = _load_workflow("test.yaml")["jobs"]["prepare"]["steps"]
    filters = yaml.safe_load(
        next(s for s in steps if s.get("id") == "filter")["with"]["filters"]
    )["changes"]
    for dockerfile in dcc.discover_dockerfiles(REPO_ROOT):
        context = dockerfile.rsplit("/", 1)[0]
        for name in ("package-lock.json", "package.json", "index.js", "x.sh"):
            assert _path_filter_matches(filters, f"{context}/{name}")
    assert not _path_filter_matches(filters, "templates/base/alpine/x.sh")
    assert not _path_filter_matches(filters, "archived/parity/branch/x.sh")


AGGREGATORS = {
    "container-builds-result": "container-builds",
    "security-scan-result": "security-scan",
}


@pytest.mark.parametrize("aggregator, matrix_job", sorted(AGGREGATORS.items()))
def test_test_workflow_aggregators_fail_when_detection_fails(aggregator, matrix_job):
    """A failed detector skips the matrix job; the required check must not pass."""
    job = _load_workflow("test.yaml")["jobs"][aggregator]
    assert job["if"] == "always()"
    assert {"detect-containers", matrix_job} <= set(job["needs"])
    (step,) = job["steps"]
    # Results travel through env, never interpolated into the script.
    assert "${{" not in step["run"]
    assert step["env"]["DETECT_RESULT"] == "${{ needs.detect-containers.result }}"
    assert step["env"]["JOB_RESULT"] == f"${{{{ needs.{matrix_job}.result }}}}"
    assert '"$DETECT_RESULT"' in step["run"] and '"$JOB_RESULT"' in step["run"]
    assert '"failure"' in step["run"] and '"cancelled"' in step["run"]


def test_build_publish_only_the_matrix_job_depends_on_detection():
    """No always() aggregator can mask a detect-changes failure: the only
    dependent is the matrix job, and 'Detect Changed Containers' itself is the
    required check that goes red."""
    jobs = _load_workflow("build-publish.yaml")["jobs"]
    dependents = {
        name
        for name, job in jobs.items()
        if "detect-changes"
        in (
            [job.get("needs")]
            if isinstance(job.get("needs"), str)
            else job.get("needs", [])
        )
    }
    assert dependents == {"build-multiarch"}
    assert (
        jobs["build-multiarch"]["if"]
        == "needs.detect-changes.outputs.has_changes == 'true'"
    )


@pytest.mark.parametrize("workflow", ["build-publish.yaml", "test.yaml"])
def test_push_runs_queue_instead_of_cancelling(workflow):
    """Each push diffs only before..sha; cancelling run A would drop A's changes."""
    concurrency = _load_workflow(workflow)["concurrency"]
    assert (
        concurrency["cancel-in-progress"]
        == "${{ github.event_name == 'pull_request' }}"
    )
    assert "github.ref" in concurrency["group"]


@pytest.mark.parametrize(
    "workflow, job",
    [("build-publish.yaml", "detect-changes"), ("test.yaml", "detect-containers")],
)
def test_detect_jobs_have_read_only_contents_permission(workflow, job):
    assert _load_workflow(workflow)["jobs"][job]["permissions"] == {"contents": "read"}

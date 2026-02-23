"""Dockerfile policy tests — RED phase.

Tests fail against current state and turn green as gaps are fixed per issue #431.
"""

import os
import re

import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_dockerfile(path: str) -> str:
    full_path = os.path.join(REPO_ROOT, path)
    with open(full_path) as f:
        return f.read()


def from_lines(content: str) -> list[str]:
    """Return all FROM lines from Dockerfile content."""
    return [
        line.strip()
        for line in content.splitlines()
        if line.strip().upper().startswith("FROM ")
    ]


# ---------------------------------------------------------------------------
# P1: Base image digest pinning in templates
# ---------------------------------------------------------------------------


def test_base_image_digest_pinning_templates():
    """All template FROM lines must include @sha256: digest."""
    templates = [
        "templates/base/alpine/Dockerfile",
        "templates/apps/nodejs/express/Dockerfile",
        "templates/apps/python/fastapi/Dockerfile",
        "templates/databases/postgresql/Dockerfile",
    ]
    failures = []
    for tmpl in templates:
        content = read_dockerfile(tmpl)
        for line in from_lines(content):
            if "@sha256:" not in line:
                failures.append(f"{tmpl}: {line}")
    assert not failures, "Template FROM lines missing @sha256: digest:\n" + "\n".join(
        failures
    )


def test_go_template_builder_digest_pinning():
    """Go template builder FROM line must include @sha256: digest."""
    content = read_dockerfile("templates/microservices/go/Dockerfile")
    builder_froms = [l for l in from_lines(content) if "golang" in l.lower()]
    failures = [l for l in builder_froms if "@sha256:" not in l]
    assert not failures, "Go template builder FROM missing @sha256::\n" + "\n".join(
        failures
    )


def test_go_template_no_alpine_latest():
    """Go template runtime stage must not reference alpine:latest tag."""
    content = read_dockerfile("templates/microservices/go/Dockerfile")
    # alpine:latest is unacceptable even with a sha256 digest appended;
    # the tag "latest" is semantically non-deterministic.
    assert "alpine:latest" not in content, (
        "templates/microservices/go/Dockerfile uses 'alpine:latest' — "
        "must use an explicit version tag, e.g. alpine:3.21"
    )


def test_uid_gid_defaults_alpine():
    """node/alpine/Dockerfile must use explicit UID/GID 1000."""
    content = read_dockerfile("node/alpine/Dockerfile")
    assert re.search(r"-u\s+1000", content), (
        "node/alpine/Dockerfile: UID not set to 1000"
    )
    assert re.search(r"-g\s+1000", content), (
        "node/alpine/Dockerfile: GID not set to 1000"
    )


def test_uid_gid_defaults_release():
    """node/release/Dockerfile must use explicit UID/GID 1000."""
    content = read_dockerfile("node/release/Dockerfile")
    # Must explicitly set numeric UID and GID to 1000
    assert "1000" in content, "node/release/Dockerfile: no explicit UID/GID 1000 found"
    assert re.search(r"(useradd|groupadd).*\b1000\b", content), (
        "node/release/Dockerfile: useradd/groupadd does not specify 1000"
    )


# ---------------------------------------------------------------------------
# P2: OCI labels
# ---------------------------------------------------------------------------


def test_oci_base_labels_present():
    """node Dockerfiles must include OCI base image labels."""
    for variant in ["node/alpine/Dockerfile", "node/release/Dockerfile"]:
        content = read_dockerfile(variant)
        assert "org.opencontainers.image.base.name" in content, (
            f"{variant}: missing org.opencontainers.image.base.name label"
        )
        assert "org.opencontainers.image.base.digest" in content, (
            f"{variant}: missing org.opencontainers.image.base.digest label"
        )


def test_no_hardcoded_created_revision_in_templates():
    """Templates must not hardcode OCI created or revision labels."""
    templates = [
        "templates/base/alpine/Dockerfile",
        "templates/apps/nodejs/express/Dockerfile",
        "templates/apps/python/fastapi/Dockerfile",
        "templates/databases/postgresql/Dockerfile",
    ]
    failures = []
    for tmpl in templates:
        content = read_dockerfile(tmpl)
        if "org.opencontainers.image.created" in content:
            failures.append(f"{tmpl}: hardcodes 'created' label (must come from CI)")
        if "org.opencontainers.image.revision" in content:
            failures.append(f"{tmpl}: hardcodes 'revision' label (must come from CI)")
    assert not failures, "Templates with hardcoded created/revision:\n" + "\n".join(
        failures
    )


def test_no_deprecated_label_schema():
    """node Dockerfiles must not contain deprecated org.label-schema.* labels."""
    for variant in ["node/alpine/Dockerfile", "node/release/Dockerfile"]:
        content = read_dockerfile(variant)
        assert "org.label-schema." not in content, (
            f"{variant}: contains deprecated org.label-schema.* labels — remove them"
        )


def test_entrypoint_scripts_exist():
    """docker-entrypoint.sh must exist for each node variant."""
    for variant in ["node/alpine", "node/release"]:
        script_path = os.path.join(REPO_ROOT, variant, "docker-entrypoint.sh")
        assert os.path.exists(script_path), (
            f"{variant}/docker-entrypoint.sh does not exist"
        )


def test_entrypoint_scripts_referenced_in_dockerfiles():
    """Dockerfiles must reference docker-entrypoint.sh."""
    for variant in ["node/alpine/Dockerfile", "node/release/Dockerfile"]:
        content = read_dockerfile(variant)
        assert "docker-entrypoint.sh" in content, (
            f"{variant}: does not reference docker-entrypoint.sh"
        )


# ---------------------------------------------------------------------------
# P3: Package version pinning
# ---------------------------------------------------------------------------


def test_package_version_pinning_alpine_node():
    """node/alpine packages must be version-pinned (apk add pkg=version)."""
    content = read_dockerfile("node/alpine/Dockerfile")
    pkg_names = ["ca-certificates", "curl", "tini"]
    failures = []
    for pkg in pkg_names:
        if pkg in content and f"{pkg}=" not in content:
            failures.append(f"node/alpine/Dockerfile: '{pkg}' not version-pinned")
    assert not failures, "\n".join(failures)


def test_package_version_pinning_release_node():
    """node/release packages must be version-pinned (apt-get install pkg=version)."""
    content = read_dockerfile("node/release/Dockerfile")
    pkg_names = ["ca-certificates", "curl", "tini"]
    failures = []
    for pkg in pkg_names:
        if pkg in content and f"{pkg}=" not in content:
            failures.append(f"node/release/Dockerfile: '{pkg}' not version-pinned")
    assert not failures, "\n".join(failures)


def test_devcontainer_package_pinning():
    """devcontainer packages must be version-pinned."""
    content = read_dockerfile(".devcontainer/Dockerfile")
    for pkg in ["python3", "py3-pip", "bash"]:
        assert f"{pkg}=" in content, (
            f".devcontainer/Dockerfile: '{pkg}' not version-pinned"
        )


def test_devcontainer_non_root_user():
    """devcontainer must define a non-root user."""
    content = read_dockerfile(".devcontainer/Dockerfile")
    # Must have a USER directive that is not 'root'
    has_user = re.search(r"^USER\s+(?!root\s*$)\S+", content, re.MULTILINE)
    assert has_user, ".devcontainer/Dockerfile has no non-root USER directive"


def test_download_verification_parity_release():
    """archived/parity/release must verify downloads via GPG or SHA256."""
    content = read_dockerfile("archived/parity/release/Dockerfile")
    # Exclude the dockerfile syntax directive which contains '@sha256:' but is not verification
    payload_lines = [l for l in content.splitlines() if not l.strip().startswith("# syntax=")]
    payload = "\n".join(payload_lines)
    has_gpg = bool(re.search(r"\bgpg\b|\bgnupg\b|\bgpgv\b", payload, re.IGNORECASE))
    has_sha256 = bool(re.search(r"\bsha256sum\b", payload))
    assert has_gpg or has_sha256, (
        "archived/parity/release/Dockerfile: downloads .deb without GPG or SHA256 verification"
    )

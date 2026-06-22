# AGENTS.md

## Project Overview

Container collection repo with Dockerfiles (`node/alpine/`, `node/release/`), Python automation scripts (`scripts/`), and GitHub Actions CI/CD. Uses mise for tool management, Poetry for Python, pnpm for Node.js tooling.

## Tool Versions (from mise.toml)

- Python 3.13 (Poetry for deps/venv, `.venv` in project root)
- Node.js 24.14.0 (pnpm 10.33.0)
- Pre-commit hooks for formatting/linting

## WHERE TO LOOK

| Task | Location | Notes |
|------|----------|-------|
| Add/modify a container image | `node/{alpine,release}/Dockerfile` | See Dockerfile Style below |
| Write Python automation | `scripts/*.py` | See `scripts/AGENTS.md` for patterns |
| Fix CI/CD | `.github/workflows/` | See `.github/workflows/AGENTS.md` |
| Add container template | `templates/` | Excluded from linting — see `templates/AGENTS.md` |
| Run linting/tests | Commands below | `pre-commit run --all-files` is the catch-all |
| Configure AI features | `ai_config.example.yaml`, `docs/AI_CONFIGURATION.md` | Initialize via `poetry run containers ai config --init` |
| Change tool versions | `mise.toml` | Never install Python/Node directly |
| Change dev environment | `.devcontainer/` | Docker-in-Docker setup |
| Review archived containers | `archived/` | Legacy, excluded from CI — don't modify |

## Build / Lint / Test Commands

```bash
# Setup
mise install && poetry install && pnpm install && pre-commit install

# Lint everything (pre-commit runs all hooks)
pre-commit run --all-files

# Individual linters
poetry run black --check --diff scripts/*.py     # Python formatting
poetry run isort --check-only --diff scripts/*.py # Python import order
yamllint -c .yamllint.yaml .                      # YAML linting
pnpm run format                                   # Prettier (JS/YAML/MD)

# Fix formatting
poetry run black scripts/*.py
poetry run isort scripts/*.py
pnpm run format                                   # Prettier writes in-place

# Python tests
poetry run pytest -v                              # All tests
poetry run pytest test_ai_cli.py -v               # Single test file
poetry run pytest test_ai_cli.py::TestClass -v    # Single test class
poetry run pytest test_ai_cli.py::test_func -v    # Single test function
poetry run pytest -k "keyword" -v                 # Tests matching keyword

# Validate project config
poetry check

# Container builds (local)
docker build -t test-image:latest node/alpine/
docker build -t test-image:latest node/release/

# Script entry points (via Poetry)
poetry run containers --help              # Main CLI (list, generate, analyze)
poetry run generate-dockerfile --help     # Dockerfile generation
poetry run collect-docker-metrics --help  # Docker metrics collection
poetry run generate-image-tags --help     # Image tag generation
poetry run template-engine --help         # Template engine
poetry run template-testing --help        # Template test framework
poetry run generate-docs --help           # Documentation generation
poetry run ai-chat --help                 # AI chat interface
poetry run ai-analyze --help              # AI project analysis
poetry run ai-recommend --help            # AI template recommendations
```

## Python Code Style

**Formatter**: Black, 88-char line length **Import sorting**: isort with `profile = "black"` **Target**: Python 3.13+ (type hints from `typing` module)

### Import Order

```python
# 1. stdlib
import argparse
import os

# 2. third-party
import requests
import yaml

# 3. local
from scripts.generate_dockerfile import generate_dockerfile_content
```

### Function Signatures

```python
def generate_dockerfile_content(
    base_image: str,
    packages: Optional[str] = None,
    env_vars: Optional[str] = None,
    architecture: Optional[str] = None,
) -> str:
    """Generate Dockerfile content with specified parameters."""
```

- Use type hints on all function parameters and return types
- Use `Optional[X]` for nullable params, `List`, `Dict` from `typing`
- Trailing commas on multi-line parameter lists
- Docstrings on all public functions

### Error Handling

```python
try:
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result
except subprocess.CalledProcessError as e:
    self.log(f"Command failed: {' '.join(cmd)}", "ERROR")
    raise
```

- Catch specific exceptions, not bare `except`
- Log informative error messages before re-raising
- Use `check=True` with `subprocess.run`

### Naming

- `snake_case` for functions, variables, modules
- `UPPER_SNAKE_CASE` for constants (e.g., `PLATFORM_CONFIGS`, `PACKAGE_MANAGERS`)
- Descriptive names; no single-letter variables outside comprehensions

## JavaScript / Prettier Style

**Config**: `@bfra.me/prettier-config/120-proof`

| Setting                     | Value |
| --------------------------- | ----- |
| printWidth                  | 120   |
| semi                        | false |
| singleQuote                 | true  |
| bracketSpacing              | false |
| arrowParens                 | avoid |
| endOfLine                   | auto  |
| tabWidth (JSON in .vscode/) | 4     |
| proseWrap (Markdown)        | never |

## YAML Style

- 2-space indentation
- Max 120 chars per line (warning level)
- No document start marker (`---` not required)
- Minimal quoting
- yamllint config: `.yamllint.yaml`
- `.github/workflows/*.yml` and `templates/` are excluded from yamllint

## Dockerfile Style

- **Lowercase instructions** preferred (`.dockerfilelintrc` warns on uppercase)
- Pin base images with SHA256 digests when available
- Combine `RUN` commands to minimize layers
- Create non-root user: `RUN useradd --create-home --shell /bin/bash appuser && USER appuser`
- Use `$TARGETPLATFORM` / `$TARGETARCH` for multi-arch builds
- Clean package caches: `rm -rf /var/lib/apt/lists/*` or `apk add --no-cache`
- `templates/` and `node/` directories excluded from dockerfilelint
- Use `# syntax=docker/dockerfile:1.x@sha256:...` for advanced features
- Health checks: 30s intervals with curl-based probes
- CI-injected labels — do NOT hardcode `created` or `revision` (set by `docker/metadata-action`)

## GitHub Actions Style

- **Pin all actions with full SHA256 hashes** + version comment:
  ```yaml
  uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
  ```
- Exclude `archived/`, `templates/`, `.devcontainer/` from CI detection
- Container image naming: `category-variant` (e.g., `node-alpine`)
- Dual-publish to GHCR (`ghcr.io/marcusrbrown/IMAGE`) and Docker Hub

## EditorConfig

- UTF-8, LF line endings, 2-space indent, final newline
- Trailing whitespace preserved in `*.md`, `*.txt`, `*.yml`

## Directory Structure

```
node/alpine/Dockerfile         # Alpine-based Node.js container
node/release/Dockerfile        # Debian Bookworm-based Node.js container
scripts/*.py                   # Automation scripts (Poetry entry points) — see scripts/AGENTS.md
templates/                     # Container templates, excluded from linting — see templates/AGENTS.md
archived/                      # Legacy containers (excluded from CI, do not modify)
tests/                         # Python test suite (pytest)
docs/                          # Project documentation (multi-arch, AI CLI, templates)
.github/workflows/             # CI/CD pipelines — see .github/workflows/AGENTS.md
.github/actions/setup/         # Shared composite action (mise + Poetry setup)
.devcontainer/                 # Docker-in-Docker dev environment
```

## Key Conventions

- **mise manages all tools** — never install Python/Node/pnpm directly
- **Poetry scripts** are the entry points for automation (`pyproject.toml [tool.poetry.scripts]`)
- **AI features require `ai_config.yaml`** — generate from `ai_config.example.yaml` or `poetry run containers ai config --init`
- **Pre-commit hooks** enforce trailing whitespace, EOF newlines, dockerfilelint, yamllint
- **`templates/` is excluded from everything** — linting, formatting, CI detection, yamllint, prettier, dockerfilelint
- **Comments**: explain _why_, not _what_. Self-documenting code preferred. Use annotations (`TODO:`, `FIXME:`, `HACK:`, `NOTE:`) when context is needed
- **No secrets** in container images, commits, or logs
- **Security scanning**: Trivy for container vulnerabilities, Hadolint for Dockerfile best practices

## Anti-Patterns (This Project)

- Do NOT hardcode OCI labels `created` or `revision` — CI injects via `docker/metadata-action`
- Do NOT run linters/formatters against `templates/` — intentionally excluded
- Do NOT modify `archived/` — legacy containers with broken dependencies
- Dockerfile policy tests in `tests/test_dockerfile_policy.py` intentionally fail against current state (tracking issue)
- Renovate manages dependency updates — do NOT manually update lockfiles unless necessary

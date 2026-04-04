# .github/workflows/AGENTS.md

CI/CD pipelines for building, testing, and publishing container images. All workflow files use `.yaml` extension.

## Workflow Map

| Workflow | Trigger | Purpose |
|----------|---------|---------|
| `build-publish.yaml` | push/PR/dispatch | Build + push multi-arch container images to GHCR and Docker Hub |
| `test.yaml` | push/PR/dispatch | Run pytest suite |
| `container-scan.yaml` | push/PR/schedule | Trivy vulnerability scanning on container images |
| `release.yaml` | push (tags)/dispatch | Docker release workflow |
| `renovate.yaml` | push/PR/dispatch | Dependency updates via Renovate |
| `cache-cleanup.yaml` | PR/schedule/dispatch | Clean up GitHub Actions caches |
| `dockerfile_generation.yaml` | dispatch | Generate Dockerfiles from templates |
| `metrics_collector.yaml` | schedule/dispatch | Collect Docker metrics |
| `fro-bot.yaml` | PR/schedule/dispatch | Fro Bot automation |
| `update-repo-settings.yaml` | push/schedule/dispatch | Sync repo settings from `.github/settings.yml` |

## Shared Setup Action

`.github/actions/setup/action.yml` — composite action used by most workflows:

1. Installs mise (tool manager)
2. Runs `mise install` (Python + Node.js + pnpm)
3. Installs Poetry dependencies
4. Installs pnpm dependencies

Usage:
```yaml
- uses: ./.github/actions/setup
```

## Key Patterns

### Action Pinning (MANDATORY)

Every action reference uses full SHA256 + version comment:
```yaml
uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
```

Never use `@v4` or `@main` — always full SHA.

### Path Exclusions

Workflows exclude `archived/`, `templates/`, `.devcontainer/` from change detection:
```yaml
paths-ignore:
  - 'archived/**'
  - 'templates/**'
  - '.devcontainer/**'
```

### Container Image Publishing

Dual-publish to:
- **GHCR**: `ghcr.io/marcusrbrown/<image-name>`
- **Docker Hub**: `marcusrbrown/<image-name>`

Image naming: `category-variant` (e.g., `node-alpine`, `node-release`)

OCI labels injected automatically by `docker/metadata-action` — do NOT hardcode `created`, `revision`, `version`.

### Multi-Architecture Builds

Uses `docker/build-push-action` with QEMU for cross-platform builds:
- `linux/amd64`
- `linux/arm64`

### Secrets

- `GITHUB_TOKEN` — automatic, used for GHCR
- `DOCKERHUB_USERNAME` / `DOCKERHUB_TOKEN` — Docker Hub publishing
- Do NOT log or echo secrets

## Anti-Patterns

- Do NOT use `@v4` style action references — always pin full SHA
- Do NOT add `templates/` or `archived/` to CI path triggers
- Do NOT hardcode OCI labels — `docker/metadata-action` handles them
- Do NOT create duplicate setup steps — use the shared composite action
- Workflow files use `.yaml` extension, not `.yml`

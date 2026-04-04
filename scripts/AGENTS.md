# scripts/AGENTS.md

Python automation scripts for container management, template generation, and AI-assisted analysis. All scripts are registered as Poetry entry points in `pyproject.toml`.

## File Map

| File | LOC | Purpose | Entry Point |
|------|-----|---------|-------------|
| `containers_cli.py` | 1340 | Main CLI — list, generate, analyze containers | `poetry run containers` |
| `containers_simple.py` | 159 | Simplified container operations | — |
| `template_documentation.py` | 2071 | Generate docs from templates | `poetry run generate-docs` |
| `template_intelligence.py` | 1018 | AI-powered template recommendations | `poetry run ai-recommend` |
| `template_engine.py` | 710 | Jinja2 template rendering engine | `poetry run template-engine` |
| `template_testing.py` | 770 | Template test framework | `poetry run template-testing` |
| `generate_dockerfile.py` | 398 | Dockerfile content generation | `poetry run generate-dockerfile` |
| `build_multiarch.py` | 513 | Multi-architecture build orchestration | — |
| `ai_chat_interface.py` | 630 | Interactive AI chat for container help | `poetry run ai-chat` |
| `ai_core.py` | 620 | Shared AI provider abstraction (OpenAI/Anthropic/Ollama) | — |
| `documentation_ai.py` | 613 | AI-enhanced documentation generation | `poetry run ai-analyze` |
| `predictive_maintenance.py` | 987 | Predictive maintenance analysis | — |
| `collect_docker_metrics.py` | 73 | Docker metrics collection | `poetry run collect-docker-metrics` |
| `generate_image_tags.py` | 49 | Image tag generation | `poetry run generate-image-tags` |

## Architecture

### AI Subsystem (`ai_core.py` → consumers)

`ai_core.py` provides `AIProvider` — a shared abstraction over OpenAI, Anthropic, and Ollama. Three scripts consume it:

- `ai_chat_interface.py` — interactive chat
- `documentation_ai.py` — documentation analysis
- `template_intelligence.py` — template recommendations

Pattern: each consumer instantiates `AIProvider`, calls `generate()` with a prompt, parses the response.

### Template Subsystem (`template_engine.py` → `template_testing.py` → `template_documentation.py`)

- `template_engine.py` — Jinja2-based renderer, reads `template.yaml` configs from `templates/`
- `template_testing.py` — validates templates build and pass health checks
- `template_documentation.py` — generates markdown docs from template metadata

### Container Management (`containers_cli.py`, `generate_dockerfile.py`, `build_multiarch.py`)

- `containers_cli.py` — main CLI, subcommands: `list`, `generate`, `analyze`
- `generate_dockerfile.py` — generates Dockerfile content from parameters
- `build_multiarch.py` — orchestrates multi-arch builds via `docker buildx`

## Code Patterns

### Dataclass Configuration

```python
@dataclass
class PlatformConfig:
    """Platform-specific build configuration."""
    name: str
    architectures: List[str]
    base_images: Dict[str, str]
```

Used extensively for structured configs — `PLATFORM_CONFIGS`, `PACKAGE_MANAGERS`, template metadata.

### Logging Pattern

```python
def log(self, message: str, level: str = "INFO") -> None:
    """Structured logging with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] [{level}] {message}")
```

Custom `log()` method on classes — not stdlib `logging`. Consistent across all scripts.

### CLI Pattern (argparse)

```python
def main():
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument("--output", type=str, help="...")
    args = parser.parse_args()
    # ...
```

All entry points use `argparse`. No Click/Typer.

## Anti-Patterns

- No `__init__.py` — scripts are standalone modules, not a package
- Do NOT add relative imports between scripts — use absolute `from scripts.X import Y`
- Do NOT use stdlib `logging` — follow the existing `log()` method pattern
- Do NOT add new CLI frameworks (Click, Typer) — use argparse

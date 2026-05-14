"""Tests for the main container CLI command behavior."""

import json

import scripts.containers_cli as cli_module


class DummyEngine:
    def __init__(self):
        self.generated_args = None

    def list_templates(self, category=None):
        return [
            {
                "name": "express-api",
                "category": category or "app",
                "version": "1.0.0",
                "description": "Express service template",
                "tags": ["node", "express"],
            }
        ]

    def generate_template(self, template, output, params, dry_run):
        self.generated_args = (template, output, params, dry_run)
        return {f"{output}/Dockerfile": "FROM alpine:3.21\n"}

    def validate_template(self, template):
        return {"valid": True, "errors": [], "warnings": []}

    def resolve_inheritance(self, template):
        return {
            "name": "express-api",
            "description": "Example",
            "version": "1.0.0",
            "category": "app",
            "author": "Test",
            "files": {"dockerfile": "Dockerfile"},
            "parameters": {},
        }


class DummyTesting:
    async def run_template_tests(self, *_args, **_kwargs):
        class Result:
            failed = 0
            passed = 2
            total_tests = 2

        return Result()

    def generate_test_report(self, _suite):
        return "ok"


class DummyDocs:
    def generate_template_documentation(self, _template):
        return "docs.md"

    def generate_all_documentation(self):
        return ["a.md"]


class DummyTemplateIntelligence:
    def recommend_templates(self, _path):
        return []

    def analyze_project(self, _path):
        return object()

    def infer_parameters(self, _template, _project):
        return {}


class DummyAssistant:
    def chat(self, _message, _context):
        return "ok"


class DummyMaintenance:
    def analyze_template(self, _template):
        return []

    def generate_maintenance_report(self):
        return {}


class DummyAIDocs:
    def generate_readme(self, _template, _config):
        return "README"

    def generate_api_docs(self, _config):
        return "API"

    def generate_troubleshooting_guide(self, _config):
        return "TS"


def _build_cli(monkeypatch):
    engine = DummyEngine()
    monkeypatch.setattr(cli_module, "TemplateEngine", lambda: engine)
    monkeypatch.setattr(cli_module, "TemplateTestFramework", lambda: DummyTesting())
    monkeypatch.setattr(cli_module, "DocumentationGenerator", lambda: DummyDocs())
    monkeypatch.setattr(cli_module, "AICore", lambda: object())
    monkeypatch.setattr(
        cli_module, "TemplateIntelligence", lambda: DummyTemplateIntelligence()
    )
    monkeypatch.setattr(cli_module, "TemplateAssistant", lambda: DummyAssistant())
    monkeypatch.setattr(cli_module, "PredictiveMaintenance", lambda: DummyMaintenance())
    monkeypatch.setattr(cli_module, "AIDocumentationGenerator", lambda: DummyAIDocs())
    return cli_module.ContainerTemplateCLI(), engine


def test_run_list_outputs_json(monkeypatch, capsys):
    cli, _ = _build_cli(monkeypatch)
    result = cli.run(["list", "--format", "json"])

    assert result == 0
    output = capsys.readouterr().out
    parsed = json.loads(output)
    assert parsed[0]["name"] == "express-api"


def test_generate_rejects_invalid_param_format(monkeypatch, tmp_path, capsys):
    cli, _ = _build_cli(monkeypatch)
    result = cli.run(["generate", "apps/nodejs/express", str(tmp_path), "--param", "bad"])

    assert result == 1
    assert "Invalid parameter format" in capsys.readouterr().out


def test_generate_passes_params_to_engine(monkeypatch, tmp_path):
    cli, engine = _build_cli(monkeypatch)
    result = cli.run(
        [
            "generate",
            "apps/nodejs/express",
            str(tmp_path),
            "--param",
            "app_name=myapp",
            "--dry-run",
        ]
    )

    assert result == 0
    assert engine.generated_args == (
        "apps/nodejs/express",
        str(tmp_path),
        {"app_name": "myapp"},
        True,
    )


def test_validate_command_success(monkeypatch):
    cli, _ = _build_cli(monkeypatch)
    result = cli.run(["validate", "apps/nodejs/express"])

    assert result == 0

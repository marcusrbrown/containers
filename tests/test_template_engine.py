"""Tests for the template engine core behavior."""

import pytest

from scripts.template_engine import TemplateEngine


def _base_template_metadata():
    return {
        "name": "base-template",
        "version": "1.0.0",
        "description": "Base image template",
        "category": "base",
        "parameters": {
            "app_name": {
                "type": "string",
                "description": "Application name",
                "default": "demo-app",
            },
            "replicas": {
                "type": "integer",
                "description": "Replica count",
                "required": True,
                "min": 1,
            },
        },
        "files": {
            "dockerfile": "Dockerfile",
        },
    }


def test_load_template_metadata_and_list_templates(template_factory):
    templates_dir, create_template = template_factory
    create_template(
        "base/alpine",
        _base_template_metadata(),
        {"Dockerfile": "FROM alpine:3.21\n"},
    )

    engine = TemplateEngine(str(templates_dir))
    metadata = engine.load_template_metadata("base/alpine")

    assert metadata["name"] == "base-template"
    assert "base/alpine" in engine._template_cache

    listed = engine.list_templates(category="base")
    assert listed[0]["path"] == "base/alpine"
    assert listed[0]["name"] == "base-template"


def test_load_template_metadata_missing_file_raises(template_factory):
    templates_dir, _ = template_factory
    engine = TemplateEngine(str(templates_dir))

    with pytest.raises(FileNotFoundError):
        engine.load_template_metadata("missing/template")


def test_resolve_inheritance_and_generate_template(template_factory, tmp_path):
    templates_dir, create_template = template_factory

    base_meta = _base_template_metadata()
    create_template(
        "base/alpine",
        base_meta,
        {"Dockerfile": "FROM alpine:3.21\nLABEL app={{ app_name }}\n"},
    )

    child_meta = {
        "name": "child-template",
        "version": "2.0.0",
        "description": "Child template",
        "category": "app",
        "inherits": "base/alpine",
        "parameters": {
            "app_name": {
                "type": "string",
                "description": "Override app name",
                "default": "child-app",
            }
        },
        "files": {"dockerfile": "Dockerfile"},
    }
    create_template(
        "apps/nodejs/express",
        child_meta,
        {"Dockerfile": "FROM alpine:3.21\nENV APP={{ app_name }}\n"},
    )

    engine = TemplateEngine(str(templates_dir))
    resolved = engine.resolve_inheritance("apps/nodejs/express")

    assert resolved["name"] == "child-template"
    assert "inherits" not in resolved
    assert "replicas" in resolved["parameters"]

    generated = engine.generate_template(
        "apps/nodejs/express",
        str(tmp_path / "out"),
        parameters={"replicas": 2, "app_name": "my-app"},
        dry_run=True,
    )

    output_path, output_content = next(iter(generated.items()))
    assert output_path.endswith("Dockerfile")
    assert "APP=my-app" in output_content


def test_generate_template_requires_required_parameters(template_factory, tmp_path):
    templates_dir, create_template = template_factory
    create_template(
        "base/alpine",
        _base_template_metadata(),
        {"Dockerfile": "FROM alpine:3.21\n"},
    )

    engine = TemplateEngine(str(templates_dir))

    with pytest.raises(ValueError, match="Required parameter 'replicas' not provided"):
        engine.generate_template("base/alpine", str(tmp_path / "out"), dry_run=True)


def test_validate_template_reports_missing_required_files(template_factory):
    templates_dir, create_template = template_factory
    metadata = _base_template_metadata()
    metadata["files"]["compose"] = "docker-compose.yml"

    create_template(
        "base/alpine",
        metadata,
        {"Dockerfile": "FROM alpine:3.21\n"},
    )

    engine = TemplateEngine(str(templates_dir))
    validation = engine.validate_template("base/alpine")

    assert validation["valid"] is False
    assert any("docker-compose.yml" in error for error in validation["errors"])


def test_generate_template_writes_files_when_not_dry_run(template_factory, tmp_path):
    templates_dir, create_template = template_factory
    create_template(
        "base/alpine",
        _base_template_metadata(),
        {"Dockerfile": "FROM alpine:3.21\nARG GENERATED={{ generated_by }}\n"},
    )

    engine = TemplateEngine(str(templates_dir))
    output_dir = tmp_path / "generated"
    generated = engine.generate_template(
        "base/alpine", str(output_dir), parameters={"replicas": 3}, dry_run=False
    )

    output_file = output_dir / "Dockerfile"
    assert str(output_file) in generated
    assert output_file.exists()
    assert "container-template-engine" in output_file.read_text()

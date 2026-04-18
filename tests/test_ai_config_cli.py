"""Tests for AI configuration scaffolding and validation."""

import asyncio
from argparse import Namespace
from pathlib import Path

import yaml

from scripts.containers_cli import ContainerTemplateCLI


REPO_ROOT = Path(__file__).resolve().parent.parent


def test_ai_config_example_has_required_sections():
    """ai_config.example.yaml should document required sections."""
    config_path = REPO_ROOT / "ai_config.example.yaml"
    config = yaml.safe_load(config_path.read_text())

    assert "ai" in config
    assert config["ai"]["default_provider"] in {"ollama", "openai", "anthropic"}
    assert "providers" in config["ai"]
    assert {"ollama", "openai", "anthropic"} <= set(config["ai"]["providers"].keys())
    assert "cache" in config["ai"]
    assert "analytics" in config["ai"]
    assert "features" in config["ai"]


def test_ai_config_command_parser_includes_config_subcommand():
    """CLI parser should expose the ai config command."""
    cli = ContainerTemplateCLI()
    parser = cli.create_parser()

    args = parser.parse_args(["ai", "config", "--validate"])
    assert args.command == "ai"
    assert args.ai_command == "config"
    assert args.validate is True


def test_ai_config_init_creates_file_from_example(tmp_path):
    """`containers ai config --init` should create a config file."""
    config_path = tmp_path / "ai_config.yaml"
    cli = ContainerTemplateCLI()
    args = Namespace(init=True, validate=False, path=str(config_path), force=False)

    exit_code = asyncio.run(cli.cmd_ai_config(args))

    assert exit_code == 0
    assert config_path.exists()
    created = yaml.safe_load(config_path.read_text())
    example = yaml.safe_load((REPO_ROOT / "ai_config.example.yaml").read_text())
    assert created == example


def test_ai_config_validate_reports_schema_errors(tmp_path):
    """`containers ai config --validate` should fail for invalid schema."""
    config_path = tmp_path / "ai_config.yaml"
    config_path.write_text(
        yaml.safe_dump(
            {
                "ai": {
                    "enabled": True,
                    "providers": {
                        "ollama": {"enabled": True},
                        "openai": {"enabled": True},
                        "anthropic": {"enabled": False},
                    },
                }
            }
        )
    )

    cli = ContainerTemplateCLI()
    args = Namespace(init=False, validate=True, path=str(config_path), force=False)
    exit_code = asyncio.run(cli.cmd_ai_config(args))

    assert exit_code == 1

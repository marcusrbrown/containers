"""Shared pytest fixtures for template and AI module tests."""

from pathlib import Path
from typing import Any, Dict

import pytest
import yaml


@pytest.fixture
def template_factory(tmp_path):
    """Create templates in an isolated temporary templates directory."""

    templates_dir = tmp_path / "templates"
    templates_dir.mkdir()

    def _create(
        template_path: str,
        metadata: Dict[str, Any],
        files: Dict[str, str],
    ) -> Path:
        template_dir = templates_dir / template_path
        template_dir.mkdir(parents=True, exist_ok=True)
        (template_dir / "template.yaml").write_text(yaml.safe_dump(metadata))

        for relative_path, content in files.items():
            file_path = template_dir / relative_path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            file_path.write_text(content)

        return template_dir

    return templates_dir, _create


@pytest.fixture
def sample_usage_stats_data():
    """Reusable usage stats payload for predictive maintenance tests."""

    return {
        "template_name": "apps/nodejs/express",
        "total_uses": 10,
        "success_rate": 0.6,
        "avg_build_time": 420.0,
        "common_parameters": {"node_version": "22"},
        "error_patterns": [
            "dependency install failed",
            "dependency conflict detected",
            "network timeout contacting package mirror",
        ],
        "performance_trends": [100.0] * 8 + [180.0] * 7,
    }

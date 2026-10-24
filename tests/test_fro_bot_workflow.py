"""Wiring tests for .github/workflows/fro-bot.yaml scheduled delivery."""

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW = yaml.safe_load(
    (REPO_ROOT / ".github" / "workflows" / "fro-bot.yaml").read_text()
)
AGENT_STEP = next(
    step
    for step in WORKFLOW["jobs"]["fro-bot"]["steps"]
    if step.get("uses", "").startswith("fro-bot/agent@")
)
SCHEDULE_PROMPT = " ".join(WORKFLOW["env"]["SCHEDULE_PROMPT"].split())


def test_output_mode_is_branch_pr_for_schedule_and_dispatch_only():
    """Autonomous runs deliver via PR; every other event leaves the input empty."""
    assert AGENT_STEP["with"]["output-mode"] == (
        '${{ contains(fromJSON(\'["schedule", "workflow_dispatch"]\'),'
        " github.event_name) && 'branch-pr' || '' }}"
    )


@pytest.mark.parametrize(
    "rule",
    [
        "Never push to a Renovate or Dependabot branch",
        "open a separate small PR against `main`",
        "Never push to `main` directly",
        "Open one PR per concern",
    ],
)
def test_schedule_prompt_carries_delivery_rules(rule):
    assert rule in SCHEDULE_PROMPT


def test_schedule_prompt_no_longer_pushes_to_every_pr_branch():
    assert "Check out each PR branch" not in SCHEDULE_PROMPT

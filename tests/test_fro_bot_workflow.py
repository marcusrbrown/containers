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
CHECKOUT_STEP = next(
    step
    for step in WORKFLOW["jobs"]["fro-bot"]["steps"]
    if step.get("uses", "").startswith("actions/checkout@")
)
SCHEDULE_PROMPT = " ".join(WORKFLOW["env"]["SCHEDULE_PROMPT"].split())


def test_output_mode_is_branch_pr_for_schedule_and_dispatch_only():
    """Autonomous runs deliver via PR; every other event leaves the input empty."""
    assert AGENT_STEP["with"]["output-mode"] == (
        '${{ contains(fromJSON(\'["schedule", "workflow_dispatch"]\'),'
        " github.event_name) && 'branch-pr' || '' }}"
    )


def test_checkout_persists_credentials_for_schedule_and_dispatch():
    """git push needs the checkout token, so only the review-style events opt out."""
    assert CHECKOUT_STEP["with"]["persist-credentials"] == (
        '${{ !contains(fromJSON(\'["pull_request", "issue_comment", "issues"]\'),'
        " github.event_name) }}"
    )


@pytest.mark.parametrize(
    "rule",
    [
        "only if a human or `fro-bot` authored it",
        "Never push to a Renovate or Dependabot branch, or to any other bot's branch",
        "(Copilot, github-actions, and so on)",
        "check for an open Fro Bot PR that already covers the same concern",
        "update that PR instead of opening another",
        "Fix and push only on PRs authored by a human or `fro-bot`",
        "open a separate small PR against `main`",
        "Never push to `main` directly",
        "Open one PR per concern",
    ],
)
def test_schedule_prompt_carries_delivery_rules(rule):
    assert rule in SCHEDULE_PROMPT


@pytest.mark.parametrize(
    "stale", ["Check out each PR branch", "pushing fixes directly", "non-bot"]
)
def test_schedule_prompt_drops_ambiguous_or_unsafe_wording(stale):
    assert stale not in SCHEDULE_PROMPT

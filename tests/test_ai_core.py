"""Tests for AI core orchestration and caching behavior."""

import tempfile

from scripts.ai_core import AICache, AICore, AIResponse


class StubProvider:
    def __init__(self, available=True, should_fail=False):
        self.available = available
        self.should_fail = should_fail
        self.chat_calls = 0
        self.analysis_calls = 0

    def is_available(self):
        return self.available

    def chat_completion(self, messages, model=None):
        self.chat_calls += 1
        if self.should_fail:
            raise RuntimeError("provider unavailable")
        return AIResponse(
            content=f"reply:{messages[0]['content']}",
            confidence=0.9,
            provider="stub",
            model="test-model",
            metadata={"call": self.chat_calls},
        )

    def analyze_code(self, code, language=None):
        self.analysis_calls += 1
        return AIResponse(
            content=f"analysis:{language}:{code}",
            confidence=0.8,
            provider="stub",
            model="analysis-model",
            metadata={"call": self.analysis_calls},
        )


def test_aicore_defaults_when_config_missing(tmp_path):
    core = AICore(config_path=str(tmp_path / "missing-ai-config.yaml"))

    assert core.is_enabled() is False
    assert core.get_provider() is None


def test_get_provider_falls_back_to_available_provider(tmp_path):
    core = AICore(config_path=str(tmp_path / "missing-ai-config.yaml"))
    core.config = {"ai": {"enabled": True, "default_provider": "primary"}}
    core.providers = {
        "primary": StubProvider(available=False),
        "secondary": StubProvider(available=True),
    }

    provider = core.get_provider()
    assert provider is core.providers["secondary"]


def test_chat_completion_uses_cache(tmp_path):
    core = AICore(config_path=str(tmp_path / "missing-ai-config.yaml"))
    core.config = {
        "ai": {
            "enabled": True,
            "default_provider": "stub",
            "analytics": {"enabled": False},
        }
    }
    core.providers = {"stub": StubProvider()}
    core.cache = AICache(str(tmp_path / "ai_cache.db"), ttl_hours=1)

    messages = [{"role": "user", "content": "hello"}]
    first = core.chat_completion(messages, provider_name="stub")
    second = core.chat_completion(messages, provider_name="stub")

    assert first is not None
    assert second is not None
    assert second.cached is True
    assert core.providers["stub"].chat_calls == 1


def test_chat_completion_returns_none_on_provider_failure(tmp_path):
    core = AICore(config_path=str(tmp_path / "missing-ai-config.yaml"))
    core.config = {
        "ai": {
            "enabled": True,
            "default_provider": "stub",
            "analytics": {"enabled": False},
        }
    }
    core.providers = {"stub": StubProvider(should_fail=True)}
    core.cache = None

    result = core.chat_completion([{"role": "user", "content": "fail"}])
    assert result is None


def test_analyze_code_uses_provider(tmp_path):
    core = AICore(config_path=str(tmp_path / "missing-ai-config.yaml"))
    core.config = {
        "ai": {
            "enabled": True,
            "default_provider": "stub",
            "analytics": {"enabled": False},
        }
    }
    provider = StubProvider()
    core.providers = {"stub": provider}

    response = core.analyze_code("print('hello')", language="python")

    assert response is not None
    assert response.content.startswith("analysis:python")
    assert provider.analysis_calls == 1


def test_aicache_respects_ttl():
    with tempfile.TemporaryDirectory() as temp_dir:
        cache = AICache(f"{temp_dir}/cache.db", ttl_hours=0)
        key = "k"
        response = AIResponse(
            content="value",
            confidence=0.7,
            provider="stub",
            model="m",
            metadata={},
        )
        cache.set(key, response)

        assert cache.get(key) is None

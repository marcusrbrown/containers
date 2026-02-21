"""
AI Core Infrastructure for Container Template System

This module provides the foundational AI capabilities including:
- Multi-provider AI integration (Ollama, OpenAI, Anthropic)
- Configuration management
- Caching and performance optimization
- Error handling and fallback mechanisms
"""

import hashlib
import json
import logging
import os
import sqlite3
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class AIResponse:
    """Standardized AI response format"""

    content: str
    confidence: float
    provider: str
    model: str
    metadata: Dict[str, Any]
    cached: bool = False


@dataclass
class TemplateRecommendation:
    """Template recommendation with metadata"""

    template_name: str
    confidence: float
    reasoning: str
    parameters: Dict[str, Any]
    alternatives: List[str]


class AIProviderInterface(ABC):
    """Abstract interface for AI providers"""

    @abstractmethod
    def chat_completion(
        self, messages: List[Dict], model: Optional[str] = None
    ) -> AIResponse:
        """Generate chat completion"""
        pass

    @abstractmethod
    def analyze_code(self, code: str, language: Optional[str] = None) -> AIResponse:
        """Analyze code for issues and improvements"""
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if provider is available"""
        pass


class OllamaProvider(AIProviderInterface):
    """Ollama local AI provider"""

    def __init__(self, config: Dict[str, Any]):
        self.base_url = config.get("base_url", "http://localhost:11434")
        self.models = config.get("models", {})
        self.timeout = config.get("timeout", 30)

    def chat_completion(
        self, messages: List[Dict], model: Optional[str] = None
    ) -> AIResponse:
        """Generate chat completion using Ollama"""
        model = model or self.models.get("chat", "llama3.2")

        try:
            # Convert messages to Ollama format
            prompt = self._format_messages(messages)

            response = requests.post(
                f"{self.base_url}/api/generate",
                json={"model": model, "prompt": prompt, "stream": False},
                timeout=self.timeout,
            )
            response.raise_for_status()

            result = response.json()
            return AIResponse(
                content=result.get("response", ""),
                confidence=0.8,  # Ollama doesn't provide confidence scores
                provider="ollama",
                model=model,
                metadata={"tokens": len(result.get("response", "").split())},
            )

        except Exception as e:
            logger.error(f"Ollama API error: {e}")
            raise

    def analyze_code(self, code: str, language: str = None) -> AIResponse:
        """Analyze code using Ollama"""
        model = self.models.get("code", "codellama")

        messages = [
            {
                "role": "user",
                "content": f"Analyze this {language or 'code'} for security issues, performance problems, and best practice violations. Provide specific suggestions:\n\n{code}",
            }
        ]

        return self.chat_completion(messages, model)

    def is_available(self) -> bool:
        """Check if Ollama is running"""
        try:
            response = requests.get(f"{self.base_url}/api/tags", timeout=5)
            return response.status_code == 200
        except Exception:
            return False

    def _format_messages(self, messages: List[Dict]) -> str:
        """Convert chat messages to Ollama prompt format"""
        prompt = ""
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "system":
                prompt += f"System: {content}\n"
            elif role == "user":
                prompt += f"User: {content}\n"
            elif role == "assistant":
                prompt += f"Assistant: {content}\n"
        return prompt


class OpenAIProvider(AIProviderInterface):
    """OpenAI API provider"""

    def __init__(self, config: Dict[str, Any]):
        self.api_key = os.getenv(config.get("api_key_env", "OPENAI_API_KEY"))
        self.models = config.get("models", {})
        self.timeout = config.get("timeout", 30)
        self.max_tokens = config.get("max_tokens", 4000)

        if not self.api_key:
            logger.warning("OpenAI API key not found")

    def chat_completion(self, messages: List[Dict], model: str = None) -> AIResponse:
        """Generate chat completion using OpenAI"""
        if not self.api_key:
            raise ValueError("OpenAI API key not configured")

        model = model or self.models.get("chat", "gpt-4")

        try:
            import openai

            client = openai.OpenAI(api_key=self.api_key)

            response = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=self.max_tokens,
                timeout=self.timeout,
            )

            return AIResponse(
                content=response.choices[0].message.content,
                confidence=0.9,  # OpenAI generally high quality
                provider="openai",
                model=model,
                metadata={
                    "tokens": response.usage.total_tokens,
                    "prompt_tokens": response.usage.prompt_tokens,
                    "completion_tokens": response.usage.completion_tokens,
                },
            )

        except Exception as e:
            logger.error(f"OpenAI API error: {e}")
            raise

    def analyze_code(self, code: str, language: str = None) -> AIResponse:
        """Analyze code using OpenAI"""
        model = self.models.get("code", "gpt-4")

        messages = [
            {
                "role": "system",
                "content": "You are a expert code reviewer specializing in security, performance, and best practices.",
            },
            {
                "role": "user",
                "content": f"Analyze this {language or 'code'} for issues and provide specific improvement suggestions:\n\n{code}",
            },
        ]

        return self.chat_completion(messages, model)

    def is_available(self) -> bool:
        """Check if OpenAI API is available"""
        return bool(self.api_key)


class AnthropicProvider(AIProviderInterface):
    """Anthropic Claude API provider"""

    def __init__(self, config: Dict[str, Any]):
        self.api_key = os.getenv(config.get("api_key_env", "ANTHROPIC_API_KEY"))
        self.models = config.get("models", {})
        self.timeout = config.get("timeout", 30)
        self.max_tokens = config.get("max_tokens", 4000)

        if not self.api_key:
            logger.warning("Anthropic API key not found")

    def chat_completion(self, messages: List[Dict], model: str = None) -> AIResponse:
        """Generate chat completion using Anthropic"""
        if not self.api_key:
            raise ValueError("Anthropic API key not configured")

        model = model or self.models.get("chat", "claude-3-sonnet-20240229")

        try:
            import anthropic

            client = anthropic.Anthropic(api_key=self.api_key)

            # Convert messages to Anthropic format
            system_message = ""
            user_messages = []

            for msg in messages:
                if msg.get("role") == "system":
                    system_message = msg.get("content", "")
                else:
                    user_messages.append(msg)

            response = client.messages.create(
                model=model,
                max_tokens=self.max_tokens,
                system=system_message,
                messages=user_messages,
            )

            return AIResponse(
                content=response.content[0].text,
                confidence=0.9,  # Claude generally high quality
                provider="anthropic",
                model=model,
                metadata={
                    "tokens": response.usage.input_tokens
                    + response.usage.output_tokens,
                    "input_tokens": response.usage.input_tokens,
                    "output_tokens": response.usage.output_tokens,
                },
            )

        except Exception as e:
            logger.error(f"Anthropic API error: {e}")
            raise

    def analyze_code(self, code: str, language: str = None) -> AIResponse:
        """Analyze code using Anthropic"""
        model = self.models.get("code", "claude-3-sonnet-20240229")

        messages = [
            {
                "role": "user",
                "content": f"As an expert code reviewer, analyze this {language or 'code'} for security vulnerabilities, performance issues, and best practice violations. Provide specific, actionable suggestions:\n\n{code}",
            }
        ]

        return self.chat_completion(messages, model)

    def is_available(self) -> bool:
        """Check if Anthropic API is available"""
        return bool(self.api_key)


class AICache:
    """Simple SQLite-based caching for AI responses"""

    def __init__(self, database_path: str, ttl_hours: int = 24):
        self.database_path = database_path
        self.ttl_seconds = ttl_hours * 3600
        self._init_database()

    def _init_database(self):
        """Initialize cache database"""
        conn = sqlite3.connect(self.database_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ai_cache (
                key TEXT PRIMARY KEY,
                content TEXT,
                confidence REAL,
                provider TEXT,
                model TEXT,
                metadata TEXT,
                created_at INTEGER
            )
        """)
        conn.commit()
        conn.close()

    def get(self, key: str) -> Optional[AIResponse]:
        """Get cached response"""
        conn = sqlite3.connect(self.database_path)
        cursor = conn.execute(
            "SELECT content, confidence, provider, model, metadata, created_at FROM ai_cache WHERE key = ?",
            (key,),
        )
        row = cursor.fetchone()
        conn.close()

        if row:
            content, confidence, provider, model, metadata_json, created_at = row

            # Check if cache entry is still valid
            if time.time() - created_at < self.ttl_seconds:
                metadata = json.loads(metadata_json) if metadata_json else {}
                return AIResponse(
                    content=content,
                    confidence=confidence,
                    provider=provider,
                    model=model,
                    metadata=metadata,
                    cached=True,
                )

        return None

    def set(self, key: str, response: AIResponse):
        """Cache AI response"""
        conn = sqlite3.connect(self.database_path)
        conn.execute(
            """
            INSERT OR REPLACE INTO ai_cache
            (key, content, confidence, provider, model, metadata, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
            (
                key,
                response.content,
                response.confidence,
                response.provider,
                response.model,
                json.dumps(response.metadata),
                int(time.time()),
            ),
        )
        conn.commit()
        conn.close()

    def clear_expired(self):
        """Remove expired cache entries"""
        cutoff_time = int(time.time()) - self.ttl_seconds
        conn = sqlite3.connect(self.database_path)
        conn.execute("DELETE FROM ai_cache WHERE created_at < ?", (cutoff_time,))
        conn.commit()
        conn.close()


class AICore:
    """Central AI coordination and management"""

    def __init__(self, config_path: str = "ai_config.yaml"):
        self.config_path = config_path
        self.config = self._load_config()
        self.providers = self._init_providers()
        self.cache = self._init_cache()
        self.analytics_db = self._init_analytics()

    def _load_config(self) -> Dict[str, Any]:
        """Load AI configuration"""
        try:
            with open(self.config_path, "r") as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            logger.warning(
                f"AI config file {self.config_path} not found, using defaults"
            )
            return {"ai": {"enabled": False}}

    def _init_providers(self) -> Dict[str, AIProviderInterface]:
        """Initialize AI providers"""
        providers = {}

        if not self.config.get("ai", {}).get("enabled", False):
            return providers

        provider_configs = self.config.get("ai", {}).get("providers", {})

        # Initialize Ollama
        if provider_configs.get("ollama", {}).get("enabled", False):
            try:
                providers["ollama"] = OllamaProvider(provider_configs["ollama"])
                logger.info("Initialized Ollama provider")
            except Exception as e:
                logger.error(f"Failed to initialize Ollama: {e}")

        # Initialize OpenAI
        if provider_configs.get("openai", {}).get("enabled", False):
            try:
                providers["openai"] = OpenAIProvider(provider_configs["openai"])
                logger.info("Initialized OpenAI provider")
            except Exception as e:
                logger.error(f"Failed to initialize OpenAI: {e}")

        # Initialize Anthropic
        if provider_configs.get("anthropic", {}).get("enabled", False):
            try:
                providers["anthropic"] = AnthropicProvider(
                    provider_configs["anthropic"]
                )
                logger.info("Initialized Anthropic provider")
            except Exception as e:
                logger.error(f"Failed to initialize Anthropic: {e}")

        return providers

    def _init_cache(self) -> Optional[AICache]:
        """Initialize AI response cache"""
        cache_config = self.config.get("ai", {}).get("cache", {})
        if cache_config.get("enabled", True):
            ttl_hours = cache_config.get("ttl_hours", 24)
            return AICache("ai_cache.db", ttl_hours)
        return None

    def _init_analytics(self) -> str:
        """Initialize analytics database"""
        analytics_config = self.config.get("ai", {}).get("analytics", {})
        database_path = analytics_config.get("database_path", "template_analytics.db")

        if analytics_config.get("enabled", True):
            conn = sqlite3.connect(database_path)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS template_usage (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    template_name TEXT,
                    action TEXT,
                    success BOOLEAN,
                    parameters TEXT,
                    duration_seconds REAL,
                    ai_provider TEXT,
                    timestamp INTEGER
                )
            """)
            conn.commit()
            conn.close()

        return database_path

    def get_provider(self, provider_name: str = None) -> Optional[AIProviderInterface]:
        """Get AI provider by name or default"""
        if not self.config.get("ai", {}).get("enabled", False):
            return None

        if provider_name is None:
            provider_name = self.config.get("ai", {}).get("default_provider", "ollama")

        provider = self.providers.get(provider_name)
        if provider and provider.is_available():
            return provider

        # Fallback to any available provider
        for name, provider in self.providers.items():
            if provider.is_available():
                logger.info(f"Falling back to {name} provider")
                return provider

        logger.warning("No AI providers available")
        return None

    def generate_cache_key(self, operation: str, **kwargs) -> str:
        """Generate cache key for operation"""
        key_data = f"{operation}:{json.dumps(kwargs, sort_keys=True)}"
        return hashlib.md5(key_data.encode()).hexdigest()

    def chat_completion(
        self, messages: List[Dict], provider_name: str = None, use_cache: bool = True
    ) -> Optional[AIResponse]:
        """Generate chat completion with caching"""
        provider = self.get_provider(provider_name)
        if not provider:
            return None

        # Check cache
        if use_cache and self.cache:
            cache_key = self.generate_cache_key(
                "chat", messages=messages, provider=provider_name
            )
            cached_response = self.cache.get(cache_key)
            if cached_response:
                return cached_response

        # Generate response
        start_time = time.time()
        try:
            response = provider.chat_completion(messages)

            # Cache response
            if use_cache and self.cache:
                self.cache.set(cache_key, response)

            # Log analytics
            self._log_usage(
                "chat_completion", True, time.time() - start_time, provider_name
            )

            return response

        except Exception as e:
            self._log_usage(
                "chat_completion", False, time.time() - start_time, provider_name
            )
            logger.error(f"Chat completion failed: {e}")
            return None

    def analyze_code(
        self, code: str, language: str = None, provider_name: str = None
    ) -> Optional[AIResponse]:
        """Analyze code with AI"""
        provider = self.get_provider(provider_name)
        if not provider:
            return None

        start_time = time.time()
        try:
            response = provider.analyze_code(code, language)
            self._log_usage(
                "code_analysis", True, time.time() - start_time, provider_name
            )
            return response
        except Exception as e:
            self._log_usage(
                "code_analysis", False, time.time() - start_time, provider_name
            )
            logger.error(f"Code analysis failed: {e}")
            return None

    def is_enabled(self, feature: str = None) -> bool:
        """Check if AI or specific feature is enabled"""
        if not self.config.get("ai", {}).get("enabled", False):
            return False

        if feature:
            return (
                self.config.get("ai", {})
                .get("features", {})
                .get(feature, {})
                .get("enabled", False)
            )

        return True

    def _log_usage(
        self,
        action: str,
        success: bool,
        duration: float,
        provider: str,
        template_name: str = None,
        parameters: Dict = None,
    ):
        """Log usage analytics"""
        analytics_config = self.config.get("ai", {}).get("analytics", {})
        if not analytics_config.get("enabled", True):
            return

        try:
            conn = sqlite3.connect(self.analytics_db)
            conn.execute(
                """
                INSERT INTO template_usage
                (template_name, action, success, parameters, duration_seconds, ai_provider, timestamp)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    template_name,
                    action,
                    success,
                    json.dumps(parameters) if parameters else None,
                    duration,
                    provider,
                    int(time.time()),
                ),
            )
            conn.commit()
            conn.close()
        except Exception as e:
            logger.error(f"Failed to log analytics: {e}")


# Global AI core instance
_ai_core = None


def get_ai_core() -> AICore:
    """Get or create global AI core instance"""
    global _ai_core
    if _ai_core is None:
        _ai_core = AICore()
    return _ai_core


def is_ai_enabled(feature: str = None) -> bool:
    """Check if AI is enabled globally"""
    return get_ai_core().is_enabled(feature)

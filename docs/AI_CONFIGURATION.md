# AI Feature Configuration

This project’s AI functionality reads settings from `ai_config.yaml`.

## Quick Start

1. Create a config file:

   ```bash
   poetry run containers ai config --init
   ```

2. Edit `ai_config.yaml` and enable one provider.
3. Export required API key environment variables when using hosted providers.
4. Validate your configuration:

   ```bash
   poetry run containers ai config --validate
   ```

## Configuration File

An example file is included at `ai_config.example.yaml`.

Supported top-level keys:

- `ai.enabled`: Master toggle for AI features
- `ai.default_provider`: `ollama`, `openai`, or `anthropic`
- `ai.providers.*`: Provider-specific settings
- `ai.cache.enabled`: Enable SQLite response cache (`ai_cache.db`)
- `ai.cache.ttl_hours`: Cache TTL in hours
- `ai.analytics.enabled`: Enable usage analytics storage
- `ai.analytics.database_path`: Analytics DB path
- `ai.features.*.enabled`: Per-feature toggle

## Provider Setup

### Ollama (Local)

- Set `ai.providers.ollama.enabled: true`
- Ensure Ollama is running at `ai.providers.ollama.base_url` (default `http://localhost:11434`)
- Choose local models for `chat` and `code`

### OpenAI

- Set `ai.providers.openai.enabled: true`
- Set `ai.providers.openai.api_key_env` (default `OPENAI_API_KEY`)
- Export the environment variable before running commands:

  ```bash
  export OPENAI_API_KEY="your-api-key"
  ```

### Anthropic

- Set `ai.providers.anthropic.enabled: true`
- Set `ai.providers.anthropic.api_key_env` (default `ANTHROPIC_API_KEY`)
- Export the environment variable before running commands:

  ```bash
  export ANTHROPIC_API_KEY="your-api-key"
  ```

## CLI Configuration Commands

- Initialize config:

  ```bash
  poetry run containers ai config --init
  ```

- Force overwrite existing config:

  ```bash
  poetry run containers ai config --init --force
  ```

- Validate config:

  ```bash
  poetry run containers ai config --validate
  ```

- Use an alternate path:

  ```bash
  poetry run containers ai config --validate --path ./config/ai_config.yaml
  ```

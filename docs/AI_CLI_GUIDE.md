# AI-Enhanced Container Template System Guide

## Overview

The Container Template System now includes comprehensive AI-powered capabilities that enhance template selection, project analysis, and maintenance through intelligent automation.

## 🚀 Quick Start

```bash
# Install and setup
poetry install
poetry run containers ai --help

# Get AI template recommendations
poetry run containers ai recommend /path/to/your/project

# Analyze project structure
poetry run containers ai analyze /path/to/your/project --output analysis.md

# Interactive AI assistant
poetry run containers ai chat

# Infer template parameters
poetry run containers ai infer apps/nodejs/express /path/to/your/project

# Generate AI documentation
poetry run containers ai docs --template base/alpine --type readme
```

## 🧠 AI Features

### 1. Intelligent Template Recommendation

```bash
poetry run containers ai recommend <project_path> [--format text|json] [--limit N]
```

**What it does:**

- Analyzes your project structure
- Identifies languages, frameworks, and dependencies
- Recommends the most suitable container templates
- Provides confidence scores and reasoning

**Example:**

```bash
poetry run containers ai recommend ./my-node-app --format text --limit 3
```

### 2. Project Structure Analysis

```bash
poetry run containers ai analyze <project_path> [--output file]
```

**What it does:**

- Deep analysis of project files and structure
- Detects languages, frameworks, and dependencies
- Identifies configuration patterns
- Provides architectural insights

**Example:**

```bash
poetry run containers ai analyze ./my-app --output project_analysis.md
```

### 3. Interactive AI Assistant

```bash
poetry run containers ai chat [--template template_path]
```

**What it does:**

- Interactive chat interface for template questions
- Context-aware responses about containerization
- Template-specific guidance and best practices
- Natural language template queries

**Example Usage:**

```
You: How do I containerize a FastAPI app?
AI: I can help you with that! FastAPI works great with Python containers...

You: What about security considerations?
AI: For FastAPI containers, consider these security practices...
```

### 4. Smart Parameter Inference

```bash
poetry run containers ai infer <template> <project_path>
```

**What it does:**

- Automatically detects template parameters from your project
- Infers values like app names, ports, dependencies
- Generates parameter files for template generation
- Provides confidence scores for each inference

**Example:**

```bash
poetry run containers ai infer apps/python/fastapi ./my-fastapi-app
```

### 5. AI Code Review

```bash
poetry run containers ai review <path> [--template template_context]
```

**What it does:**

- AI-powered code review for containerization
- Identifies potential issues and optimizations
- Provides security and performance suggestions
- Template-specific best practice recommendations

### 6. AI Documentation Generation

```bash
poetry run containers ai docs --template <template> --type <readme|api|troubleshooting> [--output file]
```

**What it does:**

- Generates intelligent documentation using AI
- Creates README files, API docs, and troubleshooting guides
- Template-specific content and examples
- Maintains consistency across documentation

**Example:**

```bash
poetry run containers ai docs --template apps/nodejs/express --type readme --output README.md
```

### 7. Predictive Maintenance

```bash
poetry run containers ai maintenance [--template template] [--report]
```

**What it does:**

- Analyzes template health and usage patterns
- Predicts maintenance needs and potential issues
- Provides system-wide health reports
- Identifies optimization opportunities

## 🛠 Configuration

### AI Provider Setup

The system supports multiple AI providers. Configure in `ai_config.yaml`:

```yaml
ai:
  enabled: true
  default_provider: "ollama" # or 'openai', 'anthropic'

  providers:
    ollama:
      enabled: true
      base_url: "http://localhost:11434"
      models:
        chat: "llama3.2"
        code: "codellama"
        analysis: "mistral"

    openai:
      enabled: false
      api_key_env: "OPENAI_API_KEY"
      models:
        chat: "gpt-4"
        code: "gpt-4"
        analysis: "gpt-3.5-turbo"

    anthropic:
      enabled: false
      api_key_env: "ANTHROPIC_API_KEY"
      models:
        chat: "claude-3-sonnet-20240229"
        code: "claude-3-sonnet-20240229"
        analysis: "claude-3-haiku-20240307"
```

### Feature Configuration

Enable/disable specific AI features:

```yaml
ai:
  features:
    template_recommendation:
      enabled: true
      confidence_threshold: 0.7
      max_suggestions: 5

    parameter_inference:
      enabled: true
      auto_confidence_threshold: 0.8

    code_analysis:
      enabled: true
      security_scanning: true
      performance_analysis: true

    documentation_generation:
      enabled: true
      auto_examples: true

    predictive_maintenance:
      enabled: true
      alert_threshold: 0.6

    chat_interface:
      enabled: true
      session_timeout: 3600
      max_context_length: 4000
```

## 🔧 Current Status & Limitations

### ✅ Working Features

- AI CLI command structure is fully functional
- Multi-provider AI integration (Ollama, OpenAI, Anthropic)
- Configuration management
- Error handling and graceful degradation
- Import system resolved for both module and direct execution

### ⚠️ Known Issues

1. **Template Recommendations**: Currently returns generic results; needs enhanced project analysis logic
2. **Project Analysis**: Basic implementation; requires more sophisticated file parsing
3. **Maintenance Database**: SQLite schema needs initialization for analytics
4. **AI Model Integration**: Placeholder responses in some areas pending full AI integration

### 🔨 Troubleshooting

#### AI Features Not Available

```bash
⚠️  AI features unavailable: [error message]
```

**Solutions:**

1. Check AI provider configuration in `ai_config.yaml`
2. Ensure Ollama is running: `ollama serve`
3. Verify API keys for OpenAI/Anthropic if using those providers
4. Check network connectivity

#### Import Errors

```bash
ImportError: attempted relative import with no known parent package
```

**Solution:**
Always use Poetry to run commands:

```bash
poetry run containers ai <command>
```

#### Database Errors

```bash
no such column: error_message
```

**Solution:** Initialize the analytics database:

```bash
# This will be implemented in a future update
poetry run containers ai maintenance --init-db
```

## 📚 Development Guide

### Adding New AI Features

1. **Create the AI module** in `scripts/`
2. **Add CLI command** to `containers_cli.py`
3. **Update configuration** in `ai_config.yaml`
4. **Add tests** and documentation

### Example: Adding a new AI command

```python
# In containers_cli.py
async def cmd_ai_optimize(self, args) -> int:
    """AI-powered optimization suggestions."""
    print(f"🔍 Analyzing {args.path} for optimizations...")

    suggestions = await self.ai_core.get_optimization_suggestions(args.path)

    for suggestion in suggestions:
        print(f"💡 {suggestion['title']}")
        print(f"   {suggestion['description']}")

    return 0
```

### Testing AI Commands

```bash
# Test individual commands
poetry run containers ai recommend --help
poetry run containers ai analyze ./test-project
poetry run containers ai chat

# Run with different providers
OLLAMA_HOST=localhost:11434 poetry run containers ai recommend ./project
```

## 🎯 Future Enhancements

### Priority Improvements

1. **Enhanced Project Analysis**: Better language/framework detection
2. **Real AI Integration**: Connect to actual AI models for intelligent responses
3. **Database Schema**: Complete the analytics database setup
4. **Template Learning**: Machine learning from usage patterns
5. **Multi-modal Analysis**: Support for analyzing Dockerfiles, docker-compose files

### Advanced Features

1. **Continuous Learning**: AI improves recommendations based on user feedback
2. **Template Generation**: AI creates new templates from scratch
3. **Security Analysis**: Automated vulnerability scanning
4. **Performance Optimization**: AI-powered container optimization
5. **Cloud-specific Recommendations**: Provider-specific optimizations

## 📖 API Reference

### Core Classes

#### AICore

```python
class AICore:
    def __init__(self, config_path: str = "ai_config.yaml")
    async def chat(self, message: str, context: str = None) -> AIResponse
    async def analyze_code(self, code: str, language: str) -> AIResponse
    def is_enabled(self, feature: str) -> bool
```

#### TemplateIntelligence

```python
class TemplateIntelligence:
    def analyze_project(self, path: str) -> ProjectAnalysis
    def recommend_templates(self, path: str) -> List[TemplateRecommendation]
    def infer_parameters(self, template: str, project: str) -> Dict[str, Any]
```

#### PredictiveMaintenance

```python
class PredictiveMaintenance:
    def analyze_template(self, template: str) -> List[MaintenanceAlert]
    def generate_maintenance_report(self) -> Dict[str, Any]
    def log_usage(self, template: str, **metadata)
```

## 🤝 Contributing

To contribute to the AI features:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/ai-enhancement`
3. **Make your changes** following the existing patterns
4. **Add tests** for new functionality
5. **Update documentation**
6. **Submit a pull request**

### Code Style

- Follow existing patterns in AI modules
- Use type hints consistently
- Add comprehensive docstrings
- Handle errors gracefully with fallbacks

## 📝 License

This AI enhancement system is part of the Container Template project and follows the same MIT license.

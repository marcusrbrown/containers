# Template Engine API Documentation

Complete API reference for the Container Template Engine.

## Command Line Interface

### template-engine

Main command for template operations.

```bash
poetry run template-engine <command> [options]
```

#### Commands

##### list

List available templates.

```bash
poetry run template-engine list [--category CATEGORY] [--format FORMAT]
```

**Options:**
- `--category`: Filter by category (app, database, infrastructure, microservice, base)
- `--format`: Output format (table, json)

**Examples:**
```bash
# List all templates
poetry run template-engine list

# List only app templates
poetry run template-engine list --category app

# JSON output
poetry run template-engine list --format json
```

##### generate

Generate a container from a template.

```bash
poetry run template-engine generate TEMPLATE OUTPUT [options]
```

**Arguments:**
- `TEMPLATE`: Template path (e.g., apps/nodejs/express)
- `OUTPUT`: Output directory

**Options:**
- `--params FILE`: Parameters JSON file
- `--param KEY=VALUE`: Individual parameter (can be used multiple times)
- `--dry-run`: Show what would be generated without writing files

**Examples:**
```bash
# Basic generation
poetry run template-engine generate apps/nodejs/express ./my-app

# With parameters
poetry run template-engine generate apps/nodejs/express ./my-app \
  --param app_name=my-api \
  --param port=8080

# Using parameter file
poetry run template-engine generate apps/nodejs/express ./my-app \
  --params config.json

# Dry run
poetry run template-engine generate apps/nodejs/express ./my-app --dry-run
```

##### validate

Validate a template.

```bash
poetry run template-engine validate TEMPLATE
```

**Arguments:**
- `TEMPLATE`: Template path

**Examples:**
```bash
poetry run template-engine validate apps/nodejs/express
```

##### test

Test a template by building and running it.

```bash
poetry run template-engine test TEMPLATE [--params FILE]
```

**Arguments:**
- `TEMPLATE`: Template path

**Options:**
- `--params FILE`: Parameters JSON file for testing

**Examples:**
```bash
poetry run template-engine test apps/nodejs/express
poetry run template-engine test apps/nodejs/express --params test-config.json
```

### template-testing

Advanced testing framework for templates.

```bash
poetry run template-testing TEMPLATE [options]
```

**Arguments:**
- `TEMPLATE`: Template path

**Options:**
- `--params FILE`: Parameters JSON file
- `--integration`: Include integration tests
- `--performance`: Include performance tests
- `--output FILE`: Output report file
- `--format FORMAT`: Output format (text, json)

**Examples:**
```bash
# Basic testing
poetry run template-testing apps/nodejs/express

# Comprehensive testing
poetry run template-testing apps/nodejs/express \
  --integration \
  --performance \
  --output report.md

# JSON report
poetry run template-testing apps/nodejs/express \
  --format json \
  --output report.json
```

### generate-docs

Generate documentation for all templates.

```bash
poetry run generate-docs [options]
```

**Options:**
- `--output DIR`: Output directory (default: docs/templates)
- `--template PATH`: Generate docs for specific template only

**Examples:**
```bash
# Generate all documentation
poetry run generate-docs

# Generate for specific template
poetry run generate-docs --template apps/nodejs/express
```

## Python API

### TemplateEngine Class

Core template processing engine.

```python
from scripts.template_engine import TemplateEngine

# Initialize
engine = TemplateEngine("templates")

# List templates
templates = engine.list_templates()
templates_by_category = engine.list_templates(category="app")

# Load template metadata
metadata = engine.load_template_metadata("apps/nodejs/express")

# Resolve inheritance
resolved_metadata = engine.resolve_inheritance("apps/nodejs/express")

# Generate template
generated_files = engine.generate_template(
    template_path="apps/nodejs/express",
    output_dir="./output",
    parameters={"app_name": "my-app", "port": 3000},
    dry_run=False
)

# Validate template
validation_results = engine.validate_template("apps/nodejs/express")

# Test template
test_results = engine.test_template("apps/nodejs/express", {"app_name": "test"})
```

#### Methods

##### `__init__(templates_dir: str = "templates")`

Initialize the template engine.

**Parameters:**
- `templates_dir`: Path to templates directory

##### `list_templates(category: Optional[str] = None) -> List[Dict[str, Any]]`

List available templates.

**Parameters:**
- `category`: Optional category filter

**Returns:**
- List of template information dictionaries

##### `load_template_metadata(template_path: str) -> Dict[str, Any]`

Load template metadata from template.yaml.

**Parameters:**
- `template_path`: Path to template

**Returns:**
- Template metadata dictionary

**Raises:**
- `FileNotFoundError`: If template.yaml not found
- `ValidationError`: If metadata is invalid

##### `resolve_inheritance(template_path: str) -> Dict[str, Any]`

Resolve template inheritance chain.

**Parameters:**
- `template_path`: Path to template

**Returns:**
- Merged metadata with inheritance resolved

##### `generate_template(template_path: str, output_dir: str, parameters: Optional[Dict[str, Any]] = None, dry_run: bool = False) -> Dict[str, str]`

Generate files from template.

**Parameters:**
- `template_path`: Path to template
- `output_dir`: Output directory
- `parameters`: Template parameters
- `dry_run`: If True, don't write files

**Returns:**
- Dictionary mapping file paths to content

**Raises:**
- `TemplateError`: If template rendering fails
- `ValueError`: If required parameters missing

##### `validate_template(template_path: str) -> Dict[str, Any]`

Validate template structure and syntax.

**Parameters:**
- `template_path`: Path to template

**Returns:**
- Validation results dictionary

##### `test_template(template_path: str, test_params: Optional[Dict] = None) -> Dict[str, Any]`

Test template by generating and building.

**Parameters:**
- `template_path`: Path to template
- `test_params`: Test parameters

**Returns:**
- Test results dictionary

### TemplateTestFramework Class

Advanced testing framework for templates.

```python
from scripts.template_testing import TemplateTestFramework
import asyncio

# Initialize
framework = TemplateTestFramework("templates")

# Run comprehensive tests
async def test_template():
    test_suite = await framework.run_template_tests(
        "apps/nodejs/express",
        test_params={"app_name": "test"},
        include_integration=True,
        include_performance=True
    )

    # Generate report
    report = framework.generate_test_report(test_suite, "report.md")
    print(f"Tests: {test_suite.passed}/{test_suite.total_tests} passed")

# Run tests
asyncio.run(test_template())
```

### DocumentationGenerator Class

Automatic documentation generation.

```python
from scripts.template_documentation import DocumentationGenerator

# Initialize
doc_gen = DocumentationGenerator("templates", "docs/templates")

# Generate all documentation
generated_docs = doc_gen.generate_all_documentation()

# Generate specific template docs
doc_path = doc_gen.generate_template_documentation("apps/nodejs/express")
```

## Template Schema

### template.yaml Structure

```yaml
# Required fields
name: "template-name"
version: "1.0.0"
description: "Template description"
category: "app"  # app, database, infrastructure, microservice, base

# Optional fields
author: "Author Name"
license: "MIT"
tags: ["tag1", "tag2"]
inherits: "base/alpine"  # Template inheritance

# Parameters definition
parameters:
  param_name:
    type: "string"  # string, integer, boolean, array, object
    description: "Parameter description"
    default: "default_value"
    required: true
    enum: ["option1", "option2"]  # For string types
    pattern: "^[a-z]+$"  # Regex pattern for strings
    min: 1  # For numeric types
    max: 100  # For numeric types

# Files to generate
files:
  dockerfile: "Dockerfile"
  compose: "docker-compose.yml"
  config: ["config.yaml", "settings.json"]
  scripts: ["start.sh", "healthcheck.sh"]
  docs: ["README.md"]

# Dependencies
dependencies:
  build: ["nodejs", "npm"]
  runtime: ["nodejs"]
  test: ["docker", "curl"]

# Testing configuration
testing:
  build_args:
    ARG_NAME: "value"
  env_vars:
    ENV_VAR: "value"
  health_check: "curl -f http://localhost:3000/health || exit 1"
  test_commands:
    - "docker run --rm test-image npm test"
  integration_tests:
    - "pytest tests/"

# Platform support
platforms: ["linux/amd64", "linux/arm64"]

# Registry configuration
registry:
  namespace: "myorg"
  repository: "template-name"
  tags: ["latest", "1.0.0"]
```

### Parameter Types

#### string
```yaml
param_name:
  type: "string"
  description: "String parameter"
  default: "default"
  pattern: "^[a-z]+$"  # Optional regex validation
  enum: ["option1", "option2"]  # Optional allowed values
```

#### integer
```yaml
param_name:
  type: "integer"
  description: "Integer parameter"
  default: 42
  min: 1
  max: 100
```

#### boolean
```yaml
param_name:
  type: "boolean"
  description: "Boolean parameter"
  default: true
```

#### array
```yaml
param_name:
  type: "array"
  description: "Array parameter"
  default: ["item1", "item2"]
```

#### object
```yaml
param_name:
  type: "object"
  description: "Object parameter"
  default:
    key1: "value1"
    key2: "value2"
```

## Error Handling

### Common Errors

#### ValidationError
Template metadata validation failed.

```python
try:
    metadata = engine.load_template_metadata("invalid/template")
except ValidationError as e:
    print(f"Validation failed: {e}")
```

#### TemplateError
Template rendering failed.

```python
try:
    files = engine.generate_template("template", "output", params)
except TemplateError as e:
    print(f"Template error: {e}")
```

#### FileNotFoundError
Template or file not found.

```python
try:
    metadata = engine.load_template_metadata("nonexistent/template")
except FileNotFoundError as e:
    print(f"Template not found: {e}")
```

## Best Practices

### Template Development

1. **Use meaningful names**: Choose descriptive template and parameter names
2. **Provide defaults**: Include sensible defaults for all optional parameters
3. **Document thoroughly**: Add comprehensive descriptions for all parameters
4. **Test extensively**: Include validation, build, and runtime tests
5. **Follow security**: Use non-root users, minimal images, security scanning

### Parameter Design

1. **Type safety**: Use appropriate parameter types
2. **Validation**: Add pattern, enum, min/max constraints
3. **Backwards compatibility**: Don't break existing parameter interfaces
4. **Logical grouping**: Group related parameters together

### File Organization

1. **Consistent structure**: Follow the standard template directory layout
2. **Separation of concerns**: Keep configuration, scripts, and docs separate
3. **Template inheritance**: Use base templates for common functionality
4. **Version control**: Tag template versions appropriately

---

*API documentation for Container Template Engine*
*Generated automatically from source code*

# Container Template Documentation

Comprehensive documentation for all available container templates.

## Overview

This repository contains **7 templates** across **5 categories** to help you quickly bootstrap containerized applications and infrastructure.

## Quick Start

### Install Dependencies

```bash
# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -

# Install project dependencies
poetry install
```

### Generate Your First Container

```bash
# List available templates
poetry run template-engine list

# Generate a Node.js Express app
poetry run template-engine generate apps/nodejs/express ./my-app

# Build and run
cd my-app
docker-compose up -d
```

## Template Categories

### App Templates

_2 templates available_

- **[Python FastAPI](apps/python/fastapi/README.md)** - High-performance Python web API with FastAPI framework
- **[nodejs-express](apps/nodejs/express/README.md)** - Node.js Express web application template with TypeScript support

[📋 **Browse all app templates**](app/README.md)

### Base Templates

_1 templates available_

- **[alpine-base](base/alpine/README.md)** - Alpine Linux base template with security hardening and common utilities

[📋 **Browse all base templates**](base/README.md)

### Database Templates

_2 templates available_

- **[postgresql](databases/postgresql/README.md)** - PostgreSQL database server with security hardening and performance optimization
- **[redis-cache](databases/redis/README.md)** - Redis in-memory data store with persistence and security

[📋 **Browse all database templates**](database/README.md)

### Infrastructure Templates

_1 templates available_

- **[nginx-proxy](infrastructure/nginx/README.md)** - nginx reverse proxy with SSL termination and load balancing

[📋 **Browse all infrastructure templates**](infrastructure/README.md)

### Microservice Templates

_1 templates available_

- **[Go Microservice](microservices/go/README.md)** - High-performance Go microservice with gRPC and REST APIs

[📋 **Browse all microservice templates**](microservice/README.md)

## Template Library

| Name                                            | Category       | Description                                                                     | Version |
| ----------------------------------------------- | -------------- | ------------------------------------------------------------------------------- | ------- |
| [Python FastAPI](apps/python/fastapi/README.md) | app            | High-performance Python web API with FastAPI framework                          | 1.0.0   |
| [nodejs-express](apps/nodejs/express/README.md) | app            | Node.js Express web application template with TypeScript support                | 1.0.0   |
| [alpine-base](base/alpine/README.md)            | base           | Alpine Linux base template with security hardening and common utilities         | 1.0.0   |
| [postgresql](databases/postgresql/README.md)    | database       | PostgreSQL database server with security hardening and performance optimization | 1.0.0   |
| [redis-cache](databases/redis/README.md)        | database       | Redis in-memory data store with persistence and security                        | 1.0.0   |
| [nginx-proxy](infrastructure/nginx/README.md)   | infrastructure | nginx reverse proxy with SSL termination and load balancing                     | 1.0.0   |
| [Go Microservice](microservices/go/README.md)   | microservice   | High-performance Go microservice with gRPC and REST APIs                        | 1.0.0   |

## Using Templates

### Command Line Interface

```bash
# List all templates
poetry run template-engine list

# List templates by category
poetry run template-engine list --category app

# Generate template
poetry run template-engine generate <template-path> <output-dir>

# Generate with parameters
poetry run template-engine generate <template-path> <output-dir> \
  --param name=value \
  --param another=value

# Use parameter file
poetry run template-engine generate <template-path> <output-dir> \
  --params params.json

# Validate template
poetry run template-engine validate <template-path>

# Test template
poetry run template-engine test <template-path>
```

### Parameter Files

Create a `params.json` file for reusable configurations:

```json
{
  "app_name": "my-application",
  "version": "1.0.0",
  "environment": "production",
  "enable_ssl": true,
  "custom_settings": {
    "feature_flags": ["feature_a", "feature_b"]
  }
}
```

### CI/CD Integration

#### GitHub Actions

```yaml
name: Generate and Deploy
on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install Poetry
        run: curl -sSL https://install.python-poetry.org | python3 -

      - name: Install dependencies
        run: poetry install

      - name: Generate from template
        run: |
          poetry run template-engine generate apps/nodejs/express ./app \
            --params production-params.json

      - name: Build and deploy
        run: |
          cd app
          docker build -t my-app:latest .
          # Add deployment commands
```

## Development

### Creating New Templates

1. **Create template directory structure:**

   ```
   templates/category/name/
   ├── template.yaml      # Template metadata
   ├── Dockerfile         # Main Dockerfile template
   ├── docker-compose.yml # Compose template
   ├── config/            # Configuration files
   └── scripts/           # Utility scripts
   ```

2. **Define template.yaml:**

   ```yaml
   name: "my-template"
   version: "1.0.0"
   description: "Description of the template"
   category: "app" # app, database, infrastructure, microservice, base

   parameters:
     param_name:
       type: "string"
       description: "Parameter description"
       default: "default_value"
       required: true

   files:
     dockerfile: "Dockerfile"
     compose: "docker-compose.yml"
   ```

3. **Test your template:**

   ```bash
   poetry run template-engine validate category/name
   poetry run template-engine test category/name
   ```

4. **Generate documentation:**
   ```bash
   poetry run generate-docs
   ```

### Template Best Practices

- **Security First**: Always use non-root users, minimal base images
- **Parameterization**: Make templates flexible with sensible defaults
- **Documentation**: Include comprehensive parameter documentation
- **Testing**: Add health checks and test commands
- **Multi-platform**: Support common architectures (amd64, arm64)
- **Production Ready**: Include monitoring, logging, backup strategies

## API Reference

### Template Engine API

[📋 **Complete API Documentation**](API.md)

### Template Schema

Templates are defined using a structured YAML schema with the following components:

- **Metadata**: Name, version, description, category
- **Parameters**: Input parameters with types and validation
- **Files**: Template files to generate
- **Dependencies**: Required packages and tools
- **Testing**: Test configurations and commands
- **Platform Support**: Supported architectures

## Testing Framework

The template system includes comprehensive testing:

```bash
# Run all tests for a template
poetry run template-testing template-path

# Include integration tests
poetry run template-testing template-path --integration

# Include performance tests
poetry run template-testing template-path --performance

# Generate test report
poetry run template-testing template-path --output report.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add or modify templates
4. Test your changes
5. Generate documentation
6. Submit a pull request

### Guidelines

- Follow the existing template structure
- Include comprehensive documentation
- Add appropriate tests
- Use semantic versioning
- Follow security best practices

## License

MIT License - see [LICENSE.md](../LICENSE.md) for details.

## Support

- **Documentation**: Browse individual template docs
- **Issues**: Report bugs or request features on GitHub
- **Discussions**: Join community discussions
- **Examples**: Check the [examples directory](examples/)

---

_Documentation generated automatically from 7 templates_
_Last updated: 2025-07-15 21:54:36_

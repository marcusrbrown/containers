# Container Template System

A comprehensive containerization toolkit with pre-built templates for common application stacks, including template validation, customization scripts, documentation generation, and integration with existing automation tools.

## 🚀 Features

- **Template System**: Pre-built templates for Node.js, Python FastAPI, Go microservices, databases, and infrastructure
- **Template Inheritance**: Base templates with specialized variants
- **Parameter Validation**: JSON Schema validation with type checking
- **Documentation Generation**: Automatic README and API documentation
- **Testing Framework**: Comprehensive template validation and testing
- **Multi-Platform Support**: Docker images for AMD64 and ARM64
- **Security Hardening**: Non-root users, minimal images, security scanning
- **Production Ready**: Performance optimizations and best practices

## 📦 Available Templates

### Application Stacks

- **Node.js Express** (`apps/nodejs/express`) - TypeScript, hot reload, security middleware
- **Python FastAPI** (`apps/python/fastapi`) - Async APIs, database integration, OpenAPI docs
- **Go Microservices** (`microservices/go`) - gRPC + REST, metrics, distributed tracing

### Databases

- **PostgreSQL** (`databases/postgresql`) - Performance tuned, backup automation
- **Redis** (`databases/redis`) - Caching, persistence, clustering support

### Infrastructure

- **nginx** (`infrastructure/nginx`) - Reverse proxy, SSL termination, load balancing

### Base Images

- **Alpine Linux** (`base/alpine`) - Secure base with hardening

## 🛠 Installation

```bash
# Clone the repository
git clone https://github.com/marcusrbrown/containers.git
cd containers

# Install dependencies
poetry install

# Verify installation
poetry run containers list
```

## 🎯 Quick Start

### List Available Templates

```bash
poetry run containers list
```

### Get Template Information

```bash
poetry run containers info apps/nodejs/express
```

### Generate a Project

```bash
# Basic generation
poetry run containers generate apps/nodejs/express ./my-app

# With custom parameters
poetry run containers generate apps/python/fastapi ./my-api \
  --param app_name=my-api \
  --param port=8080 \
  --param debug=true

# Dry run to see what would be generated
poetry run containers generate apps/nodejs/express ./my-app --dry-run
```

### Generate Documentation

```bash
# Generate docs for all templates
poetry run containers docs

# Generate docs for specific template
poetry run containers docs --template apps/nodejs/express

# Serve documentation locally
poetry run containers docs --serve --port 8000
```

## 📋 CLI Commands

### `containers list [--format table|json] [--category app|database|infrastructure]`

List available templates with filtering options.

### `containers info <template>`

Show detailed information about a template including parameters and dependencies.

### `containers generate <template> <output-dir> [options]`

Generate a project from a template.

Options:

- `--dry-run` - Show what would be generated without creating files
- `--param key=value` - Set template parameters
- `--params file.json` - Load parameters from JSON file

### `containers docs [--template <template>] [--output dir] [--serve]`

Generate comprehensive documentation for templates.

## 🏗 Template Structure

Each template follows a standardized structure:

```
templates/category/name/
├── template.yaml      # Template metadata and parameters
├── Dockerfile         # Container definition
├── docker-compose.yml # Multi-service orchestration
├── config/           # Configuration files
├── scripts/          # Helper scripts
└── docs/            # Template-specific documentation
```

### Template Metadata (`template.yaml`)

```yaml
name: "Template Name"
version: "1.0.0"
description: "Template description"
category: "app|database|infrastructure|microservice|base"
inherits: "base/alpine" # Optional inheritance

parameters:
  param_name:
    type: string|integer|boolean|array
    description: "Parameter description"
    default: "default_value"
    required: true|false
    # Additional validation rules

files:
  dockerfile: "Dockerfile"
  compose: "docker-compose.yml"
  config: ["file1.conf", "file2.json"]

dependencies:
  build: ["package1", "package2"]
  runtime: ["runtime-pkg"]
  test: ["test-framework"]

testing:
  health_check: "curl -f http://localhost:8080/health"
  test_commands: ["npm test", "docker build ."]
```

## 🔧 Template Development

### Creating New Templates

```bash
# Initialize a new template
poetry run containers init my-new-template --category app \
  --description "My custom application template"

# Customize the generated template
cd templates/app/my-new-template
# Edit template.yaml, Dockerfile, etc.

# Test your template
poetry run containers generate app/my-new-template ./test-output --dry-run
```

### Template Inheritance

Templates can inherit from base templates:

```yaml
# In template.yaml
inherits: "base/alpine"
```

This allows:

- Reusing common configuration
- Layered security and optimization
- Consistent base images across templates

### Parameter System

Templates support rich parameter validation:

```yaml
parameters:
  app_name:
    type: string
    pattern: "^[a-z][a-z0-9-]*[a-z0-9]$"
    required: true

  port:
    type: integer
    minimum: 1024
    maximum: 65535
    default: 8080

  features:
    type: array
    items:
      type: string
      enum: ["auth", "metrics", "logging"]
    default: ["metrics"]
```

## 🧪 Testing

### Template Validation

```bash
# Validate template structure
poetry run template-engine validate apps/nodejs/express

# Run comprehensive tests
poetry run template-testing test apps/nodejs/express

# Test with custom parameters
poetry run template-testing test apps/nodejs/express --params test-params.json
```

### Integration Testing

```bash
# Test actual Docker builds
poetry run template-testing test apps/nodejs/express --integration

# Performance testing
poetry run template-testing test apps/nodejs/express --performance
```

## 🔒 Security Features

- **Non-root execution**: All containers run as non-root users
- **Minimal attack surface**: Alpine-based images with minimal packages
- **Security scanning**: Automated vulnerability detection
- **Capability dropping**: Containers drop unnecessary Linux capabilities
- **Read-only filesystems**: Where applicable for additional security
- **Secret management**: Secure handling of sensitive configuration

## 🏭 Production Deployment

### Docker Compose Stack

```bash
# Generate and deploy a complete stack
poetry run containers generate apps/python/fastapi ./my-api
cd my-api
docker-compose up -d

# Scale services
docker-compose up -d --scale api=3
```

### Kubernetes Deployment

```bash
# Generate Kubernetes manifests (if template supports it)
poetry run containers generate apps/nodejs/express ./my-app --platform kubernetes
kubectl apply -f my-app/k8s/
```

### Multi-Architecture Builds

```bash
# Build for multiple platforms
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest .
```

## 📊 Monitoring and Observability

Templates include built-in support for:

- **Health checks**: Standardized health endpoints
- **Metrics**: Prometheus metrics collection
- **Logging**: Structured logging with correlation IDs
- **Tracing**: Distributed tracing with OpenTelemetry
- **Dashboards**: Pre-configured Grafana dashboards

## 🔄 CI/CD Integration

### GitHub Actions

```yaml
name: Deploy from Template
on: [push]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Poetry
        uses: snok/install-poetry@v1
      - name: Generate Application
        run: |
          poetry install
          poetry run containers generate apps/nodejs/express ./app
      - name: Build and Deploy
        run: |
          cd app
          docker build -t ${{ env.IMAGE_NAME }} .
          docker push ${{ env.IMAGE_NAME }}
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your template or enhancement
4. Test thoroughly
5. Submit a pull request

### Template Contribution Guidelines

- Follow the standard template structure
- Include comprehensive parameter validation
- Provide clear documentation
- Add appropriate tests
- Follow security best practices

## 📖 Examples

See the [examples directory](examples/) for complete working examples and tutorials.

## 🐛 Troubleshooting

### Common Issues

**Q: Template generation fails with "Template not found"**
A: Verify the template path with `poetry run containers list`

**Q: Docker build fails in generated project**
A: Check that all required parameters are set and Docker is running

**Q: Permission denied errors**
A: Ensure your user has Docker permissions and the output directory is writable

### Debug Mode

```bash
# Enable verbose logging
export DEBUG=1
poetry run containers generate apps/nodejs/express ./debug-app
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## 🙏 Acknowledgments

- Built with [Poetry](https://python-poetry.org/) for dependency management
- Template engine powered by [Jinja2](https://jinja.palletsprojects.com/)
- Validation with [JSON Schema](https://json-schema.org/)
- Documentation generation with custom tooling

---

**Get started today**: `poetry run containers list` 🚀

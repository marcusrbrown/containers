#!/usr/bin/env python3
"""
Template Documentation Generator

Automatically generates comprehensive documentation for container templates
including usage guides, parameter references, examples, and API documentation.
"""

import json
import os
import shutil
from pathlib import Path
from typing import Dict, List, Optional, Any
from datetime import datetime

from .template_engine import TemplateEngine


class DocumentationGenerator:
    """Generates documentation for container templates."""

    def __init__(
        self, templates_dir: str = "templates", docs_dir: str = "docs/templates"
    ):
        """Initialize the documentation generator.

        Args:
            templates_dir: Path to templates directory
            docs_dir: Path to documentation output directory
        """
        self.templates_dir = Path(templates_dir)
        self.docs_dir = Path(docs_dir)
        self.engine = TemplateEngine(str(templates_dir))

        # Create docs directory
        self.docs_dir.mkdir(parents=True, exist_ok=True)

    def generate_all_documentation(self) -> Dict[str, str]:
        """Generate documentation for all templates.

        Returns:
            Dictionary mapping template paths to generated doc paths
        """
        templates = self.engine.list_templates()
        generated_docs = {}

        print(f"📚 Generating documentation for {len(templates)} templates...")

        # Generate individual template docs
        for template in templates:
            doc_path = self.generate_template_documentation(template["path"])
            generated_docs[template["path"]] = doc_path

        # Generate index documentation
        index_path = self.generate_index_documentation(templates)
        generated_docs["index"] = index_path

        # Generate category documentation
        categories = set(template["category"] for template in templates)
        for category in categories:
            category_templates = [t for t in templates if t["category"] == category]
            category_path = self.generate_category_documentation(
                category, category_templates
            )
            generated_docs[f"category_{category}"] = category_path

        # Generate API documentation
        api_path = self.generate_api_documentation()
        generated_docs["api"] = api_path

        print(f"✅ Generated documentation for {len(generated_docs)} components")
        return generated_docs

    def generate_template_documentation(self, template_path: str) -> str:
        """Generate documentation for a specific template.

        Args:
            template_path: Path to the template

        Returns:
            Path to generated documentation file
        """
        try:
            metadata = self.engine.resolve_inheritance(template_path)

            # Create template-specific doc directory
            doc_dir = self.docs_dir / template_path
            doc_dir.mkdir(parents=True, exist_ok=True)

            # Generate main README
            readme_path = doc_dir / "README.md"
            readme_content = self._generate_template_readme(metadata, template_path)

            with open(readme_path, "w") as f:
                f.write(readme_content)

            # Generate parameter reference
            params_path = doc_dir / "PARAMETERS.md"
            params_content = self._generate_parameter_reference(metadata)

            with open(params_path, "w") as f:
                f.write(params_content)

            # Generate usage examples
            examples_path = doc_dir / "EXAMPLES.md"
            examples_content = self._generate_usage_examples(metadata, template_path)

            with open(examples_path, "w") as f:
                f.write(examples_content)

            # Generate troubleshooting guide
            troubleshooting_path = doc_dir / "TROUBLESHOOTING.md"
            troubleshooting_content = self._generate_troubleshooting_guide(
                metadata, template_path
            )

            with open(troubleshooting_path, "w") as f:
                f.write(troubleshooting_content)

            print(f"  ✅ {template_path}")
            return str(readme_path)

        except Exception as e:
            print(f"  ❌ {template_path}: {e}")
            return ""

    def _generate_template_readme(self, metadata: Dict, template_path: str) -> str:
        """Generate main README for a template."""
        name = metadata.get("name", template_path)
        description = metadata.get("description", "Container template")
        version = metadata.get("version", "1.0.0")
        author = metadata.get("author", "Unknown")
        license_info = metadata.get("license", "MIT")
        category = metadata.get("category", "unknown")
        tags = metadata.get("tags", [])

        # Get parameters for quick reference
        parameters = metadata.get("parameters", {})
        required_params = [
            name for name, param in parameters.items() if param.get("required", False)
        ]
        optional_params = [
            name
            for name, param in parameters.items()
            if not param.get("required", False)
        ]

        # Get file types
        files = metadata.get("files", {})

        content = f"""# {name}

{description}

## Overview

- **Category**: {category.title()}
- **Version**: {version}
- **Author**: {author}
- **License**: {license_info}
- **Tags**: {', '.join(tags) if tags else 'None'}

## Quick Start

### Generate from Template

```bash
# Basic usage
poetry run template-engine generate {template_path} ./my-{name}

# With custom parameters
poetry run template-engine generate {template_path} ./my-{name} \\
  --param param_name=value \\
  --param another_param=value

# Using parameter file
poetry run template-engine generate {template_path} ./my-{name} \\
  --params params.json
```

### Using Docker Compose

```bash
cd my-{name}
docker-compose up -d
```

### Manual Docker Build

```bash
cd my-{name}
docker build -t my-{name}:latest .
docker run -d --name my-{name} my-{name}:latest
```

## Parameters

### Required Parameters
{self._format_parameter_list(parameters, required_params) if required_params else 'None'}

### Optional Parameters
{self._format_parameter_list(parameters, optional_params) if optional_params else 'None'}

[📋 **Full Parameter Reference**](PARAMETERS.md)

## Generated Files

This template generates the following files:

"""

        for file_type, file_patterns in files.items():
            if isinstance(file_patterns, str):
                file_patterns = [file_patterns]

            content += f"### {file_type.title()}\n"
            for pattern in file_patterns:
                content += f"- `{pattern}`\n"
            content += "\n"

        content += f"""
## Examples

[📖 **Usage Examples**](EXAMPLES.md)

## Troubleshooting

[🔧 **Troubleshooting Guide**](TROUBLESHOOTING.md)

## Dependencies

"""

        dependencies = metadata.get("dependencies", {})
        for dep_type, deps in dependencies.items():
            if deps:
                content += f"### {dep_type.title()}\n"
                for dep in deps:
                    content += f"- {dep}\n"
                content += "\n"

        platforms = metadata.get("platforms", [])
        if platforms:
            content += f"""## Supported Platforms

{', '.join(platforms)}

"""

        testing = metadata.get("testing", {})
        if testing:
            content += """## Testing

This template includes comprehensive testing:

"""
            if testing.get("test_commands"):
                content += "### Test Commands\n"
                for cmd in testing["test_commands"]:
                    content += f"- `{cmd}`\n"
                content += "\n"

            if testing.get("integration_tests"):
                content += "### Integration Tests\n"
                for test in testing["integration_tests"]:
                    content += f"- `{test}`\n"
                content += "\n"

        content += f"""
## Contributing

To modify this template:

1. Edit the template files in `templates/{template_path}/`
2. Update `template.yaml` for parameter changes
3. Test your changes: `poetry run template-engine test {template_path}`
4. Regenerate documentation: `poetry run generate-docs`

## Related Templates

Browse other templates in the same category: [**{category.title()} Templates**](../{category}/README.md)

---

*Documentation generated automatically from template metadata*
*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        return content

    def _format_parameter_list(self, parameters: Dict, param_names: List[str]) -> str:
        """Format a list of parameters for documentation."""
        if not param_names:
            return "None"

        content = ""
        for param_name in param_names:
            param = parameters[param_name]
            param_type = param.get("type", "string")
            description = param.get("description", "No description")
            default = param.get("default")

            content += f"- `{param_name}` ({param_type}): {description}"
            if default is not None:
                content += f" (default: `{default}`)"
            content += "\n"

        return content

    def _generate_parameter_reference(self, metadata: Dict) -> str:
        """Generate comprehensive parameter reference."""
        name = metadata.get("name", "Template")
        parameters = metadata.get("parameters", {})

        content = f"""# {name} - Parameter Reference

Complete reference for all available parameters.

## Parameter Overview

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
"""

        for param_name, param_def in parameters.items():
            param_type = param_def.get("type", "string")
            required = "✅" if param_def.get("required", False) else "❌"
            default = param_def.get("default", "—")
            description = param_def.get("description", "No description")

            content += f"| `{param_name}` | {param_type} | {required} | `{default}` | {description} |\n"

        content += "\n## Detailed Parameter Descriptions\n\n"

        for param_name, param_def in parameters.items():
            content += f"### `{param_name}`\n\n"
            content += f"- **Type**: {param_def.get('type', 'string')}\n"
            content += f"- **Required**: {'Yes' if param_def.get('required', False) else 'No'}\n"
            content += (
                f"- **Description**: {param_def.get('description', 'No description')}\n"
            )

            if "default" in param_def:
                content += f"- **Default**: `{param_def['default']}`\n"

            if "enum" in param_def:
                content += f"- **Allowed Values**: {', '.join(f'`{v}`' for v in param_def['enum'])}\n"

            if "pattern" in param_def:
                content += f"- **Pattern**: `{param_def['pattern']}`\n"

            if param_def.get("type") in ["integer", "number"]:
                if "min" in param_def:
                    content += f"- **Minimum**: {param_def['min']}\n"
                if "max" in param_def:
                    content += f"- **Maximum**: {param_def['max']}\n"

            content += "\n"

        content += f"""
## Parameter Examples

### Basic Usage

```bash
poetry run template-engine generate {metadata.get('name', 'template')} ./output \\
"""

        # Add example parameters
        example_params = []
        for param_name, param_def in list(parameters.items())[
            :3
        ]:  # Show first 3 parameters
            if "default" in param_def:
                example_params.append(f"  --param {param_name}={param_def['default']}")

        content += " \\\n".join(example_params)
        content += "\n```\n"

        content += """
### Using Parameter File

Create a `params.json` file:

```json
{
"""

        # Add JSON example
        json_params = []
        for param_name, param_def in list(parameters.items())[
            :5
        ]:  # Show first 5 parameters
            if "default" in param_def:
                value = param_def["default"]
                if isinstance(value, str):
                    json_params.append(f'  "{param_name}": "{value}"')
                else:
                    json_params.append(f'  "{param_name}": {json.dumps(value)}')

        content += ",\n".join(json_params)
        content += """
}
```

Then use it:

```bash
poetry run template-engine generate template_name ./output --params params.json
```

---

*Parameter reference generated automatically from template metadata*
"""

        return content

    def _generate_usage_examples(self, metadata: Dict, template_path: str) -> str:
        """Generate usage examples."""
        name = metadata.get("name", template_path)
        category = metadata.get("category", "unknown")

        content = f"""# {name} - Usage Examples

Practical examples for using this template in different scenarios.

## Basic Example

```bash
# Generate template with defaults
poetry run template-engine generate {template_path} ./my-{name}

# Navigate to generated directory
cd my-{name}

# Build and run with Docker
docker build -t my-{name}:latest .
docker run -d --name my-{name} my-{name}:latest
```

## Development Example

```bash
# Generate with development settings
poetry run template-engine generate {template_path} ./my-{name}-dev \\
  --param environment=development \\
  --param debug=true

cd my-{name}-dev

# Use Docker Compose for development
docker-compose up -d

# View logs
docker-compose logs -f
```

## Production Example

```bash
# Generate with production optimizations
poetry run template-engine generate {template_path} ./my-{name}-prod \\
  --param environment=production \\
  --param enable_ssl=true \\
  --param security_hardening=true

cd my-{name}-prod

# Build production image
docker build -t my-{name}:prod .

# Run with production settings
docker run -d \\
  --name my-{name}-prod \\
  --restart unless-stopped \\
  -p 80:80 \\
  -p 443:443 \\
  my-{name}:prod
```

"""

        # Add category-specific examples
        if category == "app":
            content += self._generate_app_examples(metadata, template_path)
        elif category == "database":
            content += self._generate_database_examples(metadata, template_path)
        elif category == "infrastructure":
            content += self._generate_infrastructure_examples(metadata, template_path)

        content += (
            """
## CI/CD Integration

### GitHub Actions

```yaml
name: Build and Deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Generate from template
        run: |
          poetry install
          poetry run template-engine generate """
            + template_path
            + """ ./app

      - name: Build Docker image
        run: |
          cd app
          docker build -t my-app:${{ github.sha }} .

      - name: Deploy
        run: |
          # Add your deployment commands here
          echo "Deploying my-app:${{ github.sha }}"
```

### GitLab CI

```yaml
stages:
  - build
  - deploy

build:
  stage: build
  script:
    - poetry install
    - poetry run template-engine generate """
            + template_path
            + """ ./app
    - cd app
    - docker build -t my-app:$CI_COMMIT_SHA .
    - docker push my-app:$CI_COMMIT_SHA

deploy:
  stage: deploy
  script:
    - docker run -d my-app:$CI_COMMIT_SHA
  only:
    - main
```

## Testing Examples

```bash
# Validate template
poetry run template-engine validate """
            + template_path
            + """

# Test template generation
poetry run template-engine test """
            + template_path
            + """

# Test with custom parameters
poetry run template-engine test """
            + template_path
            + """ --params test-params.json

# Run comprehensive tests
poetry run template-testing """
            + template_path
            + """ --integration --performance
```

## Customization Examples

### Parameter File Approach

Create `custom-params.json`:

```json
{
  "app_name": "my-custom-app",
  "version": "2.0.0",
  "enable_monitoring": true,
  "custom_settings": {
    "feature_flags": ["feature_a", "feature_b"]
  }
}
```

```bash
poetry run template-engine generate """
            + template_path
            + """ ./custom-app \\
  --params custom-params.json
```

### Environment-Specific Configurations

```bash
# Development
poetry run template-engine generate """
            + template_path
            + """ ./dev \\
  --param environment=dev \\
  --param debug=true \\
  --param hot_reload=true

# Staging
poetry run template-engine generate """
            + template_path
            + """ ./staging \\
  --param environment=staging \\
  --param monitoring=true \\
  --param ssl=true

# Production
poetry run template-engine generate """
            + template_path
            + """ ./prod \\
  --param environment=prod \\
  --param security_hardening=true \\
  --param backup_enabled=true \\
  --param monitoring=true
```

---

*Examples generated automatically for template: """
            + template_path
            + """*
"""
        )

        return content

    def _generate_app_examples(self, metadata: Dict, template_path: str) -> str:
        """Generate application-specific examples."""
        return (
            """
## Application-Specific Examples

### Multi-Container Setup

```bash
# Generate app
poetry run template-engine generate """
            + template_path
            + """ ./my-app

# Generate database
poetry run template-engine generate databases/postgresql ./my-db

# Create docker-compose.override.yml
cat > docker-compose.override.yml << EOF
version: '3.8'
services:
  app:
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb

  db:
    image: my-db:latest
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
EOF

# Start the stack
docker-compose up -d
```

### Load Balancing

```bash
# Generate multiple app instances
for i in {1..3}; do
  poetry run template-engine generate """
            + template_path
            + """ ./app-$i \\
    --param app_name=app-$i \\
    --param port=$((3000 + $i))
done

# Generate nginx load balancer
poetry run template-engine generate infrastructure/nginx ./nginx \\
  --param upstream_servers="app-1:3001,app-2:3002,app-3:3003"
```
"""
        )

    def _generate_database_examples(self, metadata: Dict, template_path: str) -> str:
        """Generate database-specific examples."""
        return (
            """
## Database-Specific Examples

### Data Persistence

```bash
# Create named volume for data persistence
docker volume create my-db-data

# Run with persistent storage
docker run -d \\
  --name my-database \\
  -v my-db-data:/var/lib/postgresql/data \\
  -p 5432:5432 \\
  my-db:latest
```

### Backup and Restore

```bash
# Create backup
docker exec my-database /usr/local/bin/backup.sh

# List backups
docker exec my-database ls -la /var/lib/postgresql/backups/

# Restore from backup
docker exec my-database /usr/local/bin/restore.sh backup-2024-01-15.sql
```

### Replication Setup

```bash
# Master database
poetry run template-engine generate """
            + template_path
            + """ ./db-master \\
  --param replication_role=master \\
  --param max_wal_senders=3

# Replica database
poetry run template-engine generate """
            + template_path
            + """ ./db-replica \\
  --param replication_role=replica \\
  --param master_host=db-master
```
"""
        )

    def _generate_infrastructure_examples(
        self, metadata: Dict, template_path: str
    ) -> str:
        """Generate infrastructure-specific examples."""
        return (
            """
## Infrastructure-Specific Examples

### SSL Termination

```bash
# Generate with SSL support
poetry run template-engine generate """
            + template_path
            + """ ./nginx-ssl \\
  --param enable_ssl=true \\
  --param ssl_cert_path=/etc/ssl/certs/cert.pem \\
  --param ssl_key_path=/etc/ssl/private/key.pem

# Mount SSL certificates
docker run -d \\
  --name nginx-ssl \\
  -v /path/to/certs:/etc/ssl/certs:ro \\
  -v /path/to/keys:/etc/ssl/private:ro \\
  -p 80:80 -p 443:443 \\
  nginx-ssl:latest
```

### High Availability

```bash
# Generate multiple instances
for i in {1..3}; do
  poetry run template-engine generate """
            + template_path
            + """ ./nginx-$i \\
    --param instance_id=$i \\
    --param cluster_mode=true
done

# Use with keepalived or similar for HA
```
"""
        )

    def _generate_troubleshooting_guide(
        self, metadata: Dict, template_path: str
    ) -> str:
        """Generate troubleshooting guide."""
        name = metadata.get("name", template_path)
        category = metadata.get("category", "unknown")

        content = f"""# {name} - Troubleshooting Guide

Common issues and solutions for this template.

## Template Generation Issues

### Issue: Template validation fails

```bash
poetry run template-engine validate {template_path}
```

**Common causes:**
- Missing required parameters
- Invalid parameter values
- Template syntax errors

**Solutions:**
- Check parameter requirements: `poetry run template-engine list`
- Validate your parameters against the schema
- Check template files for syntax errors

### Issue: Template generation produces empty files

**Symptoms:**
- Files are created but have no content
- Jinja2 template errors in output

**Solutions:**
- Verify all required parameters are provided
- Check parameter types match template expectations
- Review template syntax in source files

## Container Build Issues

### Issue: Docker build fails

```bash
# Check build logs
docker build -t {name}:debug . --no-cache

# Build with verbose output
docker build -t {name}:debug . --progress=plain
```

**Common causes:**
- Base image not available
- Package installation failures
- File permission issues
- Network connectivity problems

**Solutions:**
- Verify base image exists and is accessible
- Check package manager commands
- Ensure proper file permissions in Dockerfile
- Check network connectivity and proxy settings

### Issue: Build takes too long

**Solutions:**
- Use multi-stage builds
- Optimize package installation order
- Use .dockerignore to exclude unnecessary files
- Consider using different base images

## Container Runtime Issues

### Issue: Container exits immediately

```bash
# Check container logs
docker logs container_name

# Run interactively for debugging
docker run -it --entrypoint /bin/sh {name}:latest
```

**Common causes:**
- Application startup failures
- Missing environment variables
- Permission issues
- Port conflicts

**Solutions:**
- Check application logs
- Verify all required environment variables are set
- Ensure proper user permissions
- Check for port conflicts

### Issue: Container health check fails

```bash
# Manual health check
docker exec container_name /usr/local/bin/healthcheck.sh

# Check health status
docker inspect container_name | grep Health -A 10
```

**Solutions:**
- Verify health check script exists and is executable
- Check application is actually running
- Verify health check endpoint is accessible
- Adjust health check timeouts

"""

        # Add category-specific troubleshooting
        if category == "app":
            content += self._generate_app_troubleshooting()
        elif category == "database":
            content += self._generate_database_troubleshooting()
        elif category == "infrastructure":
            content += self._generate_infrastructure_troubleshooting()

        content += f"""
## Performance Issues

### Issue: High memory usage

```bash
# Monitor memory usage
docker stats container_name

# Check memory limits
docker inspect container_name | grep -i memory
```

**Solutions:**
- Set appropriate memory limits
- Optimize application memory usage
- Use lighter base images
- Profile application memory usage

### Issue: Slow response times

**Debugging steps:**
```bash
# Check CPU usage
docker stats container_name

# Network latency
docker exec container_name ping target_host

# Application metrics
docker exec container_name curl localhost:port/metrics
```

## Getting Help

### Check logs
```bash
# Container logs
docker logs container_name

# System logs
docker events

# Docker daemon logs
sudo journalctl -u docker.service
```

### Debug mode
```bash
# Run with debug output
poetry run template-engine generate {template_path} ./debug \\
  --param debug=true \\
  --param log_level=debug

# Interactive debugging
docker run -it --entrypoint /bin/bash {name}:latest
```

### Community resources
- Template documentation: [README.md](README.md)
- Parameter reference: [PARAMETERS.md](PARAMETERS.md)
- Usage examples: [EXAMPLES.md](EXAMPLES.md)
- GitHub issues: [Report a bug or request a feature]

---

*Troubleshooting guide for template: {template_path}*
*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        return content

    def _generate_app_troubleshooting(self) -> str:
        """Generate application-specific troubleshooting."""
        return """
## Application-Specific Issues

### Issue: Application won't start

**Common causes:**
- Missing dependencies
- Configuration errors
- Database connection failures
- Port already in use

**Solutions:**
```bash
# Check dependencies
docker exec container_name npm list  # Node.js
docker exec container_name pip list  # Python

# Check configuration
docker exec container_name env | grep APP_

# Test database connection
docker exec container_name nc -zv database_host 5432
```

### Issue: API endpoints not responding

**Debugging:**
```bash
# Check if application is listening
docker exec container_name netstat -tlnp

# Test endpoints locally
docker exec container_name curl localhost:3000/health

# Check routing configuration
docker exec container_name cat /etc/nginx/nginx.conf
```
"""

    def _generate_database_troubleshooting(self) -> str:
        """Generate database-specific troubleshooting."""
        return """
## Database-Specific Issues

### Issue: Database won't start

**Common causes:**
- Data directory permissions
- Configuration errors
- Insufficient disk space
- Port conflicts

**Solutions:**
```bash
# Check permissions
docker exec container_name ls -la /var/lib/postgresql/data

# Check disk space
docker exec container_name df -h

# Check configuration
docker exec container_name pg_ctl status
```

### Issue: Connection refused

**Debugging:**
```bash
# Check if database is listening
docker exec container_name netstat -tlnp | grep 5432

# Test connection
docker exec container_name psql -h localhost -U username -d database

# Check authentication
docker exec container_name cat /var/lib/postgresql/data/pg_hba.conf
```

### Issue: Performance problems

**Solutions:**
```bash
# Check running queries
docker exec container_name psql -c "SELECT * FROM pg_stat_activity;"

# Check locks
docker exec container_name psql -c "SELECT * FROM pg_locks;"

# Analyze slow queries
docker exec container_name psql -c "SELECT * FROM pg_stat_statements ORDER BY total_time DESC;"
```
"""

    def _generate_infrastructure_troubleshooting(self) -> str:
        """Generate infrastructure-specific troubleshooting."""
        return """
## Infrastructure-Specific Issues

### Issue: Load balancer not distributing traffic

**Debugging:**
```bash
# Check upstream servers
docker exec nginx_container nginx -T | grep upstream

# Test backend connectivity
docker exec nginx_container curl backend_server:port/health

# Check access logs
docker logs nginx_container | tail -f
```

### Issue: SSL certificate problems

**Solutions:**
```bash
# Check certificate validity
docker exec container_name openssl x509 -in /etc/ssl/cert.pem -noout -dates

# Test SSL configuration
docker exec container_name openssl s_client -connect localhost:443

# Check nginx SSL configuration
docker exec container_name nginx -t
```
"""

    def generate_index_documentation(self, templates: List[Dict]) -> str:
        """Generate index documentation for all templates."""
        index_path = self.docs_dir / "README.md"

        # Group templates by category
        categories = {}
        for template in templates:
            category = template.get("category", "other")
            if category not in categories:
                categories[category] = []
            categories[category].append(template)

        content = f"""# Container Template Documentation

Comprehensive documentation for all available container templates.

## Overview

This repository contains **{len(templates)} templates** across **{len(categories)} categories** to help you quickly bootstrap containerized applications and infrastructure.

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

"""

        for category, category_templates in sorted(categories.items()):
            content += f"### {category.title()} Templates\n\n"
            content += f"*{len(category_templates)} templates available*\n\n"

            for template in sorted(category_templates, key=lambda x: x["name"]):
                content += f"- **[{template['name']}]({template['path']}/README.md)** - {template['description']}\n"

            content += (
                f"\n[📋 **Browse all {category} templates**]({category}/README.md)\n\n"
            )

        content += """
## Template Library

| Name | Category | Description | Version |
|------|----------|-------------|---------|
"""

        for template in sorted(templates, key=lambda x: (x["category"], x["name"])):
            content += f"| [{template['name']}]({template['path']}/README.md) | {template['category']} | {template['description']} | {template.get('version', '1.0.0')} |\n"

        content += f"""

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
poetry run template-engine generate <template-path> <output-dir> \\
  --param name=value \\
  --param another=value

# Use parameter file
poetry run template-engine generate <template-path> <output-dir> \\
  --params params.json

# Validate template
poetry run template-engine validate <template-path>

# Test template
poetry run template-engine test <template-path>
```

### Parameter Files

Create a `params.json` file for reusable configurations:

```json
{{
  "app_name": "my-application",
  "version": "1.0.0",
  "environment": "production",
  "enable_ssl": true,
  "custom_settings": {{
    "feature_flags": ["feature_a", "feature_b"]
  }}
}}
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
          python-version: '3.11'

      - name: Install Poetry
        run: curl -sSL https://install.python-poetry.org | python3 -

      - name: Install dependencies
        run: poetry install

      - name: Generate from template
        run: |
          poetry run template-engine generate apps/nodejs/express ./app \\
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
   category: "app"  # app, database, infrastructure, microservice, base

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

*Documentation generated automatically from {len(templates)} templates*
*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""

        with open(index_path, "w") as f:
            f.write(content)

        return str(index_path)

    def generate_category_documentation(
        self, category: str, templates: List[Dict]
    ) -> str:
        """Generate documentation for a template category."""
        category_dir = self.docs_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)

        readme_path = category_dir / "README.md"

        content = f"""# {category.title()} Templates

Collection of {len(templates)} templates for {category} containers.

## Available Templates

"""

        for template in sorted(templates, key=lambda x: x["name"]):
            content += f"""### [{template['name']}]({template['path']}/README.md)

{template['description']}

- **Version**: {template.get('version', '1.0.0')}
- **Tags**: {', '.join(template.get('tags', []))}

```bash
poetry run template-engine generate {template['path']} ./my-{template['name']}
```

---

"""

        content += f"""
## Category Overview

{category.title()} templates provide pre-configured containers for common {category} scenarios. Each template includes:

- Production-ready configuration
- Security hardening
- Performance optimization
- Comprehensive documentation
- Automated testing

## Common Use Cases

"""

        if category == "app":
            content += """
- **Web Applications**: Full-stack web apps with frameworks like Express, FastAPI
- **API Services**: RESTful and GraphQL API backends
- **Microservices**: Containerized microservice components
- **Background Workers**: Queue processors and scheduled tasks
"""
        elif category == "database":
            content += """
- **Primary Databases**: Production database instances
- **Read Replicas**: Scalable read-only database copies
- **Analytics**: Data warehousing and analytics databases
- **Caching**: In-memory data stores for performance
"""
        elif category == "infrastructure":
            content += """
- **Load Balancers**: Traffic distribution and SSL termination
- **Reverse Proxies**: Request routing and caching
- **API Gateways**: Service mesh entry points
- **Monitoring**: Observability and alerting systems
"""
        elif category == "base":
            content += """
- **Foundation Images**: Secure, minimal base containers
- **Multi-stage Builds**: Optimized build environments
- **Language Runtimes**: Pre-configured runtime environments
- **Security Hardening**: Compliance-ready base images
"""

        content += f"""

## Getting Started

1. **Choose a template** from the list above
2. **Generate your project**:
   ```bash
   poetry run template-engine generate template-path ./my-project
   ```
3. **Customize parameters** as needed
4. **Build and deploy** your container

## Template Comparison

| Template | Use Case | Size | Complexity | Best For |
|----------|----------|------|------------|----------|
"""

        for template in templates:
            complexity = "Simple" if len(template.get("tags", [])) <= 3 else "Complex"
            use_case = (
                template["description"][:30] + "..."
                if len(template["description"]) > 30
                else template["description"]
            )

            content += f"| {template['name']} | {use_case} | TBD | {complexity} | Production use |\n"

        content += f"""

## Related Categories

- [**App Templates**](../app/README.md) - Application containers
- [**Database Templates**](../database/README.md) - Database systems
- [**Infrastructure Templates**](../infrastructure/README.md) - Infrastructure components
- [**Base Templates**](../base/README.md) - Foundation images

[⬅️ **Back to all templates**](../README.md)

---

*{category.title()} category documentation*
*{len(templates)} templates available*
"""

        with open(readme_path, "w") as f:
            f.write(content)

        return str(readme_path)

    def generate_api_documentation(self) -> str:
        """Generate API documentation."""
        api_path = self.docs_dir / "API.md"

        content = """# Template Engine API Documentation

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
poetry run template-engine generate apps/nodejs/express ./my-app \\
  --param app_name=my-api \\
  --param port=8080

# Using parameter file
poetry run template-engine generate apps/nodejs/express ./my-app \\
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
poetry run template-testing apps/nodejs/express \\
  --integration \\
  --performance \\
  --output report.md

# JSON report
poetry run template-testing apps/nodejs/express \\
  --format json \\
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
"""

        with open(api_path, "w") as f:
            f.write(content)

        return str(api_path)


def main():
    """CLI interface for documentation generator."""
    import argparse

    parser = argparse.ArgumentParser(description="Template Documentation Generator")
    parser.add_argument("--output", default="docs/templates", help="Output directory")
    parser.add_argument("--template", help="Generate docs for specific template only")

    args = parser.parse_args()

    generator = DocumentationGenerator(docs_dir=args.output)

    if args.template:
        doc_path = generator.generate_template_documentation(args.template)
        print(f"Generated documentation: {doc_path}")
    else:
        generated_docs = generator.generate_all_documentation()
        print(f"Generated {len(generated_docs)} documentation files")


if __name__ == "__main__":
    main()

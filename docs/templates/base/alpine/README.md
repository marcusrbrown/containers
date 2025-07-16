# alpine-base

Alpine Linux base template with security hardening and common utilities

## Overview

- **Category**: Base
- **Version**: 1.0.0
- **Author**: Container Template Engine
- **License**: MIT
- **Tags**: alpine, base, minimal, security

## Quick Start

### Generate from Template

```bash
# Basic usage
poetry run template-engine generate base/alpine ./my-alpine-base

# With custom parameters
poetry run template-engine generate base/alpine ./my-alpine-base \
  --param param_name=value \
  --param another_param=value

# Using parameter file
poetry run template-engine generate base/alpine ./my-alpine-base \
  --params params.json
```

### Using Docker Compose

```bash
cd my-alpine-base
docker-compose up -d
```

### Manual Docker Build

```bash
cd my-alpine-base
docker build -t my-alpine-base:latest .
docker run -d --name my-alpine-base my-alpine-base:latest
```

## Parameters

### Required Parameters

None

### Optional Parameters

- `alpine_version` (string): Alpine Linux version (default: `3.20`)
- `packages` (array): Additional packages to install (default: `['curl', 'wget', 'ca-certificates']`)
- `user_name` (string): Non-root user name (default: `appuser`)
- `user_uid` (integer): User UID (default: `1000`)
- `timezone` (string): System timezone (default: `UTC`)
- `enable_security_updates` (boolean): Enable automatic security updates (default: `True`)

[📋 **Full Parameter Reference**](PARAMETERS.md)

## Generated Files

This template generates the following files:

### Dockerfile

- `Dockerfile`

### Compose

- `docker-compose.yml`

### Config

- `entrypoint.sh`

### Docs

- `README.md`

## Examples

[📖 **Usage Examples**](EXAMPLES.md)

## Troubleshooting

[🔧 **Troubleshooting Guide**](TROUBLESHOOTING.md)

## Dependencies

### Runtime

- curl
- ca-certificates

### Test

- docker

## Supported Platforms

linux/amd64, linux/arm64, linux/arm/v7

## Testing

This template includes comprehensive testing:

### Test Commands

- `docker run --rm {{ template_name }}:latest whoami`
- `docker run --rm {{ template_name }}:latest id`

## Contributing

To modify this template:

1. Edit the template files in `templates/base/alpine/`
2. Update `template.yaml` for parameter changes
3. Test your changes: `poetry run template-engine test base/alpine`
4. Regenerate documentation: `poetry run generate-docs`

## Related Templates

Browse other templates in the same category: [**Base Templates**](../base/README.md)

---

_Documentation generated automatically from template metadata_
_Last updated: 2025-07-15 21:54:36_

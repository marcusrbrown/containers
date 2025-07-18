# {{ template_name | title }}

{{ description }}

## Overview

This is an Alpine Linux base container template generated by the Container Template Engine. It provides a secure, minimal foundation for building containerized applications.

## Features

- **Security Hardened**: Non-root user, minimal attack surface
- **Multi-Architecture**: Supports {{ platforms | join(', ') }}
- **Lightweight**: Based on Alpine Linux {{ alpine_version }}
- **Configurable**: Parameterized build with sensible defaults

## Quick Start

### Build the Container

```bash
docker build -t {{ template_name }}:latest .
```

### Run the Container

```bash
docker run --rm -it {{ template_name }}:latest
```

### Using Docker Compose

```bash
docker-compose up -d
```

## Configuration

### Build Arguments

| Argument         | Description          | Default                |
| ---------------- | -------------------- | ---------------------- |
| `ALPINE_VERSION` | Alpine Linux version | `{{ alpine_version }}` |
| `USER_NAME`      | Non-root user name   | `{{ user_name }}`      |
| `USER_UID`       | User UID             | `{{ user_uid }}`       |
| `TIMEZONE`       | System timezone      | `{{ timezone }}`       |

### Environment Variables

| Variable | Description         | Default                 |
| -------- | ------------------- | ----------------------- |
| `TZ`     | Timezone            | `{{ timezone }}`        |
| `USER`   | Current user        | `{{ user_name }}`       |
| `HOME`   | User home directory | `/home/{{ user_name }}` |

## Installed Packages

{% if packages -%}
The following packages are installed:

{% for package in packages -%}

- `{{ package }}`
  {% endfor %}
  {% endif %}

## Security Features

- Non-root user execution
- Minimal package installation
- Security updates enabled{% if enable_security_updates %} ✅{% else %} ❌{% endif %}
- Secure file permissions
- Read-only root filesystem compatible

## Health Check

The container includes a health check that runs:

```bash
{{ health_check | default('true') }}
```

## Customization

To customize this template, modify the parameters in `template.yaml` and regenerate:

```bash
poetry run template-engine generate base/alpine /path/to/output --param alpine_version=3.19
```

## License

{{ license | default('MIT') }}

---

_Generated by Container Template Engine at {{ generated_at }}_

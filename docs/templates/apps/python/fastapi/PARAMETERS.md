# Python FastAPI - Parameter Reference

Complete reference for all available parameters.

## Parameter Overview

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `alpine_version` | string | ❌ | `3.20` | Alpine Linux version |
| `packages` | array | ❌ | `['curl', 'wget', 'ca-certificates']` | Additional packages to install |
| `user_name` | string | ❌ | `appuser` | Non-root user name |
| `user_uid` | integer | ❌ | `1000` | User UID |
| `timezone` | string | ❌ | `UTC` | System timezone |
| `enable_security_updates` | boolean | ❌ | `True` | Enable automatic security updates |
| `app_name` | string | ✅ | `fastapi-app` | Application name |
| `python_version` | string | ❌ | `3.11` | Python version |
| `port` | integer | ❌ | `8000` | Application port |
| `debug` | boolean | ❌ | `False` | Enable debug mode |
| `cors_origins` | array | ❌ | `['http://localhost:3000']` | CORS allowed origins |
| `database_url` | string | ❌ | `sqlite:///./app.db` | Database connection URL |
| `secret_key` | string | ❌ | `{{ random_string(32) }}` | Application secret key |
| `enable_docs` | boolean | ❌ | `True` | Enable API documentation |
| `workers` | integer | ❌ | `1` | Number of worker processes |

## Detailed Parameter Descriptions

### `alpine_version`

- **Type**: string
- **Required**: No
- **Description**: Alpine Linux version
- **Default**: `3.20`
- **Allowed Values**: `3.18`, `3.19`, `3.20`, `latest`

### `packages`

- **Type**: array
- **Required**: No
- **Description**: Additional packages to install
- **Default**: `['curl', 'wget', 'ca-certificates']`

### `user_name`

- **Type**: string
- **Required**: No
- **Description**: Non-root user name
- **Default**: `appuser`
- **Pattern**: `^[a-z][a-z0-9_-]*$`

### `user_uid`

- **Type**: integer
- **Required**: No
- **Description**: User UID
- **Default**: `1000`
- **Minimum**: 1000
- **Maximum**: 65535

### `timezone`

- **Type**: string
- **Required**: No
- **Description**: System timezone
- **Default**: `UTC`

### `enable_security_updates`

- **Type**: boolean
- **Required**: No
- **Description**: Enable automatic security updates
- **Default**: `True`

### `app_name`

- **Type**: string
- **Required**: Yes
- **Description**: Application name
- **Default**: `fastapi-app`
- **Pattern**: `^[a-z][a-z0-9-]*[a-z0-9]$`

### `python_version`

- **Type**: string
- **Required**: No
- **Description**: Python version
- **Default**: `3.11`
- **Allowed Values**: `3.8`, `3.9`, `3.10`, `3.11`, `3.12`

### `port`

- **Type**: integer
- **Required**: No
- **Description**: Application port
- **Default**: `8000`

### `debug`

- **Type**: boolean
- **Required**: No
- **Description**: Enable debug mode
- **Default**: `False`

### `cors_origins`

- **Type**: array
- **Required**: No
- **Description**: CORS allowed origins
- **Default**: `['http://localhost:3000']`

### `database_url`

- **Type**: string
- **Required**: No
- **Description**: Database connection URL
- **Default**: `sqlite:///./app.db`

### `secret_key`

- **Type**: string
- **Required**: No
- **Description**: Application secret key
- **Default**: `{{ random_string(32) }}`

### `enable_docs`

- **Type**: boolean
- **Required**: No
- **Description**: Enable API documentation
- **Default**: `True`

### `workers`

- **Type**: integer
- **Required**: No
- **Description**: Number of worker processes
- **Default**: `1`


## Parameter Examples

### Basic Usage

```bash
poetry run template-engine generate Python FastAPI ./output \
  --param alpine_version=3.20 \
  --param packages=['curl', 'wget', 'ca-certificates'] \
  --param user_name=appuser
```

### Using Parameter File

Create a `params.json` file:

```json
{
  "alpine_version": "3.20",
  "packages": ["curl", "wget", "ca-certificates"],
  "user_name": "appuser",
  "user_uid": 1000,
  "timezone": "UTC"
}
```

Then use it:

```bash
poetry run template-engine generate template_name ./output --params params.json
```

---

*Parameter reference generated automatically from template metadata*

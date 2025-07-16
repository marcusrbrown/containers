# alpine-base - Parameter Reference

Complete reference for all available parameters.

## Parameter Overview

| Parameter                 | Type    | Required | Default                               | Description                       |
| ------------------------- | ------- | -------- | ------------------------------------- | --------------------------------- |
| `alpine_version`          | string  | ❌       | `3.20`                                | Alpine Linux version              |
| `packages`                | array   | ❌       | `['curl', 'wget', 'ca-certificates']` | Additional packages to install    |
| `user_name`               | string  | ❌       | `appuser`                             | Non-root user name                |
| `user_uid`                | integer | ❌       | `1000`                                | User UID                          |
| `timezone`                | string  | ❌       | `UTC`                                 | System timezone                   |
| `enable_security_updates` | boolean | ❌       | `True`                                | Enable automatic security updates |

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

## Parameter Examples

### Basic Usage

```bash
poetry run template-engine generate alpine-base ./output \
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

_Parameter reference generated automatically from template metadata_

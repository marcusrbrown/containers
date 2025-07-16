# nodejs-express - Parameter Reference

Complete reference for all available parameters.

## Parameter Overview

| Parameter                 | Type    | Required | Default                                        | Description                        |
| ------------------------- | ------- | -------- | ---------------------------------------------- | ---------------------------------- |
| `alpine_version`          | string  | ❌       | `3.20`                                         | Alpine Linux version               |
| `packages`                | array   | ❌       | `['curl', 'wget', 'ca-certificates']`          | Additional packages to install     |
| `user_name`               | string  | ❌       | `appuser`                                      | Non-root user name                 |
| `user_uid`                | integer | ❌       | `1000`                                         | User UID                           |
| `timezone`                | string  | ❌       | `UTC`                                          | System timezone                    |
| `enable_security_updates` | boolean | ❌       | `True`                                         | Enable automatic security updates  |
| `node_version`            | string  | ❌       | `22`                                           | Node.js version                    |
| `app_name`                | string  | ❌       | `express-app`                                  | Application name                   |
| `app_port`                | integer | ❌       | `3000`                                         | Application port                   |
| `enable_typescript`       | boolean | ❌       | `True`                                         | Enable TypeScript support          |
| `enable_hot_reload`       | boolean | ❌       | `True`                                         | Enable hot reload for development  |
| `install_packages`        | array   | ❌       | `['helmet', 'cors', 'compression', 'morgan']`  | Additional npm packages to install |
| `dev_packages`            | array   | ❌       | `['nodemon', '@types/node', '@types/express']` | Development packages to install    |

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

### `node_version`

- **Type**: string
- **Required**: No
- **Description**: Node.js version
- **Default**: `22`
- **Allowed Values**: `18`, `20`, `22`, `latest`

### `app_name`

- **Type**: string
- **Required**: No
- **Description**: Application name
- **Default**: `express-app`
- **Pattern**: `^[a-z][a-z0-9-]*$`

### `app_port`

- **Type**: integer
- **Required**: No
- **Description**: Application port
- **Default**: `3000`
- **Minimum**: 1000
- **Maximum**: 65535

### `enable_typescript`

- **Type**: boolean
- **Required**: No
- **Description**: Enable TypeScript support
- **Default**: `True`

### `enable_hot_reload`

- **Type**: boolean
- **Required**: No
- **Description**: Enable hot reload for development
- **Default**: `True`

### `install_packages`

- **Type**: array
- **Required**: No
- **Description**: Additional npm packages to install
- **Default**: `['helmet', 'cors', 'compression', 'morgan']`

### `dev_packages`

- **Type**: array
- **Required**: No
- **Description**: Development packages to install
- **Default**: `['nodemon', '@types/node', '@types/express']`

## Parameter Examples

### Basic Usage

```bash
poetry run template-engine generate nodejs-express ./output \
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

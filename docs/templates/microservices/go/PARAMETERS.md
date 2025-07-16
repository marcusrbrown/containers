# Go Microservice - Parameter Reference

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
| `service_name` | string | ✅ | `go-service` | Microservice name |
| `go_version` | string | ❌ | `1.21` | Go version |
| `http_port` | integer | ❌ | `8080` | HTTP port |
| `grpc_port` | integer | ❌ | `9090` | gRPC port |
| `metrics_port` | integer | ❌ | `9091` | Metrics port |
| `debug` | boolean | ❌ | `False` | Enable debug mode |
| `database_type` | string | ❌ | `postgres` | Database type |
| `enable_metrics` | boolean | ❌ | `True` | Enable Prometheus metrics |
| `enable_tracing` | boolean | ❌ | `True` | Enable distributed tracing |
| `log_level` | string | ❌ | `info` | Log level |

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

### `service_name`

- **Type**: string
- **Required**: Yes
- **Description**: Microservice name
- **Default**: `go-service`
- **Pattern**: `^[a-z][a-z0-9-]*[a-z0-9]$`

### `go_version`

- **Type**: string
- **Required**: No
- **Description**: Go version
- **Default**: `1.21`
- **Allowed Values**: `1.19`, `1.20`, `1.21`, `1.22`

### `http_port`

- **Type**: integer
- **Required**: No
- **Description**: HTTP port
- **Default**: `8080`

### `grpc_port`

- **Type**: integer
- **Required**: No
- **Description**: gRPC port
- **Default**: `9090`

### `metrics_port`

- **Type**: integer
- **Required**: No
- **Description**: Metrics port
- **Default**: `9091`

### `debug`

- **Type**: boolean
- **Required**: No
- **Description**: Enable debug mode
- **Default**: `False`

### `database_type`

- **Type**: string
- **Required**: No
- **Description**: Database type
- **Default**: `postgres`
- **Allowed Values**: `postgres`, `mysql`, `mongodb`, `redis`

### `enable_metrics`

- **Type**: boolean
- **Required**: No
- **Description**: Enable Prometheus metrics
- **Default**: `True`

### `enable_tracing`

- **Type**: boolean
- **Required**: No
- **Description**: Enable distributed tracing
- **Default**: `True`

### `log_level`

- **Type**: string
- **Required**: No
- **Description**: Log level
- **Default**: `info`
- **Allowed Values**: `debug`, `info`, `warn`, `error`


## Parameter Examples

### Basic Usage

```bash
poetry run template-engine generate Go Microservice ./output \
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

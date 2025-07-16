# postgresql - Parameter Reference

Complete reference for all available parameters.

## Parameter Overview

| Parameter                      | Type    | Required | Default               | Description                                   |
| ------------------------------ | ------- | -------- | --------------------- | --------------------------------------------- |
| `postgres_version`             | string  | ❌       | `16`                  | PostgreSQL version                            |
| `postgres_db`                  | string  | ❌       | `app_db`              | Default database name                         |
| `postgres_user`                | string  | ❌       | `app_user`            | Database user name                            |
| `postgres_password`            | string  | ❌       | `secure_password_123` | Database password (use secrets in production) |
| `max_connections`              | integer | ❌       | `100`                 | Maximum number of connections                 |
| `shared_buffers`               | string  | ❌       | `256MB`               | Shared buffers size                           |
| `effective_cache_size`         | string  | ❌       | `1GB`                 | Effective cache size                          |
| `maintenance_work_mem`         | string  | ❌       | `64MB`                | Maintenance work memory                       |
| `checkpoint_completion_target` | string  | ❌       | `0.9`                 | Checkpoint completion target                  |
| `wal_buffers`                  | string  | ❌       | `16MB`                | WAL buffers size                              |
| `default_statistics_target`    | integer | ❌       | `100`                 | Default statistics target                     |
| `enable_ssl`                   | boolean | ❌       | `True`                | Enable SSL connections                        |
| `enable_logging`               | boolean | ❌       | `True`                | Enable query logging                          |
| `backup_enabled`               | boolean | ❌       | `True`                | Enable automated backups                      |

## Detailed Parameter Descriptions

### `postgres_version`

- **Type**: string
- **Required**: No
- **Description**: PostgreSQL version
- **Default**: `16`
- **Allowed Values**: `13`, `14`, `15`, `16`, `latest`

### `postgres_db`

- **Type**: string
- **Required**: No
- **Description**: Default database name
- **Default**: `app_db`
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`

### `postgres_user`

- **Type**: string
- **Required**: No
- **Description**: Database user name
- **Default**: `app_user`
- **Pattern**: `^[a-zA-Z][a-zA-Z0-9_]*$`

### `postgres_password`

- **Type**: string
- **Required**: No
- **Description**: Database password (use secrets in production)
- **Default**: `secure_password_123`

### `max_connections`

- **Type**: integer
- **Required**: No
- **Description**: Maximum number of connections
- **Default**: `100`
- **Minimum**: 10
- **Maximum**: 1000

### `shared_buffers`

- **Type**: string
- **Required**: No
- **Description**: Shared buffers size
- **Default**: `256MB`

### `effective_cache_size`

- **Type**: string
- **Required**: No
- **Description**: Effective cache size
- **Default**: `1GB`

### `maintenance_work_mem`

- **Type**: string
- **Required**: No
- **Description**: Maintenance work memory
- **Default**: `64MB`

### `checkpoint_completion_target`

- **Type**: string
- **Required**: No
- **Description**: Checkpoint completion target
- **Default**: `0.9`

### `wal_buffers`

- **Type**: string
- **Required**: No
- **Description**: WAL buffers size
- **Default**: `16MB`

### `default_statistics_target`

- **Type**: integer
- **Required**: No
- **Description**: Default statistics target
- **Default**: `100`
- **Minimum**: 10
- **Maximum**: 10000

### `enable_ssl`

- **Type**: boolean
- **Required**: No
- **Description**: Enable SSL connections
- **Default**: `True`

### `enable_logging`

- **Type**: boolean
- **Required**: No
- **Description**: Enable query logging
- **Default**: `True`

### `backup_enabled`

- **Type**: boolean
- **Required**: No
- **Description**: Enable automated backups
- **Default**: `True`

## Parameter Examples

### Basic Usage

```bash
poetry run template-engine generate postgresql ./output \
  --param postgres_version=16 \
  --param postgres_db=app_db \
  --param postgres_user=app_user
```

### Using Parameter File

Create a `params.json` file:

```json
{
  "postgres_version": "16",
  "postgres_db": "app_db",
  "postgres_user": "app_user",
  "postgres_password": "secure_password_123",
  "max_connections": 100
}
```

Then use it:

```bash
poetry run template-engine generate template_name ./output --params params.json
```

---

_Parameter reference generated automatically from template metadata_

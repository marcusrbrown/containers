# redis-cache - Parameter Reference

Complete reference for all available parameters.

## Parameter Overview

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `redis_version` | string | ❌ | `7.2` | Redis version |
| `redis_port` | integer | ❌ | `6379` | Redis port |
| `redis_password` | string | ❌ | `secure_redis_password_123` | Redis authentication password |
| `max_memory` | string | ❌ | `256mb` | Maximum memory usage |
| `max_memory_policy` | string | ❌ | `allkeys-lru` | Memory eviction policy |
| `enable_persistence` | boolean | ❌ | `True` | Enable data persistence |
| `save_policy` | string | ❌ | `900 1 300 10 60 10000` | Save policy for persistence |
| `enable_aof` | boolean | ❌ | `True` | Enable Append Only File |
| `aof_rewrite_percentage` | integer | ❌ | `100` | AOF rewrite percentage |
| `enable_cluster` | boolean | ❌ | `False` | Enable Redis cluster mode |
| `cluster_announce_ip` | string | ❌ | `127.0.0.1` | Cluster announce IP |
| `log_level` | string | ❌ | `notice` | Redis log level |
| `timeout` | integer | ❌ | `300` | Client idle timeout (seconds) |
| `databases` | integer | ❌ | `16` | Number of databases |

## Detailed Parameter Descriptions

### `redis_version`

- **Type**: string
- **Required**: No
- **Description**: Redis version
- **Default**: `7.2`
- **Allowed Values**: `6.2`, `7.0`, `7.2`, `latest`

### `redis_port`

- **Type**: integer
- **Required**: No
- **Description**: Redis port
- **Default**: `6379`
- **Minimum**: 1000
- **Maximum**: 65535

### `redis_password`

- **Type**: string
- **Required**: No
- **Description**: Redis authentication password
- **Default**: `secure_redis_password_123`

### `max_memory`

- **Type**: string
- **Required**: No
- **Description**: Maximum memory usage
- **Default**: `256mb`

### `max_memory_policy`

- **Type**: string
- **Required**: No
- **Description**: Memory eviction policy
- **Default**: `allkeys-lru`
- **Allowed Values**: `noeviction`, `allkeys-lru`, `volatile-lru`, `allkeys-random`, `volatile-random`, `volatile-ttl`

### `enable_persistence`

- **Type**: boolean
- **Required**: No
- **Description**: Enable data persistence
- **Default**: `True`

### `save_policy`

- **Type**: string
- **Required**: No
- **Description**: Save policy for persistence
- **Default**: `900 1 300 10 60 10000`

### `enable_aof`

- **Type**: boolean
- **Required**: No
- **Description**: Enable Append Only File
- **Default**: `True`

### `aof_rewrite_percentage`

- **Type**: integer
- **Required**: No
- **Description**: AOF rewrite percentage
- **Default**: `100`
- **Minimum**: 1
- **Maximum**: 1000

### `enable_cluster`

- **Type**: boolean
- **Required**: No
- **Description**: Enable Redis cluster mode
- **Default**: `False`

### `cluster_announce_ip`

- **Type**: string
- **Required**: No
- **Description**: Cluster announce IP
- **Default**: `127.0.0.1`

### `log_level`

- **Type**: string
- **Required**: No
- **Description**: Redis log level
- **Default**: `notice`
- **Allowed Values**: `debug`, `verbose`, `notice`, `warning`

### `timeout`

- **Type**: integer
- **Required**: No
- **Description**: Client idle timeout (seconds)
- **Default**: `300`
- **Minimum**: 0
- **Maximum**: 3600

### `databases`

- **Type**: integer
- **Required**: No
- **Description**: Number of databases
- **Default**: `16`
- **Minimum**: 1
- **Maximum**: 16384


## Parameter Examples

### Basic Usage

```bash
poetry run template-engine generate redis-cache ./output \
  --param redis_version=7.2 \
  --param redis_port=6379 \
  --param redis_password=secure_redis_password_123
```

### Using Parameter File

Create a `params.json` file:

```json
{
  "redis_version": "7.2",
  "redis_port": 6379,
  "redis_password": "secure_redis_password_123",
  "max_memory": "256mb",
  "max_memory_policy": "allkeys-lru"
}
```

Then use it:

```bash
poetry run template-engine generate template_name ./output --params params.json
```

---

*Parameter reference generated automatically from template metadata*

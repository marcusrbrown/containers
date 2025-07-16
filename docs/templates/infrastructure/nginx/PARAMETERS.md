# nginx-proxy - Parameter Reference

Complete reference for all available parameters.

## Parameter Overview

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `nginx_version` | string | ❌ | `1.25` | nginx version |
| `server_name` | string | ❌ | `localhost` | Server name for nginx |
| `listen_port` | integer | ❌ | `80` | HTTP listen port |
| `ssl_port` | integer | ❌ | `443` | HTTPS listen port |
| `enable_ssl` | boolean | ❌ | `True` | Enable SSL/TLS support |
| `ssl_cert_path` | string | ❌ | `/etc/ssl/certs/nginx.crt` | SSL certificate path |
| `ssl_key_path` | string | ❌ | `/etc/ssl/private/nginx.key` | SSL private key path |
| `upstream_servers` | array | ❌ | `['backend1:8080', 'backend2:8080']` | Backend servers for load balancing |
| `load_balancing_method` | string | ❌ | `round_robin` | Load balancing method |
| `enable_gzip` | boolean | ❌ | `True` | Enable gzip compression |
| `enable_rate_limiting` | boolean | ❌ | `True` | Enable rate limiting |
| `rate_limit` | string | ❌ | `10r/s` | Rate limit (requests per second) |
| `enable_caching` | boolean | ❌ | `True` | Enable response caching |
| `worker_processes` | string | ❌ | `auto` | Number of worker processes |
| `worker_connections` | integer | ❌ | `1024` | Worker connections |

## Detailed Parameter Descriptions

### `nginx_version`

- **Type**: string
- **Required**: No
- **Description**: nginx version
- **Default**: `1.25`
- **Allowed Values**: `1.24`, `1.25`, `latest`

### `server_name`

- **Type**: string
- **Required**: No
- **Description**: Server name for nginx
- **Default**: `localhost`

### `listen_port`

- **Type**: integer
- **Required**: No
- **Description**: HTTP listen port
- **Default**: `80`
- **Minimum**: 1
- **Maximum**: 65535

### `ssl_port`

- **Type**: integer
- **Required**: No
- **Description**: HTTPS listen port
- **Default**: `443`
- **Minimum**: 1
- **Maximum**: 65535

### `enable_ssl`

- **Type**: boolean
- **Required**: No
- **Description**: Enable SSL/TLS support
- **Default**: `True`

### `ssl_cert_path`

- **Type**: string
- **Required**: No
- **Description**: SSL certificate path
- **Default**: `/etc/ssl/certs/nginx.crt`

### `ssl_key_path`

- **Type**: string
- **Required**: No
- **Description**: SSL private key path
- **Default**: `/etc/ssl/private/nginx.key`

### `upstream_servers`

- **Type**: array
- **Required**: No
- **Description**: Backend servers for load balancing
- **Default**: `['backend1:8080', 'backend2:8080']`

### `load_balancing_method`

- **Type**: string
- **Required**: No
- **Description**: Load balancing method
- **Default**: `round_robin`
- **Allowed Values**: `round_robin`, `least_conn`, `ip_hash`, `random`

### `enable_gzip`

- **Type**: boolean
- **Required**: No
- **Description**: Enable gzip compression
- **Default**: `True`

### `enable_rate_limiting`

- **Type**: boolean
- **Required**: No
- **Description**: Enable rate limiting
- **Default**: `True`

### `rate_limit`

- **Type**: string
- **Required**: No
- **Description**: Rate limit (requests per second)
- **Default**: `10r/s`

### `enable_caching`

- **Type**: boolean
- **Required**: No
- **Description**: Enable response caching
- **Default**: `True`

### `worker_processes`

- **Type**: string
- **Required**: No
- **Description**: Number of worker processes
- **Default**: `auto`

### `worker_connections`

- **Type**: integer
- **Required**: No
- **Description**: Worker connections
- **Default**: `1024`
- **Minimum**: 100
- **Maximum**: 10000


## Parameter Examples

### Basic Usage

```bash
poetry run template-engine generate nginx-proxy ./output \
  --param nginx_version=1.25 \
  --param server_name=localhost \
  --param listen_port=80
```

### Using Parameter File

Create a `params.json` file:

```json
{
  "nginx_version": "1.25",
  "server_name": "localhost",
  "listen_port": 80,
  "ssl_port": 443,
  "enable_ssl": true
}
```

Then use it:

```bash
poetry run template-engine generate template_name ./output --params params.json
```

---

*Parameter reference generated automatically from template metadata*

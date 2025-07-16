# redis-cache

Redis in-memory data store with persistence and security

## Overview

- **Category**: Database
- **Version**: 1.0.0
- **Author**: Container Template Engine
- **License**: MIT
- **Tags**: redis, cache, nosql, memory, session-store

## Quick Start

### Generate from Template

```bash
# Basic usage
poetry run template-engine generate databases/redis ./my-redis-cache

# With custom parameters
poetry run template-engine generate databases/redis ./my-redis-cache \
  --param param_name=value \
  --param another_param=value

# Using parameter file
poetry run template-engine generate databases/redis ./my-redis-cache \
  --params params.json
```

### Using Docker Compose

```bash
cd my-redis-cache
docker-compose up -d
```

### Manual Docker Build

```bash
cd my-redis-cache
docker build -t my-redis-cache:latest .
docker run -d --name my-redis-cache my-redis-cache:latest
```

## Parameters

### Required Parameters

None

### Optional Parameters

- `redis_version` (string): Redis version (default: `7.2`)
- `redis_port` (integer): Redis port (default: `6379`)
- `redis_password` (string): Redis authentication password (default: `secure_redis_password_123`)
- `max_memory` (string): Maximum memory usage (default: `256mb`)
- `max_memory_policy` (string): Memory eviction policy (default: `allkeys-lru`)
- `enable_persistence` (boolean): Enable data persistence (default: `True`)
- `save_policy` (string): Save policy for persistence (default: `900 1 300 10 60 10000`)
- `enable_aof` (boolean): Enable Append Only File (default: `True`)
- `aof_rewrite_percentage` (integer): AOF rewrite percentage (default: `100`)
- `enable_cluster` (boolean): Enable Redis cluster mode (default: `False`)
- `cluster_announce_ip` (string): Cluster announce IP (default: `127.0.0.1`)
- `log_level` (string): Redis log level (default: `notice`)
- `timeout` (integer): Client idle timeout (seconds) (default: `300`)
- `databases` (integer): Number of databases (default: `16`)

[📋 **Full Parameter Reference**](PARAMETERS.md)

## Generated Files

This template generates the following files:

### Dockerfile

- `Dockerfile`

### Compose

- `docker-compose.yml`

### Config

- `redis.conf`
- `sentinel.conf`

### Scripts

- `healthcheck.sh`
- `backup.sh`
- `restore.sh`

### Docs

- `README.md`
- `CLUSTERING.md`
- `BACKUP.md`

## Examples

[📖 **Usage Examples**](EXAMPLES.md)

## Troubleshooting

[🔧 **Troubleshooting Guide**](TROUBLESHOOTING.md)

## Dependencies

### Build

- redis

### Runtime

- redis
- curl

### Test

- docker
- redis-cli

## Supported Platforms

linux/amd64, linux/arm64

## Testing

This template includes comprehensive testing:

### Test Commands

- `docker run --rm -p 6379:6379 -d {{ template_name }}:latest`
- `sleep 5`
- `redis-cli ping`

### Integration Tests

- `redis-cli set test_key test_value`
- `redis-cli get test_key`

## Contributing

To modify this template:

1. Edit the template files in `templates/databases/redis/`
2. Update `template.yaml` for parameter changes
3. Test your changes: `poetry run template-engine test databases/redis`
4. Regenerate documentation: `poetry run generate-docs`

## Related Templates

Browse other templates in the same category: [**Database Templates**](../database/README.md)

---

_Documentation generated automatically from template metadata_
_Last updated: 2025-07-15 21:54:36_

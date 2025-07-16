# postgresql

PostgreSQL database server with security hardening and performance optimization

## Overview

- **Category**: Database
- **Version**: 1.0.0
- **Author**: Container Template Engine
- **License**: MIT
- **Tags**: postgresql, database, sql, postgres

## Quick Start

### Generate from Template

```bash
# Basic usage
poetry run template-engine generate databases/postgresql ./my-postgresql

# With custom parameters
poetry run template-engine generate databases/postgresql ./my-postgresql \
  --param param_name=value \
  --param another_param=value

# Using parameter file
poetry run template-engine generate databases/postgresql ./my-postgresql \
  --params params.json
```

### Using Docker Compose

```bash
cd my-postgresql
docker-compose up -d
```

### Manual Docker Build

```bash
cd my-postgresql
docker build -t my-postgresql:latest .
docker run -d --name my-postgresql my-postgresql:latest
```

## Parameters

### Required Parameters

None

### Optional Parameters

- `postgres_version` (string): PostgreSQL version (default: `16`)
- `postgres_db` (string): Default database name (default: `app_db`)
- `postgres_user` (string): Database user name (default: `app_user`)
- `postgres_password` (string): Database password (use secrets in production) (default: `secure_password_123`)
- `max_connections` (integer): Maximum number of connections (default: `100`)
- `shared_buffers` (string): Shared buffers size (default: `256MB`)
- `effective_cache_size` (string): Effective cache size (default: `1GB`)
- `maintenance_work_mem` (string): Maintenance work memory (default: `64MB`)
- `checkpoint_completion_target` (string): Checkpoint completion target (default: `0.9`)
- `wal_buffers` (string): WAL buffers size (default: `16MB`)
- `default_statistics_target` (integer): Default statistics target (default: `100`)
- `enable_ssl` (boolean): Enable SSL connections (default: `True`)
- `enable_logging` (boolean): Enable query logging (default: `True`)
- `backup_enabled` (boolean): Enable automated backups (default: `True`)

[📋 **Full Parameter Reference**](PARAMETERS.md)

## Generated Files

This template generates the following files:

### Dockerfile

- `Dockerfile`

### Compose

- `docker-compose.yml`

### Config

- `postgresql.conf`
- `pg_hba.conf`
- `init.sql`
- `backup.sh`

### Scripts

- `healthcheck.sh`
- `restore.sh`

### Docs

- `README.md`
- `BACKUP.md`
- `PERFORMANCE.md`

## Examples

[📖 **Usage Examples**](EXAMPLES.md)

## Troubleshooting

[🔧 **Troubleshooting Guide**](TROUBLESHOOTING.md)

## Dependencies

### Build

- postgresql

### Runtime

- postgresql
- curl

### Test

- docker
- psql

## Supported Platforms

linux/amd64, linux/arm64

## Testing

This template includes comprehensive testing:

### Test Commands

- `docker run --rm -e POSTGRES_PASSWORD=test_password -d {{ template_name }}:latest`
- `sleep 10`
- `docker exec container_id psql -U test_user -d test_db -c 'SELECT version();'`

### Integration Tests

- `pg_prove tests/`

## Contributing

To modify this template:

1. Edit the template files in `templates/databases/postgresql/`
2. Update `template.yaml` for parameter changes
3. Test your changes: `poetry run template-engine test databases/postgresql`
4. Regenerate documentation: `poetry run generate-docs`

## Related Templates

Browse other templates in the same category: [**Database Templates**](../database/README.md)

---

_Documentation generated automatically from template metadata_
_Last updated: 2025-07-15 21:54:36_

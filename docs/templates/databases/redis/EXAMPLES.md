# redis-cache - Usage Examples

Practical examples for using this template in different scenarios.

## Basic Example

```bash
# Generate template with defaults
poetry run template-engine generate databases/redis ./my-redis-cache

# Navigate to generated directory
cd my-redis-cache

# Build and run with Docker
docker build -t my-redis-cache:latest .
docker run -d --name my-redis-cache my-redis-cache:latest
```

## Development Example

```bash
# Generate with development settings
poetry run template-engine generate databases/redis ./my-redis-cache-dev \
  --param environment=development \
  --param debug=true

cd my-redis-cache-dev

# Use Docker Compose for development
docker-compose up -d

# View logs
docker-compose logs -f
```

## Production Example

```bash
# Generate with production optimizations
poetry run template-engine generate databases/redis ./my-redis-cache-prod \
  --param environment=production \
  --param enable_ssl=true \
  --param security_hardening=true

cd my-redis-cache-prod

# Build production image
docker build -t my-redis-cache:prod .

# Run with production settings
docker run -d \
  --name my-redis-cache-prod \
  --restart unless-stopped \
  -p 80:80 \
  -p 443:443 \
  my-redis-cache:prod
```


## Database-Specific Examples

### Data Persistence

```bash
# Create named volume for data persistence
docker volume create my-db-data

# Run with persistent storage
docker run -d \
  --name my-database \
  -v my-db-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  my-db:latest
```

### Backup and Restore

```bash
# Create backup
docker exec my-database /usr/local/bin/backup.sh

# List backups
docker exec my-database ls -la /var/lib/postgresql/backups/

# Restore from backup
docker exec my-database /usr/local/bin/restore.sh backup-2024-01-15.sql
```

### Replication Setup

```bash
# Master database
poetry run template-engine generate databases/redis ./db-master \
  --param replication_role=master \
  --param max_wal_senders=3

# Replica database
poetry run template-engine generate databases/redis ./db-replica \
  --param replication_role=replica \
  --param master_host=db-master
```

## CI/CD Integration

### GitHub Actions

```yaml
name: Build and Deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Generate from template
        run: |
          poetry install
          poetry run template-engine generate databases/redis ./app

      - name: Build Docker image
        run: |
          cd app
          docker build -t my-app:${{ github.sha }} .

      - name: Deploy
        run: |
          # Add your deployment commands here
          echo "Deploying my-app:${{ github.sha }}"
```

### GitLab CI

```yaml
stages:
  - build
  - deploy

build:
  stage: build
  script:
    - poetry install
    - poetry run template-engine generate databases/redis ./app
    - cd app
    - docker build -t my-app:$CI_COMMIT_SHA .
    - docker push my-app:$CI_COMMIT_SHA

deploy:
  stage: deploy
  script:
    - docker run -d my-app:$CI_COMMIT_SHA
  only:
    - main
```

## Testing Examples

```bash
# Validate template
poetry run template-engine validate databases/redis

# Test template generation
poetry run template-engine test databases/redis

# Test with custom parameters
poetry run template-engine test databases/redis --params test-params.json

# Run comprehensive tests
poetry run template-testing databases/redis --integration --performance
```

## Customization Examples

### Parameter File Approach

Create `custom-params.json`:

```json
{
  "app_name": "my-custom-app",
  "version": "2.0.0",
  "enable_monitoring": true,
  "custom_settings": {
    "feature_flags": ["feature_a", "feature_b"]
  }
}
```

```bash
poetry run template-engine generate databases/redis ./custom-app \
  --params custom-params.json
```

### Environment-Specific Configurations

```bash
# Development
poetry run template-engine generate databases/redis ./dev \
  --param environment=dev \
  --param debug=true \
  --param hot_reload=true

# Staging
poetry run template-engine generate databases/redis ./staging \
  --param environment=staging \
  --param monitoring=true \
  --param ssl=true

# Production
poetry run template-engine generate databases/redis ./prod \
  --param environment=prod \
  --param security_hardening=true \
  --param backup_enabled=true \
  --param monitoring=true
```

---

*Examples generated automatically for template: databases/redis*

# nodejs-express - Usage Examples

Practical examples for using this template in different scenarios.

## Basic Example

```bash
# Generate template with defaults
poetry run template-engine generate apps/nodejs/express ./my-nodejs-express

# Navigate to generated directory
cd my-nodejs-express

# Build and run with Docker
docker build -t my-nodejs-express:latest .
docker run -d --name my-nodejs-express my-nodejs-express:latest
```

## Development Example

```bash
# Generate with development settings
poetry run template-engine generate apps/nodejs/express ./my-nodejs-express-dev \
  --param environment=development \
  --param debug=true

cd my-nodejs-express-dev

# Use Docker Compose for development
docker-compose up -d

# View logs
docker-compose logs -f
```

## Production Example

```bash
# Generate with production optimizations
poetry run template-engine generate apps/nodejs/express ./my-nodejs-express-prod \
  --param environment=production \
  --param enable_ssl=true \
  --param security_hardening=true

cd my-nodejs-express-prod

# Build production image
docker build -t my-nodejs-express:prod .

# Run with production settings
docker run -d \
  --name my-nodejs-express-prod \
  --restart unless-stopped \
  -p 80:80 \
  -p 443:443 \
  my-nodejs-express:prod
```


## Application-Specific Examples

### Multi-Container Setup

```bash
# Generate app
poetry run template-engine generate apps/nodejs/express ./my-app

# Generate database
poetry run template-engine generate databases/postgresql ./my-db

# Create docker-compose.override.yml
cat > docker-compose.override.yml << EOF
version: '3.8'
services:
  app:
    depends_on:
      - db
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb

  db:
    image: my-db:latest
    environment:
      - POSTGRES_DB=mydb
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
EOF

# Start the stack
docker-compose up -d
```

### Load Balancing

```bash
# Generate multiple app instances
for i in {1..3}; do
  poetry run template-engine generate apps/nodejs/express ./app-$i \
    --param app_name=app-$i \
    --param port=$((3000 + $i))
done

# Generate nginx load balancer
poetry run template-engine generate infrastructure/nginx ./nginx \
  --param upstream_servers="app-1:3001,app-2:3002,app-3:3003"
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
          poetry run template-engine generate apps/nodejs/express ./app

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
    - poetry run template-engine generate apps/nodejs/express ./app
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
poetry run template-engine validate apps/nodejs/express

# Test template generation
poetry run template-engine test apps/nodejs/express

# Test with custom parameters
poetry run template-engine test apps/nodejs/express --params test-params.json

# Run comprehensive tests
poetry run template-testing apps/nodejs/express --integration --performance
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
poetry run template-engine generate apps/nodejs/express ./custom-app \
  --params custom-params.json
```

### Environment-Specific Configurations

```bash
# Development
poetry run template-engine generate apps/nodejs/express ./dev \
  --param environment=dev \
  --param debug=true \
  --param hot_reload=true

# Staging
poetry run template-engine generate apps/nodejs/express ./staging \
  --param environment=staging \
  --param monitoring=true \
  --param ssl=true

# Production
poetry run template-engine generate apps/nodejs/express ./prod \
  --param environment=prod \
  --param security_hardening=true \
  --param backup_enabled=true \
  --param monitoring=true
```

---

*Examples generated automatically for template: apps/nodejs/express*

# Go Microservice - Usage Examples

Practical examples for using this template in different scenarios.

## Basic Example

```bash
# Generate template with defaults
poetry run template-engine generate microservices/go ./my-Go Microservice

# Navigate to generated directory
cd my-Go Microservice

# Build and run with Docker
docker build -t my-Go Microservice:latest .
docker run -d --name my-Go Microservice my-Go Microservice:latest
```

## Development Example

```bash
# Generate with development settings
poetry run template-engine generate microservices/go ./my-Go Microservice-dev \
  --param environment=development \
  --param debug=true

cd my-Go Microservice-dev

# Use Docker Compose for development
docker-compose up -d

# View logs
docker-compose logs -f
```

## Production Example

```bash
# Generate with production optimizations
poetry run template-engine generate microservices/go ./my-Go Microservice-prod \
  --param environment=production \
  --param enable_ssl=true \
  --param security_hardening=true

cd my-Go Microservice-prod

# Build production image
docker build -t my-Go Microservice:prod .

# Run with production settings
docker run -d \
  --name my-Go Microservice-prod \
  --restart unless-stopped \
  -p 80:80 \
  -p 443:443 \
  my-Go Microservice:prod
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
          poetry run template-engine generate microservices/go ./app

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
    - poetry run template-engine generate microservices/go ./app
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
poetry run template-engine validate microservices/go

# Test template generation
poetry run template-engine test microservices/go

# Test with custom parameters
poetry run template-engine test microservices/go --params test-params.json

# Run comprehensive tests
poetry run template-testing microservices/go --integration --performance
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
poetry run template-engine generate microservices/go ./custom-app \
  --params custom-params.json
```

### Environment-Specific Configurations

```bash
# Development
poetry run template-engine generate microservices/go ./dev \
  --param environment=dev \
  --param debug=true \
  --param hot_reload=true

# Staging
poetry run template-engine generate microservices/go ./staging \
  --param environment=staging \
  --param monitoring=true \
  --param ssl=true

# Production
poetry run template-engine generate microservices/go ./prod \
  --param environment=prod \
  --param security_hardening=true \
  --param backup_enabled=true \
  --param monitoring=true
```

---

_Examples generated automatically for template: microservices/go_

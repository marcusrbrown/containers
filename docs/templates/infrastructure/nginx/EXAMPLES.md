# nginx-proxy - Usage Examples

Practical examples for using this template in different scenarios.

## Basic Example

```bash
# Generate template with defaults
poetry run template-engine generate infrastructure/nginx ./my-nginx-proxy

# Navigate to generated directory
cd my-nginx-proxy

# Build and run with Docker
docker build -t my-nginx-proxy:latest .
docker run -d --name my-nginx-proxy my-nginx-proxy:latest
```

## Development Example

```bash
# Generate with development settings
poetry run template-engine generate infrastructure/nginx ./my-nginx-proxy-dev \
  --param environment=development \
  --param debug=true

cd my-nginx-proxy-dev

# Use Docker Compose for development
docker-compose up -d

# View logs
docker-compose logs -f
```

## Production Example

```bash
# Generate with production optimizations
poetry run template-engine generate infrastructure/nginx ./my-nginx-proxy-prod \
  --param environment=production \
  --param enable_ssl=true \
  --param security_hardening=true

cd my-nginx-proxy-prod

# Build production image
docker build -t my-nginx-proxy:prod .

# Run with production settings
docker run -d \
  --name my-nginx-proxy-prod \
  --restart unless-stopped \
  -p 80:80 \
  -p 443:443 \
  my-nginx-proxy:prod
```

## Infrastructure-Specific Examples

### SSL Termination

```bash
# Generate with SSL support
poetry run template-engine generate infrastructure/nginx ./nginx-ssl \
  --param enable_ssl=true \
  --param ssl_cert_path=/etc/ssl/certs/cert.pem \
  --param ssl_key_path=/etc/ssl/private/key.pem

# Mount SSL certificates
docker run -d \
  --name nginx-ssl \
  -v /path/to/certs:/etc/ssl/certs:ro \
  -v /path/to/keys:/etc/ssl/private:ro \
  -p 80:80 -p 443:443 \
  nginx-ssl:latest
```

### High Availability

```bash
# Generate multiple instances
for i in {1..3}; do
  poetry run template-engine generate infrastructure/nginx ./nginx-$i \
    --param instance_id=$i \
    --param cluster_mode=true
done

# Use with keepalived or similar for HA
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
          poetry run template-engine generate infrastructure/nginx ./app

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
    - poetry run template-engine generate infrastructure/nginx ./app
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
poetry run template-engine validate infrastructure/nginx

# Test template generation
poetry run template-engine test infrastructure/nginx

# Test with custom parameters
poetry run template-engine test infrastructure/nginx --params test-params.json

# Run comprehensive tests
poetry run template-testing infrastructure/nginx --integration --performance
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
poetry run template-engine generate infrastructure/nginx ./custom-app \
  --params custom-params.json
```

### Environment-Specific Configurations

```bash
# Development
poetry run template-engine generate infrastructure/nginx ./dev \
  --param environment=dev \
  --param debug=true \
  --param hot_reload=true

# Staging
poetry run template-engine generate infrastructure/nginx ./staging \
  --param environment=staging \
  --param monitoring=true \
  --param ssl=true

# Production
poetry run template-engine generate infrastructure/nginx ./prod \
  --param environment=prod \
  --param security_hardening=true \
  --param backup_enabled=true \
  --param monitoring=true
```

---

_Examples generated automatically for template: infrastructure/nginx_

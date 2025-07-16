# Go Microservice

High-performance Go microservice with gRPC and REST APIs

## Overview

- **Category**: Microservice
- **Version**: 1.0.0
- **Author**: Container Template Engine
- **License**: MIT
- **Tags**: go, microservice, grpc, rest, api

## Quick Start

### Generate from Template

```bash
# Basic usage
poetry run template-engine generate microservices/go ./my-Go Microservice

# With custom parameters
poetry run template-engine generate microservices/go ./my-Go Microservice \
  --param param_name=value \
  --param another_param=value

# Using parameter file
poetry run template-engine generate microservices/go ./my-Go Microservice \
  --params params.json
```

### Using Docker Compose

```bash
cd my-Go Microservice
docker-compose up -d
```

### Manual Docker Build

```bash
cd my-Go Microservice
docker build -t my-Go Microservice:latest .
docker run -d --name my-Go Microservice my-Go Microservice:latest
```

## Parameters

### Required Parameters

- `service_name` (string): Microservice name (default: `go-service`)

### Optional Parameters

- `alpine_version` (string): Alpine Linux version (default: `3.20`)
- `packages` (array): Additional packages to install (default: `['curl', 'wget', 'ca-certificates']`)
- `user_name` (string): Non-root user name (default: `appuser`)
- `user_uid` (integer): User UID (default: `1000`)
- `timezone` (string): System timezone (default: `UTC`)
- `enable_security_updates` (boolean): Enable automatic security updates (default: `True`)
- `go_version` (string): Go version (default: `1.21`)
- `http_port` (integer): HTTP port (default: `8080`)
- `grpc_port` (integer): gRPC port (default: `9090`)
- `metrics_port` (integer): Metrics port (default: `9091`)
- `debug` (boolean): Enable debug mode (default: `False`)
- `database_type` (string): Database type (default: `postgres`)
- `enable_metrics` (boolean): Enable Prometheus metrics (default: `True`)
- `enable_tracing` (boolean): Enable distributed tracing (default: `True`)
- `log_level` (string): Log level (default: `info`)

[📋 **Full Parameter Reference**](PARAMETERS.md)

## Generated Files

This template generates the following files:

### Dockerfile

- `Dockerfile`

### Compose

- `docker-compose.yml`

### Config

- `go.mod`
- `go.sum`
- `main.go`
- `config.go`

### Docs

- `README.md`
- `api.md`

### Scripts

- `entrypoint.sh`
- `health.sh`

### Proto

- `proto/service.proto`

### Tests

- `main_test.go`
- `integration_test.go`

## Examples

[📖 **Usage Examples**](EXAMPLES.md)

## Troubleshooting

[🔧 **Troubleshooting Guide**](TROUBLESHOOTING.md)

## Dependencies

### Build

- golang:{{ go_version }}-alpine
- protoc
- protoc-gen-go
- protoc-gen-go-grpc

### Runtime

- github.com/gin-gonic/gin
- google.golang.org/grpc
- github.com/prometheus/client_golang
- go.opentelemetry.io/otel
- github.com/spf13/viper

### Test

- github.com/stretchr/testify
- github.com/golang/mock

## Supported Platforms

linux/amd64, linux/arm64

## Testing

This template includes comprehensive testing:

### Test Commands

- `go test -v ./...`
- `go vet ./...`
- `go run -race .`

## Contributing

To modify this template:

1. Edit the template files in `templates/microservices/go/`
2. Update `template.yaml` for parameter changes
3. Test your changes: `poetry run template-engine test microservices/go`
4. Regenerate documentation: `poetry run generate-docs`

## Related Templates

Browse other templates in the same category: [**Microservice Templates**](../microservice/README.md)

---

_Documentation generated automatically from template metadata_
_Last updated: 2025-07-15 21:54:36_

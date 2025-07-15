# Node.js Container Collection

This directory contains Node.js container variants for testing the automation framework.

## Available Variants

### 1. Release (`/node/release/`)

- **Base Image**: `node:22-bookworm-slim` (Debian Bookworm)
- **Size**: ~160MB
- **Features**: Full Debian environment with comprehensive tools
- **Use Case**: Production environments requiring full compatibility

### 2. Alpine (`/node/alpine/`)

- **Base Image**: `node:22-alpine`
- **Size**: ~70MB (significantly smaller)
- **Features**: Minimal Alpine Linux environment
- **Use Case**: Production environments optimizing for size

## Application Features

Both variants include a simple Express.js application with:

- **Health Check Endpoint**: `GET /health`
- **System Info Endpoint**: `GET /info`
- **Root Endpoint**: `GET /`
- **Graceful Shutdown**: Handles SIGTERM and SIGINT signals
- **Security**: Runs as non-root user
- **Multi-Architecture**: Supports AMD64, ARM64, and ARM platforms

## Testing the Containers

### Local Build and Test

```bash
# Build the release variant
docker build -t node-test:release node/release/

# Build the Alpine variant
docker build -t node-test:alpine node/alpine/

# Run the container
docker run -p 3000:3000 node-test:release

# Test the endpoints
curl http://localhost:3000/health
curl http://localhost:3000/info
```

### Multi-Architecture Build

```bash
# Build for multiple platforms
docker buildx build --platform linux/amd64,linux/arm64 -t node-test:multi node/release/
```

## Automation Framework Validation

These containers are designed to validate the automation framework capabilities:

✅ **Multi-Architecture Support**: Both AMD64 and ARM64
✅ **Security Best Practices**: Non-root user, minimal dependencies
✅ **Health Checks**: Built-in health monitoring
✅ **Proper Labeling**: OCI-compliant metadata
✅ **Layer Optimization**: Efficient caching strategies
✅ **Base Image Pinning**: SHA256 hash verification

## CI/CD Integration

The containers will automatically trigger builds when:

- Dockerfiles are modified
- Application code is updated
- Manual workflow dispatch is triggered

Expected build outputs:

- `ghcr.io/marcusrbrown/node-release:latest`
- `ghcr.io/marcusrbrown/node-alpine:latest`
- `marcusrbrown/node-release:latest` (Docker Hub)
- `marcusrbrown/node-alpine:latest` (Docker Hub)

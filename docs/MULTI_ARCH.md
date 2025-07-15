# Multi-Architecture Container Build Support

This document provides comprehensive guidance for building, managing, and deploying multi-architecture containers in this repository.

## Table of Contents

1. [Overview](#overview)
2. [Supported Platforms](#supported-platforms)
3. [Quick Start](#quick-start)
4. [GitHub Actions Workflows](#github-actions-workflows)
5. [Local Development](#local-development)
6. [Dockerfile Best Practices](#dockerfile-best-practices)
7. [Build Scripts](#build-scripts)
8. [Registry Management](#registry-management)
9. [Troubleshooting](#troubleshooting)
10. [Contributing](#contributing)

## Overview

This repository supports building container images for multiple architectures, enabling deployment across diverse hardware platforms including:

- **AMD64/x86_64**: Traditional servers, desktops, and cloud instances
- **ARM64/AArch64**: Apple Silicon, AWS Graviton, and modern ARM servers
- **ARMv7**: Raspberry Pi and embedded devices

All containers are built using Docker Buildx with cross-compilation support and platform-specific optimizations.

## Supported Platforms

| Platform       | Architecture | Support Level   | Notes                          |
| -------------- | ------------ | --------------- | ------------------------------ |
| `linux/amd64`  | x86_64       | ✅ Full         | Primary development platform   |
| `linux/arm64`  | AArch64      | ✅ Full         | Apple Silicon, AWS Graviton    |
| `linux/arm/v7` | ARMv7        | ⚠️ Experimental | Raspberry Pi, embedded systems |
| `linux/arm/v6` | ARMv6        | ⚠️ Limited      | Older Raspberry Pi models      |
| `linux/386`    | i386         | ⚠️ Limited      | Legacy 32-bit x86 systems      |

## Quick Start

### Building a Single Container

```bash
# Build for multiple architectures
python3 scripts/build_multiarch.py build \
  --dockerfile ./parity/release/Dockerfile \
  --context ./parity/release \
  --image ghcr.io/marcusrbrown/parity-release:latest \
  --platforms linux/amd64,linux/arm64 \
  --push

# Build for local testing (single platform)
python3 scripts/build_multiarch.py build \
  --dockerfile ./parity/release/Dockerfile \
  --context ./parity/release \
  --image parity-release:test \
  --platforms linux/amd64
```

### Building All Containers

```bash
# Build all containers in the repository
python3 scripts/build_multiarch.py build-all \
  --directory . \
  --registry ghcr.io \
  --namespace marcusrbrown \
  --platforms linux/amd64,linux/arm64 \
  --push \
  --report build-report.json
```

### Generating Multi-Arch Dockerfiles

```bash
# Generate a new multi-arch Dockerfile
python3 scripts/generate_dockerfile.py \
  --base-image ubuntu:22.04 \
  --packages "curl git build-essential" \
  --platforms linux/amd64,linux/arm64 \
  --build-type production \
  --output-dir ./new-container
```

## GitHub Actions Workflows

### Automatic Multi-Arch Builds

The repository includes a comprehensive GitHub Actions workflow that automatically builds multi-architecture containers when Dockerfiles are modified.

#### Workflow Features

- **Platform Detection**: Automatically detects changed containers
- **Matrix Builds**: Parallel builds for multiple platforms
- **Registry Support**: Pushes to GitHub Container Registry and Docker Hub
- **Caching**: Optimized build caching for faster builds
- **Security**: Vulnerability scanning and security best practices

#### Workflow Configuration

```yaml
# Trigger builds on Dockerfile changes
on:
  push:
    paths:
      - "**/Dockerfile"
      - "scripts/**"

# Manual workflow dispatch with custom options
workflow_dispatch:
  inputs:
    platforms:
      description: "Platforms to build for"
      default: "linux/amd64,linux/arm64"
    push_images:
      description: "Push images to registry"
      default: true
```

#### Environment Variables

Configure the following secrets in your repository:

```bash
# GitHub Container Registry (automatic)
GITHUB_TOKEN  # Automatically provided by GitHub

# Docker Hub (optional)
DOCKERHUB_USERNAME  # Your Docker Hub username
DOCKERHUB_TOKEN     # Docker Hub access token
```

## Local Development

### Prerequisites

```bash
# Install Docker with Buildx support
docker version  # >= 20.10.0
docker buildx version

# Install QEMU for cross-platform emulation
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes

# Verify platform support
docker buildx ls
```

### Setting Up Local Environment

```bash
# Clone the repository
git clone https://github.com/marcusrbrown/containers.git
cd containers

# Set up buildx builder
python3 scripts/build_multiarch.py setup --builder-name local-multiarch

# Verify setup
docker buildx inspect local-multiarch
```

### Development Workflow

1. **Create/Modify Dockerfile**: Follow multi-arch best practices
2. **Local Testing**: Build for your platform first
3. **Multi-Arch Testing**: Build for target platforms
4. **Push Changes**: Automatic CI/CD will handle production builds

```bash
# Test locally first
docker build -t test-image .

# Test multi-arch build
python3 scripts/build_multiarch.py build \
  --dockerfile ./Dockerfile \
  --context . \
  --image test-image:multiarch \
  --platforms linux/amd64,linux/arm64

# Inspect the result
python3 scripts/build_multiarch.py inspect --image test-image:multiarch
```

## Dockerfile Best Practices

### Multi-Arch Dockerfile Template

```dockerfile
# syntax=docker/dockerfile:1.4
FROM --platform=$TARGETPLATFORM ubuntu:22.04

# Multi-architecture build arguments
ARG TARGETPLATFORM
ARG TARGETOS
ARG TARGETARCH
ARG BUILDPLATFORM

# Platform-specific optimizations
RUN case "$TARGETARCH" in \
      "amd64") echo "Optimizing for AMD64" ;; \
      "arm64") echo "Optimizing for ARM64" ;; \
      "arm") echo "Optimizing for ARMv7" ;; \
      *) echo "Unknown architecture: $TARGETARCH" >&2; exit 1 ;; \
    esac

# Use BuildKit cache mounts for better performance
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends \
      build-essential \
      curl \
      git && \
    rm -rf /var/lib/apt/lists/*

# Cross-compilation environment variables
ENV GOOS=linux
ENV GOARCH=$TARGETARCH

# Security best practices
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser

# Metadata labels
LABEL org.opencontainers.image.title="Multi-Arch Example" \
      org.opencontainers.image.description="Example multi-architecture container" \
      org.opencontainers.image.source="https://github.com/marcusrbrown/containers"
```

### Platform-Specific Optimizations

#### ARM64 Optimizations

```dockerfile
# ARM64-specific package installations
RUN case "$TARGETARCH" in \
      "arm64") \
        # ARM64-specific optimizations
        export ARM64_OPTIMIZATIONS=1; \
        echo 'export CFLAGS="-march=armv8-a -mtune=cortex-a72"' >> ~/.bashrc; \
        ;; \
    esac
```

#### Cross-Compilation Support

```dockerfile
# Rust cross-compilation
ENV CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=aarch64-linux-gnu-gcc
ENV CARGO_TARGET_ARMV7_UNKNOWN_LINUX_GNUEABIHF_LINKER=arm-linux-gnueabihf-gcc

# Go cross-compilation
ENV GOOS=linux
ENV GOARCH=$TARGETARCH
```

## Build Scripts

### `build_multiarch.py`

Comprehensive multi-architecture build utility with advanced features:

```bash
# Available commands
python3 scripts/build_multiarch.py --help

# Setup buildx environment
python3 scripts/build_multiarch.py setup

# Build single container
python3 scripts/build_multiarch.py build \
  --dockerfile path/to/Dockerfile \
  --context path/to/context \
  --image registry/namespace/name:tag \
  --platforms linux/amd64,linux/arm64

# Build all containers
python3 scripts/build_multiarch.py build-all \
  --directory ./containers \
  --registry ghcr.io \
  --namespace username \
  --platforms linux/amd64,linux/arm64 \
  --push

# Inspect multi-arch image
python3 scripts/build_multiarch.py inspect --image image:tag
```

### `generate_dockerfile.py`

Enhanced Dockerfile generation with platform-specific optimizations:

```bash
# Generate multi-arch Dockerfile
python3 scripts/generate_dockerfile.py \
  --base-image ubuntu:22.04 \
  --packages "build-essential curl git" \
  --platforms linux/amd64,linux/arm64 \
  --build-type production \
  --output-dir ./new-container

# Available build types
# - production: Optimized for production use
# - development: Includes debugging tools
# - minimal: Minimal footprint
```

## Registry Management

### Supported Registries

- **GitHub Container Registry (GHCR)**: `ghcr.io/username/image`
- **Docker Hub**: `docker.io/username/image`
- **AWS Elastic Container Registry (ECR)**: `aws-account-id.dkr.ecr.region.amazonaws.com/image`
- **Azure Container Registry (ACR)**: `registry.azurecr.io/image`

### Authentication

```bash
# GitHub Container Registry
echo $GITHUB_TOKEN | docker login ghcr.io -u username --password-stdin

# Docker Hub
echo $DOCKERHUB_TOKEN | docker login docker.io -u username --password-stdin

# AWS ECR
aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws-account-id.dkr.ecr.region.amazonaws.com

# Azure ACR
az acr login --name myregistry
```

### Tagging Strategy

```bash
# Recommended tagging strategy for multi-arch images
registry/namespace/image:latest          # Latest stable release
registry/namespace/image:v1.2.3          # Specific version
registry/namespace/image:main            # Main branch build
registry/namespace/image:main-abc123     # Main branch with commit SHA
```

## Troubleshooting

### Common Issues

#### 1. QEMU Emulation Performance

**Problem**: ARM builds are slow on AMD64 hosts

**Solution**: Use native ARM64 runners or optimize build steps

```yaml
# Use GitHub ARM64 runners
runs-on: ubuntu-latest-arm64 # If available
```

#### 2. Cross-Compilation Errors

**Problem**: Native compilation fails for target architecture

**Solution**: Install cross-compilation toolchains

```dockerfile
# Install cross-compilation tools
RUN case "$TARGETARCH" in \
      "arm64") apt-get install -y gcc-aarch64-linux-gnu ;; \
      "arm") apt-get install -y gcc-arm-linux-gnueabihf ;; \
    esac
```

#### 3. Platform-Specific Dependencies

**Problem**: Packages not available for target architecture

**Solution**: Use platform-specific package sources

```dockerfile
# Add architecture-specific repositories
RUN case "$TARGETARCH" in \
      "arm64") \
        echo "deb [arch=arm64] http://ports.ubuntu.com/ubuntu-ports jammy main" >> /etc/apt/sources.list; \
        ;; \
    esac
```

#### 4. BuildKit Cache Issues

**Problem**: Cache not working correctly for multi-arch builds

**Solution**: Use proper cache configuration

```bash
# Clear BuildKit cache
docker buildx prune --all

# Use registry cache
docker buildx build \
  --cache-from type=registry,ref=registry/namespace/image:cache \
  --cache-to type=registry,ref=registry/namespace/image:cache,mode=max
```

### Debugging Multi-Arch Builds

```bash
# Inspect buildx builder
docker buildx inspect

# Check supported platforms
docker buildx ls

# Debug specific platform
docker buildx build --platform linux/arm64 --load .
docker run --rm -it --platform linux/arm64 image:tag /bin/bash

# View build logs
docker buildx build --progress=plain .
```

### Performance Optimization

#### Build Speed Optimization

```dockerfile
# Use cache mounts
RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt \
    --mount=type=cache,target=/root/.cache/pip \
    apt-get update && \
    apt-get install -y python3-pip && \
    pip install package
```

#### Image Size Optimization

```dockerfile
# Multi-stage builds for smaller images
FROM --platform=$TARGETPLATFORM golang:1.19 AS builder
COPY . .
RUN CGO_ENABLED=0 go build -o app

FROM --platform=$TARGETPLATFORM alpine:latest
COPY --from=builder /app /usr/local/bin/app
CMD ["app"]
```

## Contributing

### Adding New Containers

1. Create directory structure:

   ```
   new-container/
   ├── Dockerfile
   ├── README.md
   └── .build-info.json
   ```

2. Use multi-arch Dockerfile template
3. Test locally before submitting PR
4. Update documentation

### Guidelines

- Always use `--platform=$TARGETPLATFORM` in FROM statements
- Include platform-specific optimizations when beneficial
- Add proper labels and metadata
- Test on multiple architectures
- Update documentation for new features

### Testing

```bash
# Test single platform
make test-amd64

# Test multi-platform
make test-multiarch

# Integration tests
make test-integration
```

## Examples

### Example 1: Node.js Application

```dockerfile
# syntax=docker/dockerfile:1.4
FROM --platform=$TARGETPLATFORM node:18-alpine

ARG TARGETPLATFORM
ARG TARGETARCH

# Install platform-specific packages
RUN case "$TARGETARCH" in \
      "arm64") apk add --no-cache python3 make g++ ;; \
      "amd64") apk add --no-cache python3 make g++ ;; \
    esac

WORKDIR /app
COPY package*.json ./

# Use cache mount for npm
RUN --mount=type=cache,target=/root/.npm \
    npm ci --only=production

COPY . .
USER node
CMD ["npm", "start"]
```

### Example 2: Go Application with Cross-Compilation

```dockerfile
# syntax=docker/dockerfile:1.4
FROM --platform=$BUILDPLATFORM golang:1.19 AS builder

ARG TARGETPLATFORM
ARG TARGETOS
ARG TARGETARCH

WORKDIR /src
COPY go.mod go.sum ./
RUN --mount=type=cache,target=/go/pkg/mod \
    go mod download

COPY . .
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    CGO_ENABLED=0 GOOS=$TARGETOS GOARCH=$TARGETARCH \
    go build -o /out/app .

FROM --platform=$TARGETPLATFORM alpine:latest
RUN apk add --no-cache ca-certificates
COPY --from=builder /out/app /usr/local/bin/app
CMD ["app"]
```

### Example 3: Python Application

```dockerfile
# syntax=docker/dockerfile:1.4
FROM --platform=$TARGETPLATFORM python:3.11-slim

ARG TARGETARCH

# Install platform-specific build tools
RUN case "$TARGETARCH" in \
      "arm64") apt-get update && apt-get install -y gcc g++ ;; \
      "arm") apt-get update && apt-get install -y gcc g++ ;; \
    esac && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .

# Use cache mount for pip
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-deps -r requirements.txt

COPY . .
USER 1000
CMD ["python", "app.py"]
```

## Resources

- [Docker Buildx Documentation](https://docs.docker.com/buildx/)
- [Docker Multi-Platform Images](https://docs.docker.com/docker-for-mac/multi-arch/)
- [GitHub Actions Docker Build and Push](https://github.com/docker/build-push-action)
- [QEMU User Emulation](https://github.com/multiarch/qemu-user-static)

## License

This documentation and associated scripts are available under the same license as the repository.

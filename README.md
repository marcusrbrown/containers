# Container Collection & Automation Framework

> A comprehensive collection of Dockerfiles with advanced automation tools for multi-architecture container builds, metrics collection, and CI/CD workflows.

[![GitHub Actions](https://img.shields.io/github/actions/workflow/status/marcusrbrown/containers/build-publish.yaml?branch=main&label=build&style=for-the-badge)](https://github.com/marcusrbrown/containers/actions)
[![License](https://img.shields.io/github/license/marcusrbrown/containers?style=for-the-badge)](LICENSE.md)
[![Python](https://img.shields.io/badge/python-3.13.4-blue.svg?style=for-the-badge)](https://python.org)
[![Poetry](https://img.shields.io/badge/dependency%20management-poetry-blue.svg?style=for-the-badge)](https://python-poetry.org)

## Overview

This repository provides a comprehensive container development ecosystem featuring:

- **Container Collection**: Curated Dockerfiles for Node.js applications and archived Ethereum Parity client
- **Automation Framework**: Python scripts for dynamic Dockerfile generation, metrics collection, and image tagging
- **Multi-Architecture Support**: ARM64 and AMD64 builds with platform-specific optimizations
- **CI/CD Integration**: GitHub Actions workflows for building, testing, vulnerability scanning, and publishing
- **Development Environment**: Docker-in-Docker devcontainer setup with mise tool management

## ✨ Features

- **🐳 Dynamic Dockerfile Generation**: Multi-architecture support with customizable base images and packages
- **📊 Container Metrics Collection**: Build time, image size, and registry usage analytics
- **🏷️ Intelligent Image Tagging**: Metadata-based tagging with semantic versioning
- **🔒 Security Integration**: Automated vulnerability scanning with Trivy
- **⚡ Modern Tooling**: Poetry, mise, pre-commit hooks, and automated dependency updates
- **🚀 CI/CD Workflows**: Comprehensive GitHub Actions for container lifecycle management

## 📦 Available Containers

### Node.js Applications

**[`node/`](node/)** - Production-ready Node.js container variants:

- **[`node/release/`](node/release/)**: Debian Bookworm-based (~160MB) - Full compatibility for production
- **[`node/alpine/`](node/alpine/)**: Alpine Linux-based (~70MB) - Optimized for size

### Archived Containers

**[`archived/parity/`](archived/parity/)** - Ethereum Parity client containers:

- **`branch/`**: Development builds from Git branches
- **`release/`**: Stable production releases

## 🚀 Quick Start

### Prerequisites

- [mise](https://mise.jdx.dev/) - Polyglot tool version manager
- [Docker](https://docker.com/) - Container platform

### Environment Setup

```bash
# Clone the repository
git clone https://github.com/marcusrbrown/containers.git
cd containers

# Install development tools with mise
mise install

# Install Python dependencies
poetry install

# Install Node.js dependencies
pnpm install

# Setup pre-commit hooks
pre-commit install
```

### Build a Container

```bash
# Build Node.js Alpine variant
docker build -t my-node-app:alpine node/alpine/

# Build Node.js release variant
docker build -t my-node-app:release node/release/
```

## 🛠️ Automation Scripts

This repository includes three powerful Python scripts accessible via Poetry:

### Generate Dockerfiles

Create customized Dockerfiles with multi-architecture support:

```bash
# Generate a basic Dockerfile
poetry run generate-dockerfile --base-image debian:bullseye-slim --packages "curl wget python3"

# Multi-architecture with environment variables
poetry run generate-dockerfile \
  --base-image alpine:3.18 \
  --packages "nodejs npm" \
  --env "NODE_ENV=production PORT=3000" \
  --architecture "linux/amd64,linux/arm64"

# Extend existing Dockerfile
poetry run generate-dockerfile --existing-dockerfile ./node/alpine/Dockerfile --packages "git"
```

### Collect Container Metrics

Gather build performance and image analytics:

```bash
# Collect metrics for all containers
poetry run collect-docker-metrics

# Collect metrics for specific registry
poetry run collect-docker-metrics --registry github

# View collected metrics
cat collected_metrics.yaml
```

### Generate Image Tags

Create semantic tags based on container metadata:

```bash
# Generate tags for all containers
poetry run generate-image-tags

# View generated tags
cat generated_tags.json
```

## 🔧 Development Environment

### Local Development

```bash
# Activate development environment
mise shell

# Run linting and formatting
pre-commit run --all-files

# Run specific script during development
poetry run python scripts/generate_dockerfile.py --help
```

### VS Code DevContainer

Open the repository in VS Code and use the **"Reopen in Container"** command for a complete Docker-in-Docker development environment with all tools pre-configured.

## ⚙️ CI/CD Workflows

This repository includes comprehensive GitHub Actions workflows:

- **[`build-publish.yaml`](.github/workflows/build-publish.yaml)**: Multi-architecture container builds and registry publishing
- **[`container-scan.yaml`](.github/workflows/container-scan.yaml)**: Security vulnerability scanning with Trivy
- **[`dockerfile_generation.yaml`](.github/workflows/dockerfile_generation.yaml)**: Automated Dockerfile generation
- **[`metrics_collector.yaml`](.github/workflows/metrics_collector.yaml)**: Performance metrics collection
- **[`test.yaml`](.github/workflows/test.yaml)**: Container testing and validation

## 📚 Project Structure

```text
├── node/                     # Node.js container variants
│   ├── alpine/              # Alpine-based builds
│   └── release/             # Debian-based builds
├── archived/                # Legacy container definitions
│   └── parity/             # Ethereum Parity client
├── scripts/                 # Automation tools
│   ├── generate_dockerfile.py
│   ├── collect_docker_metrics.py
│   └── generate_image_tags.py
├── .devcontainer/          # VS Code development environment
├── .github/workflows/      # CI/CD automation
└── docs/                   # Documentation
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests and linting (`pre-commit run --all-files`)
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📄 License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.

## 🔗 Links

- [GitHub Repository](https://github.com/marcusrbrown/containers)
- [GitHub Actions](https://github.com/marcusrbrown/containers/actions)
- [Issues](https://github.com/marcusrbrown/containers/issues)
- [Pull Requests](https://github.com/marcusrbrown/containers/pulls)

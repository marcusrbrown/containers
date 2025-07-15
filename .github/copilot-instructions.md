# Container Collection - GitHub Copilot Instructions

## Project Overview

This is the **marcusrbrown/containers** repository - a comprehensive collection of Dockerfiles, container automation tools, and CI/CD workflows designed for efficient container management and distribution with advanced multi-architecture support.

### Key Features

- **Container Collection**: Curated Dockerfiles for Node.js applications and archived Ethereum Parity client
- **Multi-Architecture Build System**: Advanced ARM64/AMD64 builds with platform-specific optimizations via Docker Buildx
- **Automated Generation**: Python scripts for dynamic Dockerfile creation, metrics collection, and intelligent tagging
- **CI/CD Integration**: Sophisticated GitHub Actions workflows with conditional building, security scanning, and registry publishing
- **Development Environment**: Docker-in-Docker devcontainer setup with mise tool management for consistent environments

### Tech Stack

- **Python 3.13.4**: Primary automation language with Poetry for dependency management
- **Node.js 22.17.0/pnpm**: JavaScript tooling and formatting with Prettier
- **Docker + Buildx**: Multi-architecture container platform with advanced caching and manifest creation
- **mise**: Polyglot tool version manager for consistent development environments
- **GitHub Actions**: CI/CD automation with matrix builds and security scanning
- **Trivy**: Container vulnerability scanning integrated into workflows

## Project Architecture

### Critical Directory Structure

#### Active Container Definitions

- **`node/`**: Production-ready Node.js container variants
  - **`alpine/`**: Alpine Linux-based (~70MB) - Size-optimized builds
  - **`release/`**: Debian Bookworm-based (~160MB) - Full compatibility
- **`archived/parity/`**: Legacy Ethereum Parity client containers (excluded from CI/CD)

#### Automation Scripts (`scripts/`)

- **`generate_dockerfile.py`**: Dynamic Dockerfile generation with multi-arch platform support and package managers
- **`collect_docker_metrics.py`**: Build performance and image size metrics with registry analytics
- **`generate_image_tags.py`**: Automated Docker image tagging based on metadata extraction
- **`build_multiarch.py`**: **[NEW]** Advanced multi-architecture build utility with buildx management

#### Critical Configuration Files

- **`pyproject.toml`**: Poetry configuration with script entry points (`generate-dockerfile`, `collect-docker-metrics`, `generate-image-tags`)
- **`.mise.toml`**: Tool version management with automatic Poetry venv creation
- **`.github/workflows/build-publish.yaml`**: **[CORE]** Smart container detection and multi-arch CI/CD pipeline

## Essential Workflows & Patterns

### Container Build Detection Logic

The CI/CD system uses intelligent detection in `build-publish.yaml`:

```yaml
# Detects changed Dockerfiles but excludes archived/system containers
changed_files=$(git diff --name-only | grep "Dockerfile$" | grep -v -E "(archived/|\.devcontainer/|\.github/)")
```

### Multi-Architecture Build Commands

```bash
# Local multi-arch builds using the build utility
python3 scripts/build_multiarch.py build \
  --dockerfile ./node/alpine/Dockerfile \
  --context ./node/alpine \
  --image myapp:latest \
  --platforms linux/amd64,linux/arm64

# Build all containers in directory
python3 scripts/build_multiarch.py build-all \
  --directory ./node \
  --registry ghcr.io \
  --namespace username \
  --platforms linux/amd64,linux/arm64 \
  --push
```

### Development Environment Setup Pattern

```bash
# Critical: mise manages ALL tools - never use direct pip/npm
mise install              # Installs Python 3.13.4, Node.js 22.17.0, Poetry, pnpm
poetry install           # Installs Python dependencies in auto-created venv
pnpm install            # Installs Node.js tooling (Prettier, etc.)
pre-commit install      # Sets up automated code quality hooks
```

### Script Usage Patterns (via Poetry)

```bash
# Dockerfile generation with platform-aware package management
poetry run generate-dockerfile \
  --base-image alpine:3.18 \
  --packages "nodejs npm git" \
  --env "NODE_ENV=production" \
  --architecture "linux/amd64,linux/arm64"

# Registry metrics collection
poetry run collect-docker-metrics --registry github

# Tag generation from container metadata
poetry run generate-image-tags
```

## Critical Integration Points

### CI/CD Matrix Build System

The `build-publish.yaml` workflow creates dynamic matrices:

- **Container Detection**: Scans for changed Dockerfiles, excluding archived/system containers
- **Image Naming**: Uses directory structure (`parent-dir-container-name` format)
- **Platform Building**: Defaults to `linux/amd64,linux/arm64` with manual override support
- **Registry Publishing**: Dual-publishes to GitHub Container Registry and Docker Hub

### Security & Compliance Integration

- **Trivy Scanning**: Automated vulnerability scanning in `container-scan.yaml`
- **SARIF Reports**: Security findings integrated into GitHub Security tab
- **Hash Pinning**: All GitHub Actions use SHA256 hashes for security
- **Secret Management**: Supports DOCKERHUB_TOKEN and automatic GITHUB_TOKEN

### Development Environment Dependencies

- **mise Integration**: ALL tool management goes through mise - never install tools directly
- **Poetry Scripts**: Use `poetry run <script-name>` - scripts are defined as entry points in pyproject.toml
- **Pre-commit Hooks**: Automatic formatting (Black, Prettier) and linting (yamllint)
- **VS Code DevContainer**: Provides Docker-in-Docker with all tools pre-configured

## Key Code Patterns

### Multi-Architecture Dockerfile Patterns

```dockerfile
# Platform-aware builds with BuildKit
FROM --platform=$TARGETPLATFORM node:18-alpine
ARG TARGETARCH

# Platform-specific package installation
RUN case "$TARGETARCH" in \
      "arm64") apk add --no-cache python3 make g++ ;; \
      "amd64") apk add --no-cache python3 make g++ ;; \
    esac
```

### Build Script Error Handling

```python
# Standard pattern from build_multiarch.py
def run_command(self, cmd: List[str], capture_output: bool = False) -> subprocess.CompletedProcess:
    """Run shell command with error handling."""
    try:
        result = subprocess.run(cmd, capture_output=capture_output, text=True, check=True)
        return result
    except subprocess.CalledProcessError as e:
        self.log(f"Command failed: {' '.join(cmd)}", "ERROR")
        if capture_output:
            self.log(f"Error output: {e.stderr}", "ERROR")
        raise
```

### Container Registry Publishing Pattern

```yaml
# GitHub Actions pattern for multi-registry publishing
images: |
  ${{ env.REGISTRY_GHCR }}/${{ github.repository_owner }}/${{ matrix.image }}
  ${{ env.DOCKERHUB_USERNAME }}/${{ matrix.image }}
tags: |
  type=ref,event=branch
  type=sha,format=short,prefix={{branch}}-,enable={{is_default_branch}}
  type=raw,value=latest,enable={{is_default_branch}}
```

## Project-Specific Conventions

### Container Naming Strategy

- **Directory Structure**: `category/variant/` (e.g., `node/alpine/`, `node/release/`)
- **Image Names**: `category-variant` format in CI/CD (e.g., `node-alpine`, `node-release`)
- **Registry Paths**: `ghcr.io/marcusrbrown/IMAGE` and `marcusrbrown/IMAGE`

### Exclusion Patterns

- **Archived Containers**: `archived/` directory excluded from CI/CD builds
- **System Containers**: `.devcontainer/`, `.github/` excluded from automatic builds
- **Development Files**: Build scripts ignore test/development Dockerfiles

### Build Optimization Strategies

- **Cache Mounts**: Leverage BuildKit cache mounts for package installations
- **Multi-stage Builds**: Separate build and runtime stages for smaller images
- **Platform Detection**: Use `$TARGETPLATFORM` and `$TARGETARCH` for conditional builds

## Security Best Practices

### Action Security Patterns

```yaml
# Always pin actions with SHA256 hashes
- uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2
- uses: docker/setup-buildx-action@18ce135bb5112fa8ce4ed6c17ab05699d7f3a5e0 # v3.11.0
```

### Dockerfile Security Patterns

```dockerfile
# Create non-root user for security
RUN useradd --create-home --shell /bin/bash appuser
USER appuser

# Pin base images with SHA256 hashes (when available)
FROM debian:bullseye-slim@sha256:...
```

This repository serves as a sophisticated container development platform with emphasis on automation, security, and multi-architecture support. Understanding the integration between mise, Poetry, GitHub Actions, and Docker Buildx is crucial for effective development.

#### Automation Scripts (`scripts/`)

- **`generate_dockerfile.py`**: Dynamic Dockerfile generation with customizable base images and packages
- **`collect_docker_metrics.py`**: Build performance and image size metrics collection
- **`generate_image_tags.py`**: Automated Docker image tagging based on metadata

#### Build & Configuration

- **`pyproject.toml`**: Python project configuration with Poetry dependency management
- **`package.json`**: Node.js tooling configuration with Prettier formatting
- **`.mise.toml`**: Development environment tool versions and configuration
- **`.pre-commit-config.yaml`**: Code quality hooks and automated checks

#### CI/CD Workflows (`.github/workflows/`)

- **`build-publish.yaml`**: Container build and registry publishing pipeline
- **`container-scan.yaml`**: Security vulnerability scanning with Trivy
- **`dockerfile_generation.yaml`**: Automated Dockerfile generation workflow
- **`metrics_collector.yaml`**: Performance metrics collection and analysis
- **`test.yaml`**: Container testing and validation suite

#### Development Environment (`.devcontainer/`)

- **`devcontainer.json`**: VS Code devcontainer configuration
- **`Dockerfile`**: Docker-in-Docker development environment setup

### Key Script Components

#### Container Generation (`scripts/generate_dockerfile.py`)

**Core Functionality:**

- Dynamic base image selection with architecture support
- Package installation for Alpine and Debian-based distributions
- Environment variable configuration and multi-stage builds
- Existing Dockerfile extension and modification capabilities

**Usage Patterns:**

```bash
poetry run generate-dockerfile --base-image debian:bullseye --packages "curl wget" --env "NODE_ENV=production"
```

#### Metrics Collection (`scripts/collect_docker_metrics.py`)

**Performance Tracking:**

- Build time measurement and optimization analysis
- Image size monitoring and compression strategies
- Registry usage statistics and pull count tracking
- Multi-registry support (DockerHub, GitHub Container Registry)

#### Tag Management (`scripts/generate_image_tags.py`)

**Automated Tagging:**

- Metadata extraction from Dockerfile LABEL instructions
- Semantic versioning and branch-based tag generation
- Multi-architecture tag coordination and manifest creation

### GitHub Actions Architecture

#### Build Pipeline (`build-publish.yaml`)

**Trigger Conditions:**

- Dockerfile changes in any directory
- Manual workflow dispatch for testing
- Scheduled builds for base image updates

**Build Process:**

1. **Setup**: Checkout code and configure Docker Buildx
2. **Authentication**: Login to container registries
3. **Build**: Multi-architecture container builds
4. **Test**: Container functionality validation
5. **Publish**: Push to configured registries with proper tagging

#### Security Scanning (`container-scan.yaml`)

**Vulnerability Assessment:**

- Trivy security scanner integration
- SARIF report generation for GitHub Security tab
- Critical and high-severity vulnerability blocking
- Scheduled weekly scans for ongoing monitoring

#### Automation Workflows

- **Dockerfile Generation**: Manual trigger for new container creation
- **Metrics Collection**: Daily performance monitoring and reporting
- **Dependency Updates**: Renovate integration for automated updates

### Development Environment

#### Mise Configuration (`.mise.toml`)

**Tool Management:**

- **Python 3.13.4**: Primary development language
- **Node.js 22.17.0**: JavaScript tooling and formatting
- **Poetry**: Python dependency and virtual environment management
- **pnpm 10.13.0**: Fast, disk space efficient package manager
- **pre-commit**: Automated code quality checks

**Environment Variables:**

- `MISE_POETRY_AUTO_INSTALL`: Automatic Poetry installation
- `MISE_POETRY_VENV_AUTO`: Automatic virtual environment creation
- PATH extensions for local tooling

#### Devcontainer Setup

**Docker-in-Docker Environment:**

- Base image: `docker:28.3.0` with security hash pinning
- Essential packages: Python 3, pip, bash for development
- VS Code extensions: Python, Pylance, Docker tools
- Post-creation commands: Automatic dependency installation

## Coding Standards

### Python Guidelines

- **Formatting**: Black formatter with 88-character line length
- **Import Sorting**: isort with Black profile for consistent ordering
- **Type Checking**: Basic type checking with Pylance
- **Documentation**: Docstrings for all public functions and classes
- **Error Handling**: Explicit exception handling with informative messages

**File Structure Example:**

```python
import argparse
import os
from typing import Dict, List, Optional

def generate_dockerfile_content(
    base_image: str,
    packages: Optional[str] = None,
    env_vars: Optional[str] = None,
    architecture: Optional[str] = None,
) -> str:
    """Generate Dockerfile content with specified parameters."""
    # Implementation
```

### Dockerfile Best Practices

- **Base Image Pinning**: Always use SHA256 hashes for reproducible builds
- **Multi-Stage Builds**: Separate build and runtime stages for smaller images
- **Layer Optimization**: Combine RUN commands to reduce layer count
- **Security**: Non-root user creation and minimal package installation
- **Caching**: Leverage BuildKit cache mounts for dependency installation

**Example Structure:**

```dockerfile
FROM debian:bullseye-slim@sha256:...

# Install dependencies in single layer
RUN { \
    set -ex; \
    apt-get update -qq && apt-get install -y --no-install-recommends \
        curl \
        wget; \
    rm -rf /var/lib/apt/lists/*; \
}

# Create non-root user
RUN useradd --create-home --shell /bin/bash appuser
USER appuser

ENTRYPOINT ["app"]
```

### JavaScript/Node.js Guidelines

- **Formatting**: Prettier with custom configuration
- **Line Length**: 100 characters maximum
- **Quotes**: Single quotes for consistency
- **Semicolons**: Required for statement termination
- **Tab Width**: 2 spaces for JavaScript, 4 for JSON in .vscode/

### YAML Configuration

- **Indentation**: 2 spaces consistently
- **Line Length**: 120 characters maximum (yamllint configuration)
- **Quotes**: Minimal quoting, only when necessary
- **Comments**: Descriptive comments for complex workflow steps

## Development Guidelines

### Container Development Workflow

#### 1. Dockerfile Creation

**Manual Creation:**

```bash
# Create new container directory
mkdir -p containers/myapp
cd containers/myapp

# Create Dockerfile with best practices
# - Pin base image with SHA256
# - Use multi-stage builds when applicable
# - Implement security hardening
```

**Automated Generation:**

```bash
# Generate base Dockerfile
poetry run generate-dockerfile \
    --base-image debian:bullseye-slim \
    --packages "curl wget python3" \
    --env "APP_ENV=production PORT=8080" \
    --output-dir containers/myapp
```

#### 2. Local Testing

```bash
# Build container locally
docker build -t myapp:test containers/myapp/

# Test container functionality
docker run --rm myapp:test --version

# Security scan
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
    aquasec/trivy image myapp:test
```

#### 3. Metrics Collection

```bash
# Collect build and size metrics
poetry run collect-docker-metrics --registry github

# Review metrics output
cat collected_metrics.yaml
```

### GitHub Actions Development

#### Workflow Testing

- **Local Testing**: Use `act` or GitHub CLI for local workflow validation
- **Branch Protection**: Test workflows in feature branches before main merge
- **Security Review**: Validate all external actions with security hash pinning

#### Action Configuration Patterns

```yaml
# Secure checkout with hash pinning
- name: Checkout code
  uses: actions/checkout@11bd71901bbe5b1630ceea73d27597364c9af683 # v4.2.2

# Environment setup with caching
- name: Setup
  uses: ./.github/actions/setup

# Conditional execution based on file changes
- if: steps.filter.outputs.changes == 'true'
  name: Build container
  uses: docker/build-push-action@...
```

### Mise Environment Management

#### Tool Installation and Usage

```bash
# Install all tools defined in .mise.toml
mise install

# Use specific tool versions
mise exec python@3.13.4 -- python script.py
mise exec node@22.17.0 -- npm install

# Activate mise in shell (one-time setup)
echo 'eval "$(mise activate zsh)"' >> ~/.zshrc
```

#### Configuration Best Practices

- **Version Pinning**: Specify exact versions for reproducibility
- **Environment Variables**: Use mise for project-specific environment setup
- **Virtual Environments**: Leverage automatic Python venv creation
- **Path Management**: Utilize mise for local binary path management

### Security and Compliance

#### Container Security

- **Base Image Security**: Regularly update base images and scan for vulnerabilities
- **Minimal Attack Surface**: Install only necessary packages and dependencies
- **User Privileges**: Run containers as non-root users when possible
- **Secret Management**: Never embed secrets in container images

#### GitHub Actions Security

- **Action Pinning**: Use SHA256 hashes instead of version tags
- **Secret Access**: Limit secret scope to necessary workflows only
- **Dependency Scanning**: Regular dependency updates via Renovate
- **SARIF Integration**: Upload security scan results to GitHub Security tab

### Testing Standards

- **Unit Tests**: Test individual script functions with pytest
- **Integration Tests**: Validate complete container builds and functionality
- **Security Tests**: Automated vulnerability scanning in CI/CD
- **Performance Tests**: Monitor build times and image sizes over time

### File Organization

- **Logical Grouping**: Group containers by application or use case
- **Clear Naming**: Use descriptive directory and file names
- **Documentation**: README files for complex container setups
- **Metadata**: Use LABEL instructions for container documentation

## Key Development Workflows

### Container Lifecycle Management

#### 1. New Container Development

```bash
# 1. Create container structure
mkdir -p containers/newapp/{branch,release}

# 2. Generate base Dockerfiles
poetry run generate-dockerfile --base-image debian:bullseye --output-dir containers/newapp/release

# 3. Customize for specific needs
# Edit generated Dockerfile for application-specific requirements

# 4. Test locally
docker build -t newapp:test containers/newapp/release/
docker run --rm newapp:test

# 5. Add to CI/CD
# Update build-publish.yaml workflow if needed
```

#### 2. Container Updates and Maintenance

```bash
# 1. Update base images with security patches
# Check for new base image versions

# 2. Regenerate with updated dependencies
poetry run generate-dockerfile --existing-dockerfile containers/app/Dockerfile --packages "updated-package"

# 3. Collect performance metrics
poetry run collect-docker-metrics

# 4. Security scan
poetry run trivy-scan containers/app/
```

#### 3. Release Management

```bash
# 1. Generate tags based on metadata
poetry run generate-image-tags

# 2. Review generated tags
cat generated_tags.json

# 3. Trigger release workflow
gh workflow run release.yaml
```

### Development Environment Setup

#### Initial Setup

```bash
# 1. Clone repository
git clone https://github.com/marcusrbrown/containers.git
cd containers

# 2. Install mise and activate
curl https://mise.run | sh
echo 'eval "$(mise activate zsh)"' >> ~/.zshrc
source ~/.zshrc

# 3. Install all development tools
mise install

# 4. Install Python dependencies
poetry install

# 5. Install Node.js dependencies
pnpm install

# 6. Setup pre-commit hooks
pre-commit install
```

#### VS Code Devcontainer

```bash
# 1. Open in VS Code
code .

# 2. Reopen in container (Command Palette: "Reopen in Container")
# This provides Docker-in-Docker environment with all tools

# 3. Verify environment
poetry --version
docker --version
python --version
```

### Automation and Maintenance

#### Dependency Management

- **Renovate**: Automated dependency updates with testing
- **Poetry**: Python dependency management with lock files
- **pnpm**: JavaScript dependency management with efficient storage
- **mise**: Tool version management and environment consistency

#### Monitoring and Alerts

- **GitHub Actions**: Workflow failure notifications
- **Security Scanning**: Vulnerability alert integration
- **Performance Monitoring**: Build time and image size trending
- **Registry Monitoring**: Pull count and usage analytics

### Contribution Guidelines

#### Pull Request Process

1. **Feature Branches**: Create feature branches for all changes
2. **Testing**: Ensure all containers build and pass security scans
3. **Documentation**: Update README and inline documentation
4. **Code Review**: Peer review for Dockerfile and workflow changes
5. **CI/CD Validation**: All workflows must pass before merge

#### Code Quality Standards

- **Pre-commit Hooks**: Automated formatting and linting
- **Security Review**: Manual review of all Dockerfile changes
- **Performance Impact**: Consider build time and image size impact
- **Backward Compatibility**: Maintain compatibility with existing containers

This repository serves as a comprehensive foundation for container development, providing automation tools, security best practices, and efficient development workflows. Understanding the integration between mise, Poetry, GitHub Actions, and Docker is crucial for effective contributions and maintenance.

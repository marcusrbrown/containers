# containers

> My collection of Dockerfiles, docker-compose files, and related scripts.

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/your-username/your-repo/Your-Workflow-Name)
![Docker Pulls](https://img.shields.io/docker/pulls/your-image-name)
![GitHub Release](https://img.shields.io/github/v/release/marcusrbrown/containers)

## Overview

This repository contains a collection of Dockerfiles for various purposes. It also includes automation tools and workflows for managing the Dockerfiles.

## Features

- Automated Dockerfile generation via `generate_dockerfiles.py`.
- GitHub Actions workflows for linting, building, and releasing Docker images.
- Devcontainer settings for a Docker-in-Docker development environment.

## Usage

### Dockerfile Generation

To generate a new Dockerfile, you can use the [`generate_dockerfile.py`](scripts/generate_dockerfile.py) script:

```bash
python generate_dockerfiles.py --base_image debian --python_version 3.9
```

### Building Docker Images

Use the following command to build a Docker image from a Dockerfile:

```bash
docker build -t your-image-name .
```

### GitHub Actions Workflows

- Dockerfile Generation Workflow: Manually triggered to generate a new Dockerfile and raise a Pull Request.
- Docker Release Workflow: Triggered on push to `main` or manually, to build and release Docker images.

## Contributing

Please read the [CONTRIBUTING.md](repo/CONTRIBUTING.md) for details on how to contribute to this repository.

## License

This project is licensed under the MIT License. See the [LICENSE.md](repo/LICENSE.md) file for details.

## Badges

[![Docker Build](https://img.shields.io/docker/cloud/build/your-docker-hub-username/your-repo-name)](https://hub.docker.com/r/your-docker-hub-username/your-repo-name/builds)
[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/marcusrbrown/containers/build-publish.yaml?branch=main)](https://github.com/marcusrbrown/containers/actions)
[![GitHub Release](https://img.shields.io/github/v/release/marcusrbrown/containers)](https://github.com/marcusrbrown/containers/releases)
[![License](https://img.shields.io/github/license/marcusrbrown/containers)](LICENSE.md)

## Prerequisite Software

- Python 3.x: For running Python scripts.
- Node.js: For running JavaScript-based linting tools.
- Docker: For building and testing Docker images.

## Setup Instructions

### Python Setup

1. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### package.json Setup

1. Install the required Node.js packages:

   ```bash
   pnpm install
   ```

## Usage Instructions

### Invoking Scripts Individually

1. Generate Dockerfiles:

   ```bash
   poetry run generate-dockerfile
   ```

2. Collect Docker Metrics:

   ```bash
   poetry run collect-docker-metrics
   ```

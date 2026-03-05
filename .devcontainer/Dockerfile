# Use a Docker-in-Docker base image
FROM docker:29.3.0@sha256:1ba18449911d01f477a3fc104123c85d677addc60701b14b3fcb5381f9c4a537

# Install essential packages
# NOTE: Alpine repos only serve the latest package version per release.
# The base image digest above is the reproducibility boundary.
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

RUN addgroup -g 1000 devuser && \
    adduser -D -u 1000 -G devuser devuser

USER devuser

# Set up the environment
ENV SHELL /bin/bash

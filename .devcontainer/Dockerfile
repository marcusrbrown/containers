# Use a Docker-in-Docker base image
FROM docker:29.9.1@sha256:3e5756e2b6dad6a5f1f5deacf0a19f9eaa2581b76ae092b2d4a118162e1d4d4e

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

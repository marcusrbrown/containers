# Use a Docker-in-Docker base image
FROM docker:29.2.1@sha256:8bcbad4b45f0bff9d3e809d85a7ac589390f0be8acbc526850c998c35c1243fd

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

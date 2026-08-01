# Use a Docker-in-Docker base image
FROM docker:29.7.0@sha256:084e385b0c9b7ab35d5a46dfedd033721448c000dbec71adcf13da8a9e71baa8

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

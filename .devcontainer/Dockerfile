# Use a Docker-in-Docker base image
FROM docker:29.2.1@sha256:68f6d9ab84623d1116c5432a3b924a07ee09960e6129ca1cb03ef14010588cb4

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

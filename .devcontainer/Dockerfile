# Use a Docker-in-Docker base image
FROM docker:29.6.0@sha256:7bb861a04bb42bda1d237fc2cb539f9823c9b666ecfbfdbd3e534ab74c8cb976

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

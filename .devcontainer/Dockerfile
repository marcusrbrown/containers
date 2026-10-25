# Use a Docker-in-Docker base image
FROM docker:29.9.2@sha256:9e79b879b177fbd72c34376a3dd3d91747da5db49e1f560f76aea59561471977

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

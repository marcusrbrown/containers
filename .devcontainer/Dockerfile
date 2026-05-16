# Use a Docker-in-Docker base image
FROM docker:29.5.0@sha256:8e3fae900cbfbdc14e8abca89a9e44363065cb535f34a09283c59cc0dde2de20

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

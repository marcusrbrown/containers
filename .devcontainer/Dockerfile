# Use a Docker-in-Docker base image
FROM docker:29.4.0@sha256:edaa00c1ab17574f96a93508de97c699dee40a9593b69e6bb0c2b8810d73c505

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

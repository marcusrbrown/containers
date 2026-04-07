# Use a Docker-in-Docker base image
FROM docker:29.4.0@sha256:f80c26212befc1c1988b529495532c6b9180d9b1dab1611f4a1efbe9da8ec821

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

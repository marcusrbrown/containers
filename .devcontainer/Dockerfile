# Use a Docker-in-Docker base image
FROM docker:28.3.0@sha256:85ed11849f25fa5b4d6ce6bc0b53c6738ab3e7d65c9457c2e26a1e404015be4e

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

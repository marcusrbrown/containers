# Use a Docker-in-Docker base image
FROM docker:28.4.0@sha256:2ceb471176ad51e37145d43ce7cbf0fa5d644a2b185bd537f0ef695fb3a37497

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

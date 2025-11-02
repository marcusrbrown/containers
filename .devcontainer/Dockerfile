# Use a Docker-in-Docker base image
FROM docker:28.5.0@sha256:c090c93b63bc690570a0cab398904c855a46f08e0b6804e51bb5ad26e3407f9a

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

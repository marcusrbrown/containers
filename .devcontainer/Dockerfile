# Use a Docker-in-Docker base image
FROM docker:19.03.13

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

# Use a Docker-in-Docker base image
FROM docker:28.2.2@sha256:5fb3f5b69bdab6690d93398a316fdfe906ae4d30667e07994ea5be66483c7b3b

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

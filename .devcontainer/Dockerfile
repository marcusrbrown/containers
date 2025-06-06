# Use a Docker-in-Docker base image
FROM docker:19.03.15@sha256:ea1f0761c92b600417ad14bc9b2b3a30abf8e96e94895fee6cbb5353316f30b0

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

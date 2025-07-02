# Use a Docker-in-Docker base image
FROM docker:28.3.0@sha256:56e360024d7d35dac801b8fc87f869ccf5c89b88399dd266f7cfc1169690a86b

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

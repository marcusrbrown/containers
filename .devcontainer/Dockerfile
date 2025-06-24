# Use a Docker-in-Docker base image
FROM docker:28.2.2@sha256:7613944c7bc318c7b97541bd0e65b8a18d033e37e204305f1ee2639fc9a03827

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

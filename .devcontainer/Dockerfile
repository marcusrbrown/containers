# Use a Docker-in-Docker base image
FROM docker:28.3.0@sha256:c621e5090b92e66b7f2a668e80f4375c30f797fe60fdc16fdde3471c37acd0d7

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

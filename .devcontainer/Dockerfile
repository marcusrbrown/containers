# Use a Docker-in-Docker base image
FROM docker:28.3.0@sha256:f260449941a8347fe7907278a318043d1868fbad74a7acbfe6325b8249968957

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

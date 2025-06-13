# Use a Docker-in-Docker base image
FROM docker:28.2.2@sha256:ff052514f359111edd920b54581e7aca65629458607f9fbdbf82d7eefbe0602b

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

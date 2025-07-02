# Use a Docker-in-Docker base image
FROM docker:28.3.0@sha256:75c0cb1b328158f4adcafcae7a4b02737825422744ff55121a0dbac13ccb770c

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

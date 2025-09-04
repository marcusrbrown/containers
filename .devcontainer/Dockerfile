# Use a Docker-in-Docker base image
FROM docker:28.4.0@sha256:831644212c5bdd0b3362b5855c87b980ea39a83c9e9adcef2ce03eced99a737a

# Install essential packages
RUN apk add --no-cache \
    python3 \
    py3-pip \
    bash

# Set up the environment
ENV SHELL /bin/bash

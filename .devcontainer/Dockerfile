# Use a Docker-in-Docker base image
FROM docker:29.2.1@sha256:8bcbad4b45f0bff9d3e809d85a7ac589390f0be8acbc526850c998c35c1243fd

# Install essential packages
# NOTE: Package versions are coupled to the base image digest above.
# Update versions when bumping the base image SHA.
RUN apk add --no-cache \
    python3=3.12.10-r0 \
    py3-pip=24.3.1-r0 \
    bash=5.2.37-r0

RUN addgroup -g 1000 devuser && \
    adduser -D -u 1000 -G devuser devuser

USER devuser

# Set up the environment
ENV SHELL /bin/bash

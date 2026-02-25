# syntax=docker/dockerfile:1.21@sha256:27f9262d43452075f3c410287a2c43f5ef1bf7ec2bb06e8c9eeb1b8d453087bc
FROM node:24-bookworm-slim@sha256:2a31a1c9c5f82c6a9e3362aac6e9ef836e32409369651befca27a57efed71512

# Multi-architecture build arguments
ARG TARGETPLATFORM
ARG TARGETOS
ARG TARGETARCH
ARG BUILDPLATFORM

# Node.js application version
ARG NODE_VERSION=22.17.0
ENV NODE_VERSION=$NODE_VERSION
ENV NODE_ENV=production

# Install runtime dependencies and security updates
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
  --mount=type=cache,target=/var/lib/apt,sharing=locked \
  { \
  set -ex; \
  \
  # NOTE: Debian repos replace package versions with security updates.
  # Exact version pins break when repos rotate — the base image digest above
  # is the reproducibility boundary, not individual package versions.
  DEPS=" \
  ca-certificates \
  curl \
  tini \
  "; \
  \
  rm -f /etc/apt/apt.conf.d/docker-clean; \
  echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache; \
  apt-get update -qq && apt-get install -qq -y --no-install-recommends $DEPS; \
  \
  # Clean up \
  apt-get autoremove -qq -y; \
  rm -rf /tmp/* /var/tmp/*; \
  }

# Add labels for multi-arch support and metadata
LABEL org.opencontainers.image.title="Node.js Runtime" \
  org.opencontainers.image.description="Multi-architecture Node.js runtime container" \
  org.opencontainers.image.version="${NODE_VERSION}" \
  org.opencontainers.image.vendor="Node.js Foundation" \
  org.opencontainers.image.source="https://github.com/marcusrbrown/containers" \
  org.opencontainers.image.licenses="MIT" \
  org.opencontainers.image.base.name="node:24-bookworm-slim" \
  org.opencontainers.image.base.digest="sha256:a81a03dd965b4052269a57fac857004022b522a4bf06e7a739e25e18bce45af2"

# Base image already provides 'node' user at UID/GID 1000

# Set up application directory
WORKDIR /app
RUN chown node:node /app

# Copy entrypoint script
COPY --chmod=755 docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

# Copy package files for better layer caching
COPY --chown=node:node package*.json ./

# Switch to non-root user
USER node

# Install dependencies
RUN npm ci --only=production && npm cache clean --force

# Copy application code
COPY --chown=node:node . .

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD curl -f http://localhost:3000/health || exit 1

# Expose default Node.js port
EXPOSE 3000

# Use tini as init system for proper signal handling
ENTRYPOINT ["/usr/bin/tini", "--", "/usr/local/bin/docker-entrypoint.sh"]
CMD ["node", "index.js"]

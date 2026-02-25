# syntax=docker/dockerfile:1.21@sha256:27f9262d43452075f3c410287a2c43f5ef1bf7ec2bb06e8c9eeb1b8d453087bc
FROM node:24-alpine@sha256:7b5a34685a2c783049dd76919cfec137b76f846151f0b6f855e539c833e219ac

# Multi-architecture build arguments
ARG TARGETPLATFORM
ARG TARGETOS
ARG TARGETARCH
ARG BUILDPLATFORM

# Node.js application version
ARG NODE_VERSION=22.17.0
ENV NODE_VERSION=$NODE_VERSION
ENV NODE_ENV=production

# Install runtime dependencies
RUN --mount=type=cache,target=/var/cache/apk,sharing=locked \
  { \
  set -ex; \
  \
  # NOTE: Alpine repos only serve the latest package version per release.
  # Exact version pins break when repos rotate — the base image digest above
  # is the reproducibility boundary, not individual package versions.
  apk add --no-cache \
  ca-certificates \
  curl \
  tini; \
  \
  # Clean up \
  rm -rf /tmp/* /var/tmp/*; \
  }

# Add labels for multi-arch support and metadata
LABEL org.opencontainers.image.title="Node.js Runtime (Alpine)" \
  org.opencontainers.image.description="Multi-architecture Node.js runtime container based on Alpine Linux" \
  org.opencontainers.image.version="${NODE_VERSION}" \
  org.opencontainers.image.vendor="Node.js Foundation" \
  org.opencontainers.image.source="https://github.com/marcusrbrown/containers" \
  org.opencontainers.image.licenses="MIT" \
  org.opencontainers.image.base.name="node:24-alpine" \
  org.opencontainers.image.base.digest="sha256:4f696fbf39f383c1e486030ba6b289a5d9af541642fc78ab197e584a113b9c03"

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
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/docker-entrypoint.sh"]
CMD ["node", "index.js"]

# syntax=docker/dockerfile:1.21@sha256:27f9262d43452075f3c410287a2c43f5ef1bf7ec2bb06e8c9eeb1b8d453087bc
FROM node:24-alpine@sha256:4f696fbf39f383c1e486030ba6b289a5d9af541642fc78ab197e584a113b9c03

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

# Create non-root user for security
RUN addgroup -g 1000 -S nodeuser && \
  adduser -S -D -H -u 1000 -h /home/nodeuser -s /sbin/nologin -G nodeuser nodeuser && \
  mkdir -p /home/nodeuser && \
  chown nodeuser:nodeuser /home/nodeuser

# Set up application directory
WORKDIR /app
RUN chown nodeuser:nodeuser /app

# Copy entrypoint script
COPY --chmod=755 docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

# Copy package files for better layer caching
COPY --chown=nodeuser:nodeuser package*.json ./

# Switch to non-root user
USER nodeuser

# Install dependencies
RUN npm ci --only=production && npm cache clean --force

# Copy application code
COPY --chown=nodeuser:nodeuser . .

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 CMD curl -f http://localhost:3000/health || exit 1

# Expose default Node.js port
EXPOSE 3000

# Use tini as init system for proper signal handling
ENTRYPOINT ["/sbin/tini", "--", "/usr/local/bin/docker-entrypoint.sh"]
CMD ["node", "index.js"]

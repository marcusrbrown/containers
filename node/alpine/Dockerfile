# syntax=docker/dockerfile:1.19@sha256:b6afd42430b15f2d2a4c5a02b919e98a525b785b1aaff16747d2f623364e39b6
FROM --platform=$TARGETPLATFORM node:24-alpine@sha256:f36fed0b2129a8492535e2853c64fbdbd2d29dc1219ee3217023ca48aebd3787

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
  # Install packages \
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
  org.label-schema.docker.dockerfile="/node/alpine/Dockerfile" \
  org.label-schema.vcs-type="git"

# Create non-root user for security
RUN addgroup -g 1001 -S nodeuser && \
  adduser -S -D -H -u 1001 -h /home/nodeuser -s /sbin/nologin -G nodeuser nodeuser && \
  mkdir -p /home/nodeuser && \
  chown nodeuser:nodeuser /home/nodeuser

# Set up application directory
WORKDIR /app
RUN chown nodeuser:nodeuser /app

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
ENTRYPOINT ["/sbin/tini", "--"]
CMD ["node", "index.js"]

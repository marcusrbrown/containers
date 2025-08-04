# syntax=docker/dockerfile:1.17@sha256:38387523653efa0039f8e1c89bb74a30504e76ee9f565e25c9a09841f9427b05
FROM --platform=$TARGETPLATFORM node:22-alpine@sha256:f9a425f0ef0b8ab90c7be73eb85cc3a5ae37cfefd3c315db1d787c58eef44fad

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

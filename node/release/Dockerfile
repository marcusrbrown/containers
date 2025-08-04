# syntax=docker/dockerfile:1.17@sha256:38387523653efa0039f8e1c89bb74a30504e76ee9f565e25c9a09841f9427b05
FROM --platform=$TARGETPLATFORM node:22-bookworm-slim@sha256:1a04f0598fcff8b72b58776574740f93226530d953d2c5676e0bd580688e596e

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
  org.label-schema.docker.dockerfile="/node/release/Dockerfile" \
  org.label-schema.vcs-type="git"

# Create non-root user for security
RUN groupadd -r nodeuser && useradd -r -g nodeuser -m -s /bin/bash nodeuser

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
ENTRYPOINT ["/usr/bin/tini", "--"]
CMD ["node", "index.js"]

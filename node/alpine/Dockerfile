# syntax=docker/dockerfile:1.26@sha256:ecfaec9ed6d810b56388c508f4121597bfbba70d41a6dfeee4d8cad5f295fc32
FROM node:24-alpine@sha256:d32cdf619f63fe0471182d08996dd516c6275bb5fd31ae06e55a570bd9e1ad43

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

# Upgrade bundled npm to patch known CVEs in npm's vendored dependencies
# (undici CVE-2026-12151/CVE-2026-9679, tar CVE-2026-53655)
RUN npm install -g npm@12.0.2

# Patch npm's vendored tar, brace-expansion, ip-address, and undici, which
# remain vulnerable in the latest published npm release (CVE-2026-14257,
# GHSA-r292-9mhp-454m, CVE-2026-69152, CVE-2026-69192, CVE-2026-54272,
# CVE-2026-69198, CVE-2026-15157, CVE-2026-16728, CVE-2026-16729). Overwrite
# the bundled copies in-place since npm's internal deps are outside the public
# registry's dependency graph and can't be bumped via `npm install -g` alone.
RUN --mount=type=cache,target=/root/.npm,sharing=locked \
  { \
  set -ex; \
  NPM_ROOT="$(npm root -g)/npm/node_modules"; \
  npm pack tar@7.5.22 brace-expansion@5.0.9 ip-address@10.3.1 undici@6.28.0 --silent --pack-destination /tmp; \
  rm -rf "$NPM_ROOT/tar" "$NPM_ROOT/brace-expansion" "$NPM_ROOT/ip-address" "$NPM_ROOT/undici"; \
  mkdir -p "$NPM_ROOT/tar" "$NPM_ROOT/brace-expansion" "$NPM_ROOT/ip-address" "$NPM_ROOT/undici"; \
  tar -xzf /tmp/tar-7.5.22.tgz -C "$NPM_ROOT/tar" --strip-components=1; \
  tar -xzf /tmp/brace-expansion-5.0.9.tgz -C "$NPM_ROOT/brace-expansion" --strip-components=1; \
  tar -xzf /tmp/ip-address-10.3.1.tgz -C "$NPM_ROOT/ip-address" --strip-components=1; \
  tar -xzf /tmp/undici-6.28.0.tgz -C "$NPM_ROOT/undici" --strip-components=1; \
  rm -f /tmp/tar-7.5.22.tgz /tmp/brace-expansion-5.0.9.tgz /tmp/ip-address-10.3.1.tgz /tmp/undici-6.28.0.tgz; \
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

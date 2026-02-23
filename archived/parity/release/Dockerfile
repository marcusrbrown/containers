# syntax=docker/dockerfile:1.21@sha256:27f9262d43452075f3c410287a2c43f5ef1bf7ec2bb06e8c9eeb1b8d453087bc
FROM --platform=$TARGETPLATFORM debian:bullseye-slim@sha256:f0dbd70ae23f6ffa17f8b816a1ba1a489f7e9b3c32328867f6b456dec869e031

# Multi-architecture build arguments
ARG TARGETPLATFORM
ARG TARGETOS
ARG TARGETARCH
ARG BUILDPLATFORM

ARG PARITY_VERSION=1.4.5
ENV PARITY_VERSION=$PARITY_VERSION

# Platform-specific Parity download URLs
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
  --mount=type=cache,target=/var/lib/apt,sharing=locked \
  { \
  set -ex; \
  \
  # Determine architecture-specific URL
  case "$TARGETARCH" in \
  "amd64") \
  PARITY_ARCH="x86_64-unknown-linux-gnu"; \
  PARITY_DEB="parity_${PARITY_VERSION}_amd64.deb"; \
  ;; \
  "arm64") \
  PARITY_ARCH="aarch64-unknown-linux-gnu"; \
  PARITY_DEB="parity_${PARITY_VERSION}_arm64.deb"; \
  ;; \
  "arm") \
  PARITY_ARCH="armv7-unknown-linux-gnueabihf"; \
  PARITY_DEB="parity_${PARITY_VERSION}_armhf.deb"; \
  ;; \
  *) \
  echo "Unsupported architecture: $TARGETARCH" >&2; \
  exit 1; \
  ;; \
  esac; \
  \
  PARITY_DEB_URL="http://d1h4xl4cr1h0mo.cloudfront.net/v${PARITY_VERSION}/${PARITY_ARCH}/${PARITY_DEB}"; \
  \
  DEPS=" \
  curl \
  ca-certificates \
  "; \
  \
  rm -f /etc/apt/apt.conf.d/docker-clean; \
  echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache; \
  apt-get update -qq && apt-get install -qq -y --no-install-recommends $DEPS; \
  \
  echo "Downloading Parity for $TARGETARCH from $PARITY_DEB_URL"; \
  curl -fsSL "$PARITY_DEB_URL" -o /tmp/parity.deb; \
  # NOTE: This is archived software with broken download URLs. \
  # SHA256 values below are placeholders — update if restoring this container. \
  case "$TARGETARCH" in \
  "amd64") PARITY_SHA256="0000000000000000000000000000000000000000000000000000000000000000" ;; \
  "arm64") PARITY_SHA256="0000000000000000000000000000000000000000000000000000000000000000" ;; \
  "arm") PARITY_SHA256="0000000000000000000000000000000000000000000000000000000000000000" ;; \
  esac; \
  echo "$PARITY_SHA256  /tmp/parity.deb" | sha256sum --check --status; \
  dpkg -i /tmp/parity.deb || true; \
  apt-get install -f -y; \
  \
  apt-get remove -qq -y $DEPS; \
  apt-get autoremove -qq -y; \
  rm -rf /tmp/* /var/tmp/*; \
  }

# Add labels for multi-arch support
LABEL org.opencontainers.image.title="Parity Ethereum Client" \
  org.opencontainers.image.description="Multi-architecture Parity Ethereum client" \
  org.opencontainers.image.version="${PARITY_VERSION}" \
  org.opencontainers.image.vendor="Parity Technologies" \
  org.opencontainers.image.source="https://github.com/marcusrbrown/containers" \
  org.label-schema.docker.dockerfile="/parity/release/Dockerfile" \
  org.label-schema.vcs-type="git"

# Create non-root user for security
RUN groupadd -r parity && useradd -r -g parity parity

# Set up data directory
RUN mkdir -p /home/parity/.local/share/io.parity.ethereum && \
  chown -R parity:parity /home/parity

USER parity
WORKDIR /home/parity

ENTRYPOINT ["parity"]

# syntax=docker/dockerfile:1.17@sha256:38387523653efa0039f8e1c89bb74a30504e76ee9f565e25c9a09841f9427b05
FROM --platform=$TARGETPLATFORM debian:bullseye-slim@sha256:c2c58af6e3ceeb3ed40adba85d24cfa62b7432091597ada9b76b56a51b62f4c6

# Multi-architecture build arguments
ARG TARGETPLATFORM
ARG TARGETOS
ARG TARGETARCH
ARG BUILDPLATFORM

ARG PARITY_BRANCH=master
ENV PARITY_BRANCH=$PARITY_BRANCH
ENV RUST_BACKTRACE=1

# Cross-compilation environment variables
ENV CARGO_TARGET_AARCH64_UNKNOWN_LINUX_GNU_LINKER=aarch64-linux-gnu-gcc
ENV CARGO_TARGET_ARMV7_UNKNOWN_LINUX_GNUEABIHF_LINKER=arm-linux-gnueabihf-gcc

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
  --mount=type=cache,target=/var/lib/apt,sharing=locked \
  --mount=type=cache,target=/usr/local/cargo/registry,sharing=locked \
  { \
  set -ex; \
  \
  # Platform-specific build dependencies
  BUILD_DEPS=" \
  binutils \
  ca-certificates \
  curl \
  file \
  g++ \
  git \
  make \
  pkg-config \
  libudev-dev \
  "; \
  \
  # Add cross-compilation tools for ARM builds
  case "$TARGETARCH" in \
  "arm64") \
  BUILD_DEPS="$BUILD_DEPS gcc-aarch64-linux-gnu"; \
  RUST_TARGET="aarch64-unknown-linux-gnu"; \
  ;; \
  "arm") \
  BUILD_DEPS="$BUILD_DEPS gcc-arm-linux-gnueabihf"; \
  RUST_TARGET="armv7-unknown-linux-gnueabihf"; \
  ;; \
  "amd64") \
  RUST_TARGET="x86_64-unknown-linux-gnu"; \
  ;; \
  *) \
  echo "Unsupported architecture: $TARGETARCH" >&2; \
  exit 1; \
  ;; \
  esac; \
  \
  # Configure APT cache
  rm -f /etc/apt/apt.conf.d/docker-clean; \
  echo 'Binary::apt::APT::Keep-Downloaded-Packages "true";' > /etc/apt/apt.conf.d/keep-cache; \
  \
  # Install build dependencies
  apt-get update -qq; \
  apt-get install -qq -y --no-install-recommends $BUILD_DEPS; \
  \
  # Install Rust compiler and add cross-compilation target
  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y --default-toolchain stable; \
  export PATH=$HOME/.cargo/bin:$PATH; \
  \
  # Add target architecture for cross-compilation
  if [ "$RUST_TARGET" != "x86_64-unknown-linux-gnu" ]; then \
  rustup target add "$RUST_TARGET"; \
  fi; \
  \
  rustc -vV; \
  cargo -V; \
  \
  # Clone Parity repository
  git clone https://github.com/ethcore/parity /tmp/parity --depth 1 --branch "$PARITY_BRANCH"; \
  cd /tmp/parity; \
  \
  # Build Parity for target architecture
  if [ "$RUST_TARGET" != "x86_64-unknown-linux-gnu" ]; then \
  cargo build --release --target "$RUST_TARGET"; \
  PARITY_BINARY="/tmp/parity/target/$RUST_TARGET/release/parity"; \
  else \
  cargo build --release; \
  PARITY_BINARY="/tmp/parity/target/release/parity"; \
  fi; \
  \
  # Verify binary exists and copy to final location
  ls -la "$PARITY_BINARY"; \
  strip "$PARITY_BINARY"; \
  cp "$PARITY_BINARY" /usr/local/bin/parity; \
  chmod +x /usr/local/bin/parity; \
  \
  # Remove build dependencies and clean up
  apt-get purge -qq -y --auto-remove $BUILD_DEPS; \
  rm -rf /tmp/* /var/tmp/*; \
  }

# Add labels for multi-arch support
LABEL org.opencontainers.image.title="Parity Ethereum Client (Branch Build)" \
  org.opencontainers.image.description="Multi-architecture Parity Ethereum client built from source branch" \
  org.opencontainers.image.vendor="Parity Technologies" \
  org.opencontainers.image.source="https://github.com/marcusrbrown/containers" \
  org.label-schema.docker.dockerfile="/parity/branch/Dockerfile" \
  org.label-schema.vcs-type="git" \
  org.label-schema.build-arch="$TARGETARCH" \
  parity.branch="$PARITY_BRANCH"

# Create non-root user for security
RUN groupadd -r parity && useradd -r -g parity parity

# Set up data directory
RUN mkdir -p /home/parity/.local/share/io.parity.ethereum && \
  chown -R parity:parity /home/parity

USER parity
WORKDIR /home/parity

ENTRYPOINT ["parity"]

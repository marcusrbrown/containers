FROM debian:jessie-slim

ARG PARITY_BRANCH=master
ENV PARITY_BRANCH $PARITY_BRANCH

ENV RUST_BACKTRACE 1

RUN { \
      set -ex; \

      BUILD_DEPS=" \
        binutils \
        ca-certificates \
        curl \
        file \
        g++ \
        git \
        make \
      "; \

      # Install build dependencies
      apt-get update -qq; \
      apt-get install -qq -y --no-install-recommends $BUILD_DEPS; \

      # Install Rust compiler and add it to the PATH
      curl https://sh.rustup.rs -sSf | sh -s -- -y; \
      export PATH=$HOME/.cargo/bin:$PATH; \

      rustc -vV; \
      cargo -V; \
      g++ -v; \
      make -v; \

      # Clone and build Parity from the specified branch
      git clone https://github.com/ethcore/parity /tmp/parity --depth 1 --branch $PARITY_BRANCH; \
      cd /tmp/parity; \

      cargo build --release; \
      ls target/release/parity; \
      strip target/release/parity; \
      mv target/release/parity /usr/local/bin; \

      # Remove build dependencies and clean up
      apt-get purge -qq -y --auto-remove $BUILD_DEPS; \
      rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* $HOME/.multirust $HOME/.cargo; \
    }

ENTRYPOINT ["parity"]

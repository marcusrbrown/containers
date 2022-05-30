FROM debian:jessie-slim@sha256:b9b0e7354098cbd534861d7532c082fb81cdb4d893303ba1f322f52c9e583cd2

ARG PARITY_VERSION=1.4.5
ENV PARITY_VERSION $PARITY_VERSION
ENV PARITY_DEB_URL http://d1h4xl4cr1h0mo.cloudfront.net/v${PARITY_VERSION}/x86_64-unknown-linux-gnu/parity_${PARITY_VERSION}_amd64.deb

RUN { \
      set -ex; \

      DEPS=" \
        curl \
      "; \

      apt-get update -qq && apt-get install -qq -y --no-install-recommends $DEPS; \

      curl -Lk $PARITY_DEB_URL > /tmp/parity.deb; \
      dpkg -i /tmp/parity.deb; \

      apt-get remove -qq -y $DEPS; \
      apt-get autoremove -qq -y; \
      rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*; \
    }

ENTRYPOINT ["parity"]

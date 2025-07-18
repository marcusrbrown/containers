# syntax=docker/dockerfile:1@sha256:9857836c9ee4268391bb5b09f9f157f3c91bb15821bb77969642813b0d00518d
# Node.js Express Application Template
# Generated by Container Template Engine at {{ generated_at }}

ARG NODE_VERSION={{ node_version }}
FROM node:${NODE_VERSION}-alpine

# Metadata
LABEL maintainer="{{ author | default('Container Template Engine') }}"
LABEL version="{{ template_version }}"
LABEL description="{{ description | default('Node.js Express application') }}"
LABEL org.opencontainers.image.title="{{ template_name }}"
LABEL org.opencontainers.image.description="{{ description | default('Node.js Express application') }}"
LABEL org.opencontainers.image.version="{{ template_version }}"
LABEL org.opencontainers.image.created="{{ generated_at }}"

# Build arguments
ARG TARGETPLATFORM
ARG TARGETARCH
ARG BUILDPLATFORM
ARG APP_NAME={{ app_name }}
ARG APP_PORT={{ app_port }}
ARG NODE_ENV=production

# Install system dependencies
RUN set -eux; \
    apk update; \
    apk add --no-cache \
        curl \
        wget \
        ca-certificates \
        dumb-init \
        {% if enable_typescript -%}
        python3 \
        make \
        g++ \
        {% endif -%}
        tzdata; \
    rm -rf /var/cache/apk/*; \
    rm -rf /tmp/*

# Create app directory and user
RUN addgroup -g 1000 node && \
    adduser -D -u 1000 -G node -s /bin/sh node

WORKDIR /usr/src/app

# Copy package files
COPY package*.json ./
{% if enable_typescript -%}
COPY tsconfig.json ./
{% endif %}
{% if enable_hot_reload -%}
COPY nodemon.json ./
{% endif %}

# Install dependencies
RUN set -eux; \
    npm ci --only=production --no-audit --no-fund; \
    {% if enable_typescript -%}
    npm install -g typescript@latest; \
    {% endif -%}
    npm cache clean --force; \
    chown -R node:node /usr/src/app

# Copy application code
COPY --chown=node:node src/ ./src/

# Build TypeScript if enabled
{% if enable_typescript -%}
RUN npm run build
{% endif %}

# Switch to non-root user
USER node

# Expose port
EXPOSE ${APP_PORT}

# Environment variables
ENV NODE_ENV=${NODE_ENV}
ENV PORT=${APP_PORT}
ENV APP_NAME=${APP_NAME}

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:${APP_PORT}/health || exit 1

# Use dumb-init to handle signals properly
ENTRYPOINT ["dumb-init", "--"]

# Start the application
{% if enable_hot_reload and node_env != 'production' -%}
CMD ["npm", "run", "dev"]
{% elif enable_typescript -%}
CMD ["npm", "start"]
{% else -%}
CMD ["node", "src/app.js"]
{% endif %}

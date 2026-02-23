# Go Microservice Container Template
# Multi-stage build for optimal performance

ARG GO_VERSION={{ go_version }}
FROM golang:${GO_VERSION}-alpine AS builder

# Metadata
LABEL maintainer="Container Template Engine"
LABEL version="1.0.0"
LABEL description="High-performance Go microservice with gRPC and REST APIs"
LABEL service.name="{{ service_name }}"

# Build arguments
ARG SERVICE_NAME={{ service_name }}
ARG HTTP_PORT={{ http_port }}
ARG GRPC_PORT={{ grpc_port }}
ARG METRICS_PORT={{ metrics_port }}

# Install build dependencies
RUN apk add --no-cache \
    git \
    gcc \
    musl-dev \
    protoc \
    protobuf-dev

# Install Go tools
RUN go install google.golang.org/protobuf/cmd/protoc-gen-go@latest && \
    go install google.golang.org/grpc/cmd/protoc-gen-go-grpc@latest

# Set working directory
WORKDIR /build

# Copy go mod files
COPY go.mod go.sum ./

# Download dependencies
RUN go mod download && go mod verify

# Copy source code
COPY . .

# Generate protobuf code
RUN protoc --go_out=. --go_opt=paths=source_relative \
    --go-grpc_out=. --go-grpc_opt=paths=source_relative \
    proto/*.proto

# Build the application
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build \
    -ldflags='-w -s -extldflags "-static"' \
    -tags netgo \
    -o /build/{{ service_name }} \
    .

# Runtime stage
ARG ALPINE_VERSION=3.21
FROM alpine:${ALPINE_VERSION}

# Install runtime dependencies
RUN apk --no-cache add \
    ca-certificates \
    curl \
    tzdata \
    && rm -rf /var/cache/apk/*

# Create app user
RUN addgroup -g 1000 -S appgroup && \
    adduser -u 1000 -S appuser -G appgroup

# Set working directory
WORKDIR /app

# Copy binary from builder
COPY --from=builder --chown=appuser:appgroup /build/{{ service_name }} /app/{{ service_name }}

# Copy configuration files
COPY --chown=appuser:appgroup config/ ./config/
COPY --chown=appuser:appgroup entrypoint.sh /entrypoint.sh
COPY --chown=appuser:appgroup health.sh /health.sh

# Make scripts executable
RUN chmod +x /entrypoint.sh /health.sh

# Create necessary directories
RUN mkdir -p /app/logs /app/data && \
    chown -R appuser:appgroup /app

# Set environment variables
ENV SERVICE_NAME=${SERVICE_NAME} \
    HTTP_PORT=${HTTP_PORT} \
    GRPC_PORT=${GRPC_PORT} \
    METRICS_PORT=${METRICS_PORT} \
    GIN_MODE=release

# Switch to non-root user
USER appuser

# Expose ports
EXPOSE ${HTTP_PORT} ${GRPC_PORT} ${METRICS_PORT}

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD /health.sh

# Volume for data
VOLUME ["/app/data"]

# Start application
ENTRYPOINT ["/entrypoint.sh"]
CMD ["/app/{{ service_name }}"]

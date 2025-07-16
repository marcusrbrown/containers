# Python FastAPI Container Template
# Multi-stage build for production optimization

ARG PYTHON_VERSION={{ python_version }}
FROM python:${PYTHON_VERSION}-alpine AS base

# Metadata
LABEL maintainer="Container Template Engine"
LABEL version="1.0.0"
LABEL description="High-performance Python web API with FastAPI framework"
LABEL app.name="{{ app_name }}"
LABEL app.version="1.0.0"

# Build arguments
ARG APP_NAME={{ app_name }}
ARG PORT={{ port }}
ARG DEBUG={{ debug }}

# Environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    APP_NAME=${APP_NAME} \
    PORT=${PORT} \
    DEBUG=${DEBUG}

# Create app user
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    openssl-dev \
    curl \
    && rm -rf /var/cache/apk/*

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=appuser:appgroup . .

# Create necessary directories
RUN mkdir -p /app/logs /app/data && \
    chown -R appuser:appgroup /app

# Copy entrypoint script
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Switch to non-root user
USER appuser

# Expose port
EXPOSE ${PORT}

# Health check
COPY healthcheck.py /healthcheck.py
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python /healthcheck.py

# Start application
ENTRYPOINT ["/entrypoint.sh"]
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "{{ port }}", {% if debug %}"--reload"{% endif %}]

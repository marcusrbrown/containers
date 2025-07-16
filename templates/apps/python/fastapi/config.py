#!/usr/bin/env python3
"""
Configuration module for {{ app_name }}

Centralized settings management using Pydantic Settings.
"""

from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """Application settings."""

    # Application
    app_name: str = "{{ app_name }}"
    debug: bool = {{ debug }}
    secret_key: str = "{{ secret_key }}"

    # Server
    host: str = "0.0.0.0"
    port: int = {{ port }}
    workers: int = {{ workers }}

    # Database
    database_url: str = "{{ database_url }}"

    # Security
    cors_origins: List[str] = {{ cors_origins }}
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    # API Documentation
    enable_docs: bool = {{ enable_docs }}

    # Logging
    log_level: str = "DEBUG" if debug else "INFO"
    log_format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    # Redis (for caching/sessions)
    redis_url: str = os.getenv("REDIS_URL", "redis://localhost:6379")

    # File uploads
    max_file_size: int = 10 * 1024 * 1024  # 10MB
    upload_dir: str = "/app/uploads"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

# Global settings instance
settings = Settings()

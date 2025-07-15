# Archived Containers

This directory contains outdated container definitions that are no longer actively maintained.

## Parity Ethereum Client

**Archived Date**: July 15, 2025
**Reason**: End-of-life software with broken dependencies

### Issues Found

- **Debian Jessie**: Base image reached end-of-life in June 2020
- **Repository Unavailable**: APT repositories no longer accessible
- **Download URLs Broken**: Parity 1.4.5 distribution URLs return 404 errors
- **Security Concerns**: Outdated base image with known vulnerabilities

### Original Structure

```text
parity/
├── branch/
│   └── Dockerfile          # Development builds from Git branches
└── release/
    └── Dockerfile          # Production builds from stable releases
```

### Migration Notes

The Parity containers have been replaced with modern Node.js containers that:

- Use current, supported base images (Debian Bookworm, Alpine)
- Follow security best practices
- Include comprehensive health checks
- Support multi-architecture builds
- Provide working download/installation processes

### Restoration

If you need to restore these containers:

1. Update base images to current Debian/Alpine versions
2. Find alternative Parity distribution sources
3. Update package installation methods
4. Test multi-architecture builds
5. Verify security compliance

The containers were last functional with the Debian Bullseye update that resolved the original exit code 127 error.

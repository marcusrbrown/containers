# redis-cache - Troubleshooting Guide

Common issues and solutions for this template.

## Template Generation Issues

### Issue: Template validation fails

```bash
poetry run template-engine validate databases/redis
```

**Common causes:**
- Missing required parameters
- Invalid parameter values
- Template syntax errors

**Solutions:**
- Check parameter requirements: `poetry run template-engine list`
- Validate your parameters against the schema
- Check template files for syntax errors

### Issue: Template generation produces empty files

**Symptoms:**
- Files are created but have no content
- Jinja2 template errors in output

**Solutions:**
- Verify all required parameters are provided
- Check parameter types match template expectations
- Review template syntax in source files

## Container Build Issues

### Issue: Docker build fails

```bash
# Check build logs
docker build -t redis-cache:debug . --no-cache

# Build with verbose output
docker build -t redis-cache:debug . --progress=plain
```

**Common causes:**
- Base image not available
- Package installation failures
- File permission issues
- Network connectivity problems

**Solutions:**
- Verify base image exists and is accessible
- Check package manager commands
- Ensure proper file permissions in Dockerfile
- Check network connectivity and proxy settings

### Issue: Build takes too long

**Solutions:**
- Use multi-stage builds
- Optimize package installation order
- Use .dockerignore to exclude unnecessary files
- Consider using different base images

## Container Runtime Issues

### Issue: Container exits immediately

```bash
# Check container logs
docker logs container_name

# Run interactively for debugging
docker run -it --entrypoint /bin/sh redis-cache:latest
```

**Common causes:**
- Application startup failures
- Missing environment variables
- Permission issues
- Port conflicts

**Solutions:**
- Check application logs
- Verify all required environment variables are set
- Ensure proper user permissions
- Check for port conflicts

### Issue: Container health check fails

```bash
# Manual health check
docker exec container_name /usr/local/bin/healthcheck.sh

# Check health status
docker inspect container_name | grep Health -A 10
```

**Solutions:**
- Verify health check script exists and is executable
- Check application is actually running
- Verify health check endpoint is accessible
- Adjust health check timeouts


## Database-Specific Issues

### Issue: Database won't start

**Common causes:**
- Data directory permissions
- Configuration errors
- Insufficient disk space
- Port conflicts

**Solutions:**
```bash
# Check permissions
docker exec container_name ls -la /var/lib/postgresql/data

# Check disk space
docker exec container_name df -h

# Check configuration
docker exec container_name pg_ctl status
```

### Issue: Connection refused

**Debugging:**
```bash
# Check if database is listening
docker exec container_name netstat -tlnp | grep 5432

# Test connection
docker exec container_name psql -h localhost -U username -d database

# Check authentication
docker exec container_name cat /var/lib/postgresql/data/pg_hba.conf
```

### Issue: Performance problems

**Solutions:**
```bash
# Check running queries
docker exec container_name psql -c "SELECT * FROM pg_stat_activity;"

# Check locks
docker exec container_name psql -c "SELECT * FROM pg_locks;"

# Analyze slow queries
docker exec container_name psql -c "SELECT * FROM pg_stat_statements ORDER BY total_time DESC;"
```

## Performance Issues

### Issue: High memory usage

```bash
# Monitor memory usage
docker stats container_name

# Check memory limits
docker inspect container_name | grep -i memory
```

**Solutions:**
- Set appropriate memory limits
- Optimize application memory usage
- Use lighter base images
- Profile application memory usage

### Issue: Slow response times

**Debugging steps:**
```bash
# Check CPU usage
docker stats container_name

# Network latency
docker exec container_name ping target_host

# Application metrics
docker exec container_name curl localhost:port/metrics
```

## Getting Help

### Check logs
```bash
# Container logs
docker logs container_name

# System logs
docker events

# Docker daemon logs
sudo journalctl -u docker.service
```

### Debug mode
```bash
# Run with debug output
poetry run template-engine generate databases/redis ./debug \
  --param debug=true \
  --param log_level=debug

# Interactive debugging
docker run -it --entrypoint /bin/bash redis-cache:latest
```

### Community resources
- Template documentation: [README.md](README.md)
- Parameter reference: [PARAMETERS.md](PARAMETERS.md)
- Usage examples: [EXAMPLES.md](EXAMPLES.md)
- GitHub issues: [Report a bug or request a feature]

---

*Troubleshooting guide for template: databases/redis*
*Last updated: 2025-07-15 21:54:36*

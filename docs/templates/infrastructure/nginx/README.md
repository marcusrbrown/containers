# nginx-proxy

nginx reverse proxy with SSL termination and load balancing

## Overview

- **Category**: Infrastructure
- **Version**: 1.0.0
- **Author**: Container Template Engine
- **License**: MIT
- **Tags**: nginx, proxy, load-balancer, ssl, web-server

## Quick Start

### Generate from Template

```bash
# Basic usage
poetry run template-engine generate infrastructure/nginx ./my-nginx-proxy

# With custom parameters
poetry run template-engine generate infrastructure/nginx ./my-nginx-proxy \
  --param param_name=value \
  --param another_param=value

# Using parameter file
poetry run template-engine generate infrastructure/nginx ./my-nginx-proxy \
  --params params.json
```

### Using Docker Compose

```bash
cd my-nginx-proxy
docker-compose up -d
```

### Manual Docker Build

```bash
cd my-nginx-proxy
docker build -t my-nginx-proxy:latest .
docker run -d --name my-nginx-proxy my-nginx-proxy:latest
```

## Parameters

### Required Parameters
None

### Optional Parameters
- `nginx_version` (string): nginx version (default: `1.25`)
- `server_name` (string): Server name for nginx (default: `localhost`)
- `listen_port` (integer): HTTP listen port (default: `80`)
- `ssl_port` (integer): HTTPS listen port (default: `443`)
- `enable_ssl` (boolean): Enable SSL/TLS support (default: `True`)
- `ssl_cert_path` (string): SSL certificate path (default: `/etc/ssl/certs/nginx.crt`)
- `ssl_key_path` (string): SSL private key path (default: `/etc/ssl/private/nginx.key`)
- `upstream_servers` (array): Backend servers for load balancing (default: `['backend1:8080', 'backend2:8080']`)
- `load_balancing_method` (string): Load balancing method (default: `round_robin`)
- `enable_gzip` (boolean): Enable gzip compression (default: `True`)
- `enable_rate_limiting` (boolean): Enable rate limiting (default: `True`)
- `rate_limit` (string): Rate limit (requests per second) (default: `10r/s`)
- `enable_caching` (boolean): Enable response caching (default: `True`)
- `worker_processes` (string): Number of worker processes (default: `auto`)
- `worker_connections` (integer): Worker connections (default: `1024`)


[📋 **Full Parameter Reference**](PARAMETERS.md)

## Generated Files

This template generates the following files:

### Dockerfile
- `Dockerfile`

### Compose
- `docker-compose.yml`

### Config
- `nginx.conf`
- `ssl.conf`
- `upstream.conf`
- `cache.conf`

### Scripts
- `healthcheck.sh`
- `reload.sh`

### Docs
- `README.md`
- `SSL_SETUP.md`


## Examples

[📖 **Usage Examples**](EXAMPLES.md)

## Troubleshooting

[🔧 **Troubleshooting Guide**](TROUBLESHOOTING.md)

## Dependencies

### Build
- nginx

### Runtime
- nginx
- curl

### Test
- docker
- curl

## Supported Platforms

linux/amd64, linux/arm64

## Testing

This template includes comprehensive testing:

### Test Commands
- `docker run --rm -p 80:80 -d {{ template_name }}:latest`
- `sleep 5`
- `curl -f http://localhost/health`

### Integration Tests
- `nginx -t`


## Contributing

To modify this template:

1. Edit the template files in `templates/infrastructure/nginx/`
2. Update `template.yaml` for parameter changes
3. Test your changes: `poetry run template-engine test infrastructure/nginx`
4. Regenerate documentation: `poetry run generate-docs`

## Related Templates

Browse other templates in the same category: [**Infrastructure Templates**](../infrastructure/README.md)

---

*Documentation generated automatically from template metadata*
*Last updated: 2025-07-15 21:54:36*

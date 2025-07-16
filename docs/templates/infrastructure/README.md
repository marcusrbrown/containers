# Infrastructure Templates

Collection of 1 templates for infrastructure containers.

## Available Templates

### [nginx-proxy](infrastructure/nginx/README.md)

nginx reverse proxy with SSL termination and load balancing

- **Version**: 1.0.0
- **Tags**: nginx, proxy, load-balancer, ssl, web-server

```bash
poetry run template-engine generate infrastructure/nginx ./my-nginx-proxy
```

---


## Category Overview

Infrastructure templates provide pre-configured containers for common infrastructure scenarios. Each template includes:

- Production-ready configuration
- Security hardening
- Performance optimization
- Comprehensive documentation
- Automated testing

## Common Use Cases


- **Load Balancers**: Traffic distribution and SSL termination
- **Reverse Proxies**: Request routing and caching
- **API Gateways**: Service mesh entry points
- **Monitoring**: Observability and alerting systems


## Getting Started

1. **Choose a template** from the list above
2. **Generate your project**:
   ```bash
   poetry run template-engine generate template-path ./my-project
   ```
3. **Customize parameters** as needed
4. **Build and deploy** your container

## Template Comparison

| Template | Use Case | Size | Complexity | Best For |
|----------|----------|------|------------|----------|
| nginx-proxy | nginx reverse proxy with SSL t... | TBD | Complex | Production use |


## Related Categories

- [**App Templates**](../app/README.md) - Application containers
- [**Database Templates**](../database/README.md) - Database systems
- [**Infrastructure Templates**](../infrastructure/README.md) - Infrastructure components
- [**Base Templates**](../base/README.md) - Foundation images

[⬅️ **Back to all templates**](../README.md)

---

*Infrastructure category documentation*
*1 templates available*

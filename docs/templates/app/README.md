# App Templates

Collection of 2 templates for app containers.

## Available Templates

### [Python FastAPI](apps/python/fastapi/README.md)

High-performance Python web API with FastAPI framework

- **Version**: 1.0.0
- **Tags**: python, fastapi, web, api, async

```bash
poetry run template-engine generate apps/python/fastapi ./my-Python FastAPI
```

---

### [nodejs-express](apps/nodejs/express/README.md)

Node.js Express web application template with TypeScript support

- **Version**: 1.0.0
- **Tags**: nodejs, express, typescript, web, api

```bash
poetry run template-engine generate apps/nodejs/express ./my-nodejs-express
```

---

## Category Overview

App templates provide pre-configured containers for common app scenarios. Each template includes:

- Production-ready configuration
- Security hardening
- Performance optimization
- Comprehensive documentation
- Automated testing

## Common Use Cases

- **Web Applications**: Full-stack web apps with frameworks like Express, FastAPI
- **API Services**: RESTful and GraphQL API backends
- **Microservices**: Containerized microservice components
- **Background Workers**: Queue processors and scheduled tasks

## Getting Started

1. **Choose a template** from the list above
2. **Generate your project**:
   ```bash
   poetry run template-engine generate template-path ./my-project
   ```
3. **Customize parameters** as needed
4. **Build and deploy** your container

## Template Comparison

| Template       | Use Case                          | Size | Complexity | Best For       |
| -------------- | --------------------------------- | ---- | ---------- | -------------- |
| Python FastAPI | High-performance Python web AP... | TBD  | Complex    | Production use |
| nodejs-express | Node.js Express web applicatio... | TBD  | Complex    | Production use |

## Related Categories

- [**App Templates**](../app/README.md) - Application containers
- [**Database Templates**](../database/README.md) - Database systems
- [**Infrastructure Templates**](../infrastructure/README.md) - Infrastructure components
- [**Base Templates**](../base/README.md) - Foundation images

[⬅️ **Back to all templates**](../README.md)

---

_App category documentation_
_2 templates available_

# Database Templates

Collection of 2 templates for database containers.

## Available Templates

### [postgresql](databases/postgresql/README.md)

PostgreSQL database server with security hardening and performance optimization

- **Version**: 1.0.0
- **Tags**: postgresql, database, sql, postgres

```bash
poetry run template-engine generate databases/postgresql ./my-postgresql
```

---

### [redis-cache](databases/redis/README.md)

Redis in-memory data store with persistence and security

- **Version**: 1.0.0
- **Tags**: redis, cache, nosql, memory, session-store

```bash
poetry run template-engine generate databases/redis ./my-redis-cache
```

---


## Category Overview

Database templates provide pre-configured containers for common database scenarios. Each template includes:

- Production-ready configuration
- Security hardening
- Performance optimization
- Comprehensive documentation
- Automated testing

## Common Use Cases


- **Primary Databases**: Production database instances
- **Read Replicas**: Scalable read-only database copies
- **Analytics**: Data warehousing and analytics databases
- **Caching**: In-memory data stores for performance


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
| postgresql | PostgreSQL database server wit... | TBD | Complex | Production use |
| redis-cache | Redis in-memory data store wit... | TBD | Complex | Production use |


## Related Categories

- [**App Templates**](../app/README.md) - Application containers
- [**Database Templates**](../database/README.md) - Database systems
- [**Infrastructure Templates**](../infrastructure/README.md) - Infrastructure components
- [**Base Templates**](../base/README.md) - Foundation images

[⬅️ **Back to all templates**](../README.md)

---

*Database category documentation*
*2 templates available*

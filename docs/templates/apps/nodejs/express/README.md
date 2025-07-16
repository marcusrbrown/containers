# nodejs-express

Node.js Express web application template with TypeScript support

## Overview

- **Category**: App
- **Version**: 1.0.0
- **Author**: Container Template Engine
- **License**: MIT
- **Tags**: nodejs, express, typescript, web, api

## Quick Start

### Generate from Template

```bash
# Basic usage
poetry run template-engine generate apps/nodejs/express ./my-nodejs-express

# With custom parameters
poetry run template-engine generate apps/nodejs/express ./my-nodejs-express \
  --param param_name=value \
  --param another_param=value

# Using parameter file
poetry run template-engine generate apps/nodejs/express ./my-nodejs-express \
  --params params.json
```

### Using Docker Compose

```bash
cd my-nodejs-express
docker-compose up -d
```

### Manual Docker Build

```bash
cd my-nodejs-express
docker build -t my-nodejs-express:latest .
docker run -d --name my-nodejs-express my-nodejs-express:latest
```

## Parameters

### Required Parameters
None

### Optional Parameters
- `alpine_version` (string): Alpine Linux version (default: `3.20`)
- `packages` (array): Additional packages to install (default: `['curl', 'wget', 'ca-certificates']`)
- `user_name` (string): Non-root user name (default: `appuser`)
- `user_uid` (integer): User UID (default: `1000`)
- `timezone` (string): System timezone (default: `UTC`)
- `enable_security_updates` (boolean): Enable automatic security updates (default: `True`)
- `node_version` (string): Node.js version (default: `22`)
- `app_name` (string): Application name (default: `express-app`)
- `app_port` (integer): Application port (default: `3000`)
- `enable_typescript` (boolean): Enable TypeScript support (default: `True`)
- `enable_hot_reload` (boolean): Enable hot reload for development (default: `True`)
- `install_packages` (array): Additional npm packages to install (default: `['helmet', 'cors', 'compression', 'morgan']`)
- `dev_packages` (array): Development packages to install (default: `['nodemon', '@types/node', '@types/express']`)


[📋 **Full Parameter Reference**](PARAMETERS.md)

## Generated Files

This template generates the following files:

### Dockerfile
- `Dockerfile`

### Compose
- `docker-compose.yml`

### Config
- `package.json`
- `tsconfig.json`
- `nodemon.json`
- `.dockerignore`

### Docs
- `README.md`
- `API.md`

### Scripts
- `src/app.ts`
- `src/routes/health.ts`
- `src/middleware/error.ts`


## Examples

[📖 **Usage Examples**](EXAMPLES.md)

## Troubleshooting

[🔧 **Troubleshooting Guide**](TROUBLESHOOTING.md)

## Dependencies

### Build
- nodejs
- npm

### Runtime
- nodejs
- npm

### Test
- docker
- curl

## Supported Platforms

linux/amd64, linux/arm64

## Testing

This template includes comprehensive testing:

### Test Commands
- `docker run --rm -p 3000:3000 -d {{ template_name }}:latest`
- `sleep 5`
- `curl -f http://localhost:3000/health`

### Integration Tests
- `npm test`
- `npm run test:e2e`


## Contributing

To modify this template:

1. Edit the template files in `templates/apps/nodejs/express/`
2. Update `template.yaml` for parameter changes
3. Test your changes: `poetry run template-engine test apps/nodejs/express`
4. Regenerate documentation: `poetry run generate-docs`

## Related Templates

Browse other templates in the same category: [**App Templates**](../app/README.md)

---

*Documentation generated automatically from template metadata*
*Last updated: 2025-07-15 21:54:36*

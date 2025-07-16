{% if enable_typescript -%}
import { Router, Request, Response } from 'express';

const router = Router();

// Health check endpoint
router.get('/', (req: Request, res: Response) => {
  const healthStatus = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    version: '{{ template_version }}',
    environment: process.env.NODE_ENV || 'development',
    memory: {
      used: Math.round((process.memoryUsage().heapUsed / 1024 / 1024) * 100) / 100,
      total: Math.round((process.memoryUsage().heapTotal / 1024 / 1024) * 100) / 100,
      percentage: Math.round((process.memoryUsage().heapUsed / process.memoryUsage().heapTotal) * 100)
    },
    system: {
      platform: process.platform,
      arch: process.arch,
      node_version: process.version,
      pid: process.pid
    }
  };

  res.status(200).json(healthStatus);
});

// Readiness check
router.get('/ready', (req: Request, res: Response) => {
  // Add any readiness checks here (database connections, external services, etc.)
  res.status(200).json({
    status: 'ready',
    timestamp: new Date().toISOString()
  });
});

// Liveness check
router.get('/live', (req: Request, res: Response) => {
  res.status(200).json({
    status: 'alive',
    timestamp: new Date().toISOString()
  });
});

export { router as healthRouter };
{% else -%}
const { Router } = require('express');

const router = Router();

// Health check endpoint
router.get('/', (req, res) => {
  const healthStatus = {
    status: 'healthy',
    timestamp: new Date().toISOString(),
    uptime: process.uptime(),
    version: '{{ template_version }}',
    environment: process.env.NODE_ENV || 'development',
    memory: {
      used: Math.round((process.memoryUsage().heapUsed / 1024 / 1024) * 100) / 100,
      total: Math.round((process.memoryUsage().heapTotal / 1024 / 1024) * 100) / 100,
      percentage: Math.round((process.memoryUsage().heapUsed / process.memoryUsage().heapTotal) * 100)
    },
    system: {
      platform: process.platform,
      arch: process.arch,
      node_version: process.version,
      pid: process.pid
    }
  };

  res.status(200).json(healthStatus);
});

// Readiness check
router.get('/ready', (req, res) => {
  // Add any readiness checks here (database connections, external services, etc.)
  res.status(200).json({
    status: 'ready',
    timestamp: new Date().toISOString()
  });
});

// Liveness check
router.get('/live', (req, res) => {
  res.status(200).json({
    status: 'alive',
    timestamp: new Date().toISOString()
  });
});

module.exports = { healthRouter: router };
{% endif %}

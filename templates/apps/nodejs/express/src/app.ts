{% if enable_typescript -%}
import express, { Application, Request, Response, NextFunction } from 'express';
import helmet from 'helmet';
import cors from 'cors';
import compression from 'compression';
import morgan from 'morgan';

import { healthRouter } from './routes/health';
import { errorHandler } from './middleware/error';

// Create Express application
const app: Application = express();
const port: number = parseInt(process.env.PORT || '{{ app_port }}', 10);

// Security middleware
app.use(helmet());
app.use(cors());

// Compression and logging
app.use(compression());
app.use(morgan('combined'));

// Body parsing middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Routes
app.use('/health', healthRouter);

// Basic route
app.get('/', (req: Request, res: Response) => {
  res.json({
    message: 'Welcome to {{ app_name }}!',
    version: '{{ template_version }}',
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV || 'development'
  });
});

// API route example
app.get('/api/info', (req: Request, res: Response) => {
  res.json({
    app: '{{ app_name }}',
    description: '{{ description }}',
    version: '{{ template_version }}',
    node_version: process.version,
    platform: process.platform,
    arch: process.arch,
    uptime: process.uptime()
  });
});

// Error handling
app.use(errorHandler);

// 404 handler
app.use('*', (req: Request, res: Response) => {
  res.status(404).json({
    error: 'Not Found',
    message: `Route ${req.originalUrl} not found`,
    timestamp: new Date().toISOString()
  });
});

// Start server
const server = app.listen(port, '0.0.0.0', () => {
  console.log(`🚀 {{ app_name }} is running on port ${port}`);
  console.log(`📝 Environment: ${process.env.NODE_ENV || 'development'}`);
  console.log(`🔗 Health check: http://localhost:${port}/health`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully...');
  server.close(() => {
    console.log('Process terminated');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  console.log('SIGINT received. Shutting down gracefully...');
  server.close(() => {
    console.log('Process terminated');
    process.exit(0);
  });
});

export default app;
{% else -%}
const express = require('express');
const helmet = require('helmet');
const cors = require('cors');
const compression = require('compression');
const morgan = require('morgan');

const { healthRouter } = require('./routes/health');
const { errorHandler } = require('./middleware/error');

// Create Express application
const app = express();
const port = parseInt(process.env.PORT || '{{ app_port }}', 10);

// Security middleware
app.use(helmet());
app.use(cors());

// Compression and logging
app.use(compression());
app.use(morgan('combined'));

// Body parsing middleware
app.use(express.json({ limit: '10mb' }));
app.use(express.urlencoded({ extended: true, limit: '10mb' }));

// Routes
app.use('/health', healthRouter);

// Basic route
app.get('/', (req, res) => {
  res.json({
    message: 'Welcome to {{ app_name }}!',
    version: '{{ template_version }}',
    timestamp: new Date().toISOString(),
    environment: process.env.NODE_ENV || 'development'
  });
});

// API route example
app.get('/api/info', (req, res) => {
  res.json({
    app: '{{ app_name }}',
    description: '{{ description }}',
    version: '{{ template_version }}',
    node_version: process.version,
    platform: process.platform,
    arch: process.arch,
    uptime: process.uptime()
  });
});

// Error handling
app.use(errorHandler);

// 404 handler
app.use('*', (req, res) => {
  res.status(404).json({
    error: 'Not Found',
    message: `Route ${req.originalUrl} not found`,
    timestamp: new Date().toISOString()
  });
});

// Start server
const server = app.listen(port, '0.0.0.0', () => {
  console.log(`🚀 {{ app_name }} is running on port ${port}`);
  console.log(`📝 Environment: ${process.env.NODE_ENV || 'development'}`);
  console.log(`🔗 Health check: http://localhost:${port}/health`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('SIGTERM received. Shutting down gracefully...');
  server.close(() => {
    console.log('Process terminated');
    process.exit(0);
  });
});

process.on('SIGINT', () => {
  console.log('SIGINT received. Shutting down gracefully...');
  server.close(() => {
    console.log('Process terminated');
    process.exit(0);
  });
});

module.exports = app;
{% endif %}

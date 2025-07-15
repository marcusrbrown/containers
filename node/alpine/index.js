const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

// Middleware for JSON parsing
app.use(express.json());

// Health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    version: process.env.npm_package_version || '1.0.0',
    node_version: process.version,
    uptime: process.uptime()
  });
});

// Root endpoint
app.get('/', (req, res) => {
  res.json({
    message: 'Welcome to the Node.js Container Test Application',
    version: process.env.npm_package_version || '1.0.0',
    endpoints: {
      health: '/health',
      info: '/info'
    }
  });
});

// Info endpoint with system information
app.get('/info', (req, res) => {
  res.json({
    application: 'node-container-test',
    node_version: process.version,
    platform: process.platform,
    architecture: process.arch,
    memory_usage: process.memoryUsage(),
    environment: process.env.NODE_ENV || 'development',
    timestamp: new Date().toISOString()
  });
});

// Start the server
app.listen(port, () => {
  console.log(`🚀 Node.js container test app listening on port ${port}`);
  console.log(`📊 Health check available at: http://localhost:${port}/health`);
  console.log(`ℹ️  System info available at: http://localhost:${port}/info`);
  console.log(`🔧 Node.js version: ${process.version}`);
  console.log(`🏗️  Platform: ${process.platform} (${process.arch})`);
});

// Graceful shutdown
process.on('SIGTERM', () => {
  console.log('🛑 SIGTERM received, shutting down gracefully');
  process.exit(0);
});

process.on('SIGINT', () => {
  console.log('🛑 SIGINT received, shutting down gracefully');
  process.exit(0);
});

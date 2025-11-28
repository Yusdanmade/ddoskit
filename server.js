const http = require('http');
let requestCount = 0;
let startTime = Date.now();

const server = http.createServer((req, res) => {
  requestCount++;
  const currentTime = Date.now();
  const uptime = Math.floor((currentTime - startTime) / 1000);
  
  console.log(`[${new Date().toISOString()}] Request #${requestCount} from ${req.socket.remoteAddress || 'unknown'} - ${req.method} ${req.url}`);
  
  // Handle connection errors
  req.on('error', (err) => {
    console.log('Request error:', err.message);
  });
  
  res.on('error', (err) => {
    console.log('Response error:', err.message);
  });
  
  try {
    res.writeHead(200, {
      'Content-Type': 'text/html',
      'Connection': 'keep-alive',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type, Authorization'
    });
    
    res.end(`
      <!DOCTYPE html>
      <html>
      <head><title>DDoS Test Server</title></head>
      <body>
        <h1>🚀 DDoS Test Server Status</h1>
        <p>✅ Server is running and ready for attack!</p>
        <p>📊 Request Count: ${requestCount}</p>
        <p>⏱️ Uptime: ${uptime} seconds</p>
        <p>🕐 Current Time: ${new Date().toISOString()}</p>
        <p>🌐 Your IP: ${req.socket.remoteAddress || 'unknown'}</p>
        <p>🔧 Method: ${req.method}</p>
        <p>📍 URL: ${req.url}</p>
        <p>🔥 Ready for DDoS testing!</p>
      </body>
      </html>
    `);
  } catch (error) {
    console.log('Response write error:', error.message);
    try {
      res.writeHead(500);
      res.end('Server Error');
    } catch (e) {
      console.log('Final error:', e.message);
    }
  }
});

server.listen(8000, '127.0.0.1', () => {
  console.log('🚀 DDoS Test Server running at http://localhost:8000');
  console.log('📡 Server bound to 127.0.0.1:8000');
  console.log('🔥 Ready for DDoS attack testing!');
  console.log('📊 Monitoring requests...');
});

setInterval(() => {
  console.log(`[${new Date().toISOString()}] 📊 Status: ${requestCount} requests processed | 🚀 RPS: ${Math.round(requestCount / Math.max(1, (Date.now() - startTime) / 1000))}`);
}, 3000);
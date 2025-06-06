#!/usr/bin/env python3
"""
Test script to verify web server functionality for Render.com deployment
"""
import asyncio
from aiohttp import web
import os

PORT = int(os.environ.get('PORT', 10000))

async def health_check(request):
    """Health check endpoint for Render.com"""
    return web.Response(text="Server is running!", status=200)

async def status_endpoint(request):
    """Status endpoint showing server information"""
    response_data = {
        "status": "online",
        "port": PORT,
        "message": "Web server ready for Render.com deployment"
    }
    return web.json_response(response_data)

async def main():
    """Main function to start the web server"""
    app = web.Application()
    app.router.add_get('/', health_check)
    app.router.add_get('/health', health_check)
    app.router.add_get('/status', status_endpoint)
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '0.0.0.0', PORT)
    await site.start()
    print(f"Test server started on port {PORT}")
    print("Health check available at: /")
    print("Status endpoint available at: /status")
    
    # Keep server running
    try:
        await asyncio.Future()  # Run forever
    except KeyboardInterrupt:
        print("Server stopped")

if __name__ == "__main__":
    asyncio.run(main())
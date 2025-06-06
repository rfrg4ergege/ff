# Discord Game Status Bot

A Discord bot for tracking game/product status with admin controls, designed for deployment on Render.com.

## Features

- Track multiple games/products with status indicators
- Admin-only commands for adding, updating, and removing games
- Real-time status board with emoji indicators
- Web server for health checks (required for Render.com)
- Persistent data storage using JSON files

## Status Types

- 🟢 **Undetected** - Working normally
- 🔵 **Updating** - Currently being updated
- 🟠 **High Risk** - Potentially risky to use
- 🟡 **Testing** - Under testing
- 🔴 **Detected** - Not working/detected

## Commands

- `/addgame <name> <status>` - Add a new game to track (Admin only)
- `/setstatus <name> <status>` - Update game status (Admin only)
- `/removegame` - Remove games using selection menu (Admin only)
- `/updatestatusboard` - Manually refresh the status board (Admin only)
- `/listgames` - List all tracked games

## Deployment on Render.com

### Prerequisites

1. A Discord bot token from Discord Developer Portal
2. A Discord channel ID where the status board will be posted
3. A Render.com account

### Setup Steps

1. **Create Discord Bot:**
   - Go to Discord Developer Portal
   - Create a new application and bot
   - Copy the bot token
   - Invite bot to your server with appropriate permissions

2. **Deploy to Render:**
   - Connect your GitHub repository to Render
   - Create a new Web Service
   - Set environment variables:
     - `DISCORD_TOKEN` - Your Discord bot token
     - `CHANNEL_ID` - Discord channel ID for status board
   - Deploy the service

3. **Configure Admin Users:**
   - Update `ADMIN_IDS` in `main.py` with your Discord user IDs

### Environment Variables

- `DISCORD_TOKEN` - Discord bot token (required)
- `CHANNEL_ID` - Discord channel ID for status board (required)
- `PORT` - Web server port (automatically set by Render)

## File Structure

- `main.py` - Main bot application
- `render.yaml` - Render.com deployment configuration
- `runtime.txt` - Python version specification
- `requirements.txt` - Python dependencies
- `data/status.json` - Persistent data storage
- `.env` - Environment variables (for local development)

## Health Check

The bot includes a web server that responds to health checks at:
- `/` - Basic health check
- `/health` - Health check endpoint
- `/status` - Bot status information

This ensures the service stays alive on Render.com's platform.
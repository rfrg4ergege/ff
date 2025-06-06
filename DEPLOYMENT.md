# Render.com Deployment Guide

## Quick Setup

1. **Fork/Upload this repository to GitHub**

2. **Create a new Web Service on Render.com:**
   - Connect your GitHub repository
   - Choose "Web Service"
   - Select your repository

3. **Configure Build & Deploy Settings:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python main.py`
   - **Environment:** Python 3

4. **Set Environment Variables:**
   - `DISCORD_TOKEN` - Your Discord bot token
   - `CHANNEL_ID` - Discord channel ID where status board will appear

5. **Deploy the service**

## Getting Your Discord Credentials

### Discord Bot Token:
1. Go to https://discord.com/developers/applications
2. Create a new application or select existing one
3. Go to "Bot" section
4. Copy the token (click "Reset Token" if needed)
5. Add this as `DISCORD_TOKEN` environment variable

### Discord Channel ID:
1. Enable Developer Mode in Discord (User Settings > Advanced > Developer Mode)
2. Right-click on the channel where you want the status board
3. Click "Copy Channel ID"
4. Add this as `CHANNEL_ID` environment variable

### Bot Permissions:
Your bot needs these permissions in the target channel:
- Send Messages
- Use Slash Commands
- Embed Links
- Read Message History

## Admin Configuration

Update the `ADMIN_IDS` list in `main.py` with your Discord user IDs:

1. Enable Developer Mode in Discord
2. Right-click on your username
3. Click "Copy User ID"
4. Replace the IDs in the `ADMIN_IDS` list

## Health Check

The bot includes a web server that responds to health checks at:
- `/` - Basic "Bot is running!" message
- `/health` - Health check endpoint
- `/status` - JSON response with bot status

This ensures Render.com keeps the service alive.

## File Structure for Deployment

```
├── main.py              # Main bot application
├── requirements.txt     # Python dependencies (auto-generated)
├── runtime.txt         # Python version specification
├── render.yaml         # Render.com configuration
├── Procfile            # Process file for deployment
├── .env                # Local environment variables (not deployed)
├── data/               # Persistent data directory
│   └── status.json     # Game status storage
└── README.md           # Documentation
```

## Troubleshooting

**Bot not connecting:**
- Verify `DISCORD_TOKEN` is correct and not expired
- Check bot permissions in Discord server

**Commands not working:**
- Ensure your user ID is in `ADMIN_IDS`
- Verify bot has slash command permissions

**Status board not updating:**
- Check `CHANNEL_ID` is correct
- Verify bot can send messages in the channel

**Service not staying alive:**
- Health check endpoints should respond with 200 status
- Render.com automatically pings these endpoints
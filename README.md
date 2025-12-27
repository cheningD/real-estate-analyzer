# Real Estate Deal Analyzer - POC

Automated real estate deal monitoring and analysis system that filters Zillow MLS listings using AI and alerts your team via Discord.

## What It Does

1. **Monitors** new MLS listings from Zillow (Bridge API)
2. **Analyzes** each property with Claude AI against investment criteria
3. **Alerts** high-potential deals to Discord in real-time

## Architecture
```
MLS API (Zillow/Bridge)
    ↓
Fetch new listings
    ↓
Claude AI Analysis (filters by criteria)
    ↓
Discord Alert (if ALERT decision)
```

## Demo

![Discord Alert Example](screenshot.png)


## Current Implementation

- Uses mock data matching Bridge MLS API format (RESO standard)
- Claude Sonnet 4 for property analysis
- Discord webhooks for alerts
- Ready to integrate real MLS API credentials

## Setup

1. **Clone the repo**
```bash
git clone <this-repo>
cd real-estate-analyzer
```

2. **Create virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
```bash
cp .env.example .env
# Edit .env with your API keys:
# - ANTHROPIC_API_KEY (get from console.anthropic.com)
# - DISCORD_WEBHOOK_URL (from Discord server settings)
```

5. **Run the analyzer**
```bash
python main.py
```

## Next Steps for Production

- [ ] Integrate real Bridge MLS API with client credentials
- [ ] Add email monitoring (IMAP/Gmail API)
- [ ] Implement scheduling (run every 10 minutes via cron or AWS EventBridge)
- [ ] Add database for tracking analyzed properties (prevent duplicate alerts)
- [ ] Customize analysis criteria per client needs
- [ ] Add multiple notification channels (Slack, SMS, etc.)
- [ ] Deploy to AWS Lambda or similar serverless platform

## Tech Stack

- Python 3.9+
- Anthropic Claude API
- Discord Webhooks
- Bridge MLS API (RESO standard)

---

Built as POC in 4 hours - ready to customize for your specific investment criteria and deploy to production.
#!/bin/bash
# Start Triathlon Dashboard Backend

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Load Strava credentials
if [ -f /root/.secrets ]; then
    source /root/.secrets
    echo "✅ Loaded Strava credentials"
else
    echo "❌ Error: /root/.secrets not found"
    exit 1
fi

# Check required env vars
if [ -z "$STRAVA_CLIENT_ID" ] || [ -z "$STRAVA_ACCESS_TOKEN" ]; then
    echo "❌ Error: Missing Strava credentials"
    exit 1
fi

# Create venv if needed
if [ ! -d ".venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv .venv
    source .venv/bin/activate
    pip install flask flask-cors requests --quiet
else
    source .venv/bin/activate
fi

echo "🚴 Starting Triathlon Dashboard..."
echo "📍 Open: http://localhost:5000/"
echo ""

python3 server.py

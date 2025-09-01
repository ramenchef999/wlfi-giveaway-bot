#!/bin/bash

# 🚀 WLFI Giveaway - Google Cloud Deployment Script

# Configuration
PROJECT_ID="cryptotime-468703"  # Google Cloud Project ID
SERVICE_NAME="wlfi-giveaway"
REGION="us-central1"
BOT_TOKEN="8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s"

echo "🚀 WLFI Giveaway - Google Cloud Deployment"
echo "=========================================="

# Check if gcloud is installed
if ! command -v gcloud &> /dev/null; then
    echo "❌ Google Cloud CLI not found!"
    echo "📥 Install from: https://cloud.google.com/sdk/docs/install"
    exit 1
fi

# Check if logged in
if ! gcloud auth list --filter=status:ACTIVE --format="value(account)" | grep -q .; then
    echo "🔐 Please login to Google Cloud..."
    gcloud auth login
fi

# Set project
echo "📋 Setting project: $PROJECT_ID"
gcloud config set project $PROJECT_ID

# Enable required APIs
echo "🔧 Enabling required APIs..."
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com

# Build and deploy
echo "🏗️ Building container..."
gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME

echo "🚀 Deploying to Cloud Run..."
gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars BOT_TOKEN="$BOT_TOKEN"

# Get deployment URL
echo "📡 Getting deployment URL..."
URL=$(gcloud run services describe $SERVICE_NAME --region $REGION --format="value(status.url)")

echo ""
echo "✅ Deployment successful!"
echo "=========================================="
echo "🌐 App URL: $URL"
echo "🤖 Bot: @WLFI_AIR_BOT"
echo "📱 Mini App URL for BotFather: $URL"
echo ""
echo "🎯 Next steps:"
echo "1. Test the app: curl $URL/health"
echo "2. Update bot.js with the new URL"
echo "3. Setup Mini App with BotFather"
echo "4. Share with your community!"
echo ""
echo "🎉 Happy pranking! 😄"

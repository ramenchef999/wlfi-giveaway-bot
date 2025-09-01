# 🚀 Google Cloud Deployment Guide

## 📋 Prerequisites

1. **Google Cloud Account** (có free tier)
2. **Google Cloud CLI** (gcloud)
3. **Docker** (cho Cloud Run)

## 🛠️ Setup Google Cloud CLI

### 1. Install gcloud CLI
```bash
# macOS
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# Hoặc download từ: https://cloud.google.com/sdk/docs/install
```

### 2. Login và setup project
```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
```

## 🎯 Deployment Options

### Option 1: Google Cloud Run (Recommended)

#### 1. Enable APIs
```bash
gcloud services enable run.googleapis.com
gcloud services enable cloudbuild.googleapis.com
```

#### 2. Build và Deploy
```bash
# Build container
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/wlfi-giveaway

# Deploy to Cloud Run
gcloud run deploy wlfi-giveaway \
  --image gcr.io/YOUR_PROJECT_ID/wlfi-giveaway \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars BOT_TOKEN="8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s"
```

#### 3. Get URL
```bash
gcloud run services describe wlfi-giveaway --region us-central1 --format="value(status.url)"
```

### Option 2: Google App Engine

#### 1. Deploy
```bash
gcloud app deploy app.yaml
```

#### 2. Get URL
```bash
gcloud app browse
```

### Option 3: Google Compute Engine

#### 1. Create VM
```bash
gcloud compute instances create wlfi-giveaway \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --image-family=debian-11 \
  --image-project=debian-cloud \
  --tags=http-server,https-server
```

#### 2. SSH và setup
```bash
gcloud compute ssh wlfi-giveaway --zone=us-central1-a

# Trong VM:
sudo apt update
sudo apt install -y nodejs npm git
git clone YOUR_REPO
cd YOUR_REPO
npm install
npm start
```

## 🔧 Environment Variables

### Cloud Run
```bash
gcloud run services update wlfi-giveaway \
  --set-env-vars BOT_TOKEN="8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s" \
  --region us-central1
```

### App Engine
Đã cấu hình trong `app.yaml`

## 🌐 Custom Domain (Optional)

### 1. Map custom domain
```bash
gcloud run domain-mappings create \
  --service wlfi-giveaway \
  --domain your-domain.com \
  --region us-central1
```

### 2. Update DNS
- Thêm CNAME record: `your-domain.com` → `wlfi-giveaway-xxx-uc.a.run.app`

## 📊 Monitoring

### 1. View logs
```bash
gcloud logs tail --service=wlfi-giveaway
```

### 2. Monitor performance
- Vào Google Cloud Console
- Cloud Run → wlfi-giveaway → Metrics

## 💰 Cost Optimization

### Cloud Run (Recommended)
- **Free tier:** 2 million requests/month
- **Cost:** ~$0.40/million requests after free tier
- **Auto-scaling:** Chỉ trả tiền khi có traffic

### App Engine
- **Free tier:** 28 instance hours/day
- **Cost:** ~$0.05/hour after free tier

### Compute Engine
- **Free tier:** 1 e2-micro instance/month
- **Cost:** ~$5/month after free tier

## 🔒 Security

### 1. Environment Variables
```bash
# Set secret
echo -n "8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s" | \
gcloud secrets create bot-token --data-file=-

# Use secret
gcloud run services update wlfi-giveaway \
  --set-env-vars BOT_TOKEN="$(gcloud secrets versions access latest --secret=bot-token)" \
  --region us-central1
```

### 2. HTTPS
- Tự động enabled trên Cloud Run
- SSL certificate tự động

## 🚀 Quick Deploy Script

Tạo file `deploy.sh`:
```bash
#!/bin/bash

PROJECT_ID="your-project-id"
SERVICE_NAME="wlfi-giveaway"
REGION="us-central1"

echo "🚀 Deploying WLFI Giveaway to Google Cloud..."

# Build và deploy
gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME

gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated \
  --set-env-vars BOT_TOKEN="8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s"

# Get URL
URL=$(gcloud run services describe $SERVICE_NAME --region $REGION --format="value(status.url)")

echo "✅ Deployed successfully!"
echo "🌐 URL: $URL"
echo "🤖 Bot: @WLFI_AIR_BOT"
echo "📱 Update Mini App URL in BotFather: $URL"
```

## 🎯 Post-Deployment

### 1. Test deployment
```bash
curl https://your-app-url/health
```

### 2. Update bot.js
```javascript
const MINI_APP_URL = 'https://your-app-url';
```

### 3. Setup Mini App với BotFather
- Gửi `/newapp` cho @BotFather
- Chọn bot @WLFI_AIR_BOT
- App URL: `https://your-app-url`

## 🆘 Troubleshooting

### Common Issues:

1. **Permission denied**
   ```bash
   gcloud auth login
   gcloud config set project YOUR_PROJECT_ID
   ```

2. **Build fails**
   ```bash
   gcloud builds log BUILD_ID
   ```

3. **Service not accessible**
   ```bash
   gcloud run services update wlfi-giveaway --allow-unauthenticated
   ```

4. **Environment variables not set**
   ```bash
   gcloud run services describe wlfi-giveaway --format="value(spec.template.spec.containers[0].env)"
   ```

## 📞 Support

- [Google Cloud Documentation](https://cloud.google.com/docs)
- [Cloud Run Documentation](https://cloud.google.com/run/docs)
- [App Engine Documentation](https://cloud.google.com/appengine/docs)

---

**🎉 Happy Deploying! 🚀**

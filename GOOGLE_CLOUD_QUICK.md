# 🚀 Google Cloud - Quick Deploy

## ✅ **Files đã sẵn sàng:**
- `Dockerfile` - Container configuration
- `app.yaml` - App Engine configuration  
- `deploy.sh` - Automated deployment script
- `GOOGLE_CLOUD_DEPLOY.md` - Detailed guide

## 🎯 **3 Options Deploy:**

### **Option 1: Cloud Run (Recommended) - Free Tier**
```bash
# 1. Install gcloud CLI
curl https://sdk.cloud.google.com | bash
exec -l $SHELL

# 2. Login và setup
gcloud auth login
gcloud config set project YOUR_PROJECT_ID

# 3. Deploy tự động
./deploy.sh
```

### **Option 2: App Engine - Free Tier**
```bash
gcloud app deploy app.yaml
```

### **Option 3: Compute Engine - Free Tier**
```bash
gcloud compute instances create wlfi-giveaway \
  --zone=us-central1-a \
  --machine-type=e2-micro \
  --image-family=debian-11
```

## 💰 **Cost Comparison:**

| Platform | Free Tier | Cost After |
|----------|-----------|------------|
| **Cloud Run** | 2M requests/month | ~$0.40/M requests |
| **App Engine** | 28 hours/day | ~$0.05/hour |
| **Compute Engine** | 1 e2-micro/month | ~$5/month |

## 🚀 **Quick Start:**

### **1. Setup Google Cloud**
- Tạo account tại [cloud.google.com](https://cloud.google.com)
- Tạo project mới
- Enable billing (có free tier)

### **2. Install CLI**
```bash
curl https://sdk.cloud.google.com | bash
exec -l $SHELL
```

### **3. Deploy**
```bash
# Edit PROJECT_ID trong deploy.sh
nano deploy.sh

# Run deployment
./deploy.sh
```

### **4. Setup Bot**
- Copy URL từ deployment
- Update `bot.js` với URL mới
- Setup Mini App với BotFather

## 🎉 **Kết quả:**
- ✅ HTTPS URL tự động
- ✅ Auto-scaling
- ✅ Free tier available
- ✅ Professional hosting
- ✅ Bot + Mini App hoạt động

---

**🎯 Ready to deploy! 🚀**

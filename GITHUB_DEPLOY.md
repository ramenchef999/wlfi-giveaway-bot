# 🚀 GitHub Pages Deployment Guide

## ✅ **Files đã sẵn sàng:**
- `.github/workflows/deploy.yml` - GitHub Actions workflow
- `.github/workflows/static.yml` - Simple static deployment
- `GITHUB_DEPLOY.md` - Hướng dẫn này

## 🎯 **Cách Deploy GitHub Pages:**

### **Option 1: GitHub Actions (Recommended)**

1. **Tạo repository trên GitHub:**
   ```bash
   # Tạo repo mới trên GitHub.com
   # Tên: wlfi-giveaway-bot
   # Public hoặc Private
   ```

2. **Push code lên GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: WLFI Giveaway Bot"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/wlfi-giveaway-bot.git
   git push -u origin main
   ```

3. **Enable GitHub Pages:**
   - Vào repository → Settings
   - Pages → Source: "Deploy from a branch"
   - Branch: `gh-pages`
   - Save

4. **URL sẽ là:** `https://YOUR_USERNAME.github.io/wlfi-giveaway-bot`

### **Option 2: Manual Upload**

1. **Tạo repository trên GitHub**
2. **Upload files trực tiếp**
3. **Enable GitHub Pages từ Settings**

## 🎯 **Quick Deploy Script:**

Tạo file `deploy-github.sh`:
```bash
#!/bin/bash

echo "🚀 Deploying to GitHub Pages..."

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
fi

# Add all files
git add .

# Commit changes
git commit -m "Update WLFI Giveaway Bot"

# Push to GitHub
git push origin main

echo "✅ Deployed to GitHub Pages!"
echo "🌐 URL: https://YOUR_USERNAME.github.io/wlfi-giveaway-bot"
echo "🤖 Bot: @WLFI_AIR_BOT"
echo "📱 Update Mini App URL in BotFather"
```

## 💰 **GitHub Pages Free Features:**

- ✅ **Hoàn toàn free**
- ✅ **HTTPS tự động**
- ✅ **Custom domain support**
- ✅ **Auto-deploy từ git**
- ✅ **Unlimited bandwidth**
- ✅ **100GB storage**

## 🔧 **Setup Bot sau khi deploy:**

### 1. **Update bot.js với URL mới:**
```javascript
const MINI_APP_URL = 'https://YOUR_USERNAME.github.io/wlfi-giveaway-bot';
```

### 2. **Setup Mini App với BotFather:**
- Gửi `/newapp` cho @BotFather
- Chọn bot @WLFI_AIR_BOT
- App title: `WLFI Giveaway`
- App URL: `https://YOUR_USERNAME.github.io/wlfi-giveaway-bot`

## 🎉 **Kết quả:**

- ✅ **Free hosting**
- ✅ **HTTPS tự động**
- ✅ **Auto-deploy**
- ✅ **Professional URL**
- ✅ **Bot + Mini App hoạt động**

## 🆘 **Troubleshooting:**

### **GitHub Pages không load:**
- Check repository settings
- Verify branch name (gh-pages)
- Wait 5-10 minutes for first deploy

### **Bot không hoạt động:**
- Verify URL trong bot.js
- Check BotFather settings
- Test URL trong browser

---

**🎯 Ready to deploy! 🚀**

#!/bin/bash

echo "🚀 WLFI Giveaway - GitHub Pages Deployment"
echo "=========================================="

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git not found!"
    echo "📥 Install Git first"
    exit 1
fi

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📁 Initializing git repository..."
    git init
fi

# Add all files
echo "📦 Adding files to git..."
git add .

# Commit changes
echo "💾 Committing changes..."
git commit -m "Update WLFI Giveaway Bot - $(date)"

# Check if remote exists
if ! git remote get-url origin &> /dev/null; then
    echo "🔗 Please add remote origin:"
    echo "git remote add origin https://github.com/YOUR_USERNAME/wlfi-giveaway-bot.git"
    echo ""
    echo "📋 Then run this script again"
    exit 1
fi

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push origin main

echo ""
echo "✅ Deployed to GitHub Pages!"
echo "=========================================="
echo "🌐 URL: https://YOUR_USERNAME.github.io/wlfi-giveaway-bot"
echo "🤖 Bot: @WLFI_AIR_BOT"
echo ""
echo "🎯 Next steps:"
echo "1. Enable GitHub Pages in repository settings"
echo "2. Update bot.js with the new URL"
echo "3. Setup Mini App with BotFather"
echo "4. Share with your community!"
echo ""
echo "🎉 Happy pranking! 😄"

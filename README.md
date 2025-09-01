# WLFI Giveaway Telegram Mini App 🚀

A fun Telegram Mini App that pretends to be a WLFI token giveaway but reveals it's just a prank when users try to claim!

## Features ✨

- 🎁 Beautiful giveaway interface with WLFI token branding
- 💳 Wallet address input with validation
- 📱 Direct link to join @asteroid_community Telegram group
- 🎯 Claim button that reveals the prank message
- 🎨 Modern, responsive design with animations
- 📱 Full Telegram Mini App integration
- 🎊 Confetti effects and fun animations

## Screenshots 📸

The app features:
- Gradient background with rocket logo
- Prize display showing $WLFI tokens
- Requirements checklist
- Wallet input field
- Telegram community join button
- Claim button that triggers the prank

## Setup Instructions 🛠️

### Prerequisites
- Node.js (version 14 or higher)
- npm or yarn
- A web server or hosting service

### Local Development

1. **Clone or download the files**
   ```bash
   # If you have the files locally, navigate to the directory
   cd /path/to/your/mini-app
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Start the development server**
   ```bash
   npm run dev
   ```

4. **Open in browser**
   - Navigate to `http://localhost:3000`
   - The app will be available for testing

### Production Deployment

1. **Install dependencies**
   ```bash
   npm install --production
   ```

2. **Start the server**
   ```bash
   npm start
   ```

3. **Deploy to your hosting service**
   - Upload all files to your web server
   - Ensure HTTPS is enabled (required for Telegram Mini Apps)
   - Set up your domain

## Telegram Mini App Setup 🤖

### 1. Create a Bot
1. Message [@BotFather](https://t.me/botfather) on Telegram
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Save the bot token

### 2. Create Mini App
1. Send `/newapp` to BotFather
2. Select your bot
3. Choose "Mini App"
4. Set the app title: "WLFI Giveaway"
5. Set the short description: "Join our WLFI token giveaway!"
6. Upload an app icon (512x512 PNG)
7. Set the app URL to your deployed domain

### 3. Configure Mini App
1. Send `/myapps` to BotFather
2. Select your Mini App
3. Configure additional settings as needed

## File Structure 📁

```
wlfi-giveaway-mini-app/
├── index.html          # Main HTML file
├── styles.css          # CSS styles and animations
├── script.js           # JavaScript functionality
├── server.js           # Express server
├── package.json        # Dependencies and scripts
└── README.md           # This file
```

## How It Works 🔧

1. **User Interface**: Beautiful giveaway page with WLFI branding
2. **Wallet Input**: Users enter their Ethereum wallet address
3. **Validation**: JavaScript validates the wallet format
4. **Telegram Integration**: Direct link to join @asteroid_community
5. **Claim Process**: 
   - User clicks "Claim WLFI Tokens"
   - Loading animation plays
   - After 2 seconds, shows the prank message
   - "Chúc mừng! Bạn bị lừa rồi haha! 😂"

## Customization 🎨

### Colors
- Primary gradient: `#667eea` to `#764ba2`
- Success color: `#4CAF50`
- Error color: `#ff6b6b`
- Telegram blue: `#0088cc`

### Text
- Edit the Vietnamese prank message in `script.js` line 67
- Modify the giveaway title and description in `index.html`
- Update the Telegram community link

### Animations
- Confetti effect colors in `script.js` line 108
- Bounce animation for the rocket logo
- Slide-in animations for page elements

## Security Considerations 🔒

- The app only collects wallet addresses for the prank
- No real transactions or token transfers occur
- All data is processed client-side
- HTTPS is required for Telegram Mini Apps

## Troubleshooting 🐛

### Common Issues

1. **App not loading in Telegram**
   - Ensure HTTPS is enabled
   - Check that all files are accessible
   - Verify the domain is correctly set in BotFather

2. **Styling issues**
   - Clear browser cache
   - Check CSS file is loading correctly
   - Verify file paths are correct

3. **JavaScript errors**
   - Check browser console for errors
   - Ensure Telegram WebApp API is available
   - Verify all DOM elements exist

## Contributing 🤝

Feel free to fork this project and customize it for your own pranks! Just remember to:
- Keep it fun and harmless
- Don't collect sensitive information
- Respect Telegram's Mini App guidelines

## License 📄

MIT License - Feel free to use this for your own projects!

## Support 💬

If you need help setting up your Mini App, join the [Asteroid Community](https://t.me/asteroid_community) on Telegram!

---

**Disclaimer**: This is a harmless prank app. No real tokens are distributed, and no financial transactions occur. Use responsibly! 😄

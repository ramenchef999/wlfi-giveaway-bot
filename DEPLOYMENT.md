# Deployment Guide 🚀

This guide will help you deploy your WLFI Giveaway Telegram Mini App to various hosting platforms.

## Quick Deploy Options

### 1. Vercel (Recommended) ⚡

**Easiest option for static hosting:**

1. **Fork/Clone the repository**
2. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

3. **Deploy:**
   ```bash
   vercel
   ```

4. **Follow the prompts:**
   - Link to existing project: No
   - Project name: `wlfi-giveaway-mini-app`
   - Directory: `./` (current directory)
   - Override settings: No

5. **Set up for static hosting:**
   Create `vercel.json`:
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "*.html",
         "use": "@vercel/static"
       }
     ],
     "routes": [
       {
         "src": "/(.*)",
         "dest": "/$1"
       }
     ]
   }
   ```

### 2. Netlify 🌐

1. **Drag and drop method:**
   - Go to [netlify.com](https://netlify.com)
   - Drag your project folder to the deploy area
   - Your site will be live instantly

2. **Git deployment:**
   - Connect your GitHub repository
   - Set build command: `npm install`
   - Set publish directory: `.`
   - Deploy!

### 3. GitHub Pages 📄

1. **Create a new repository on GitHub**
2. **Upload your files**
3. **Go to Settings > Pages**
4. **Select source: Deploy from a branch**
5. **Choose main branch**
6. **Save - your site will be available at `https://username.github.io/repository-name`**

### 4. Heroku ☁️

1. **Install Heroku CLI**
2. **Login:**
   ```bash
   heroku login
   ```

3. **Create app:**
   ```bash
   heroku create your-app-name
   ```

4. **Deploy:**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push heroku main
   ```

5. **Open:**
   ```bash
   heroku open
   ```

## Custom Domain Setup 🌍

### For Vercel:
1. Go to your project dashboard
2. Settings > Domains
3. Add your custom domain
4. Update DNS records as instructed

### For Netlify:
1. Site settings > Domain management
2. Add custom domain
3. Configure DNS records

### For Heroku:
1. Settings > Domains
2. Add domain
3. Configure DNS

## SSL/HTTPS Setup 🔒

**Important:** Telegram Mini Apps require HTTPS!

### Vercel/Netlify:
- SSL is automatically enabled
- No additional setup needed

### Heroku:
- SSL is included with paid plans
- Free tier: Use Cloudflare for SSL

### Custom Server:
```bash
# Using Let's Encrypt
sudo certbot --nginx -d yourdomain.com
```

## Environment Variables ⚙️

Create a `.env` file for local development:

```env
PORT=3000
NODE_ENV=production
```

## Performance Optimization 🚀

### 1. Enable Compression
Add to your server:

```javascript
const compression = require('compression');
app.use(compression());
```

### 2. Cache Headers
```javascript
app.use(express.static(__dirname, {
  maxAge: '1d',
  etag: true
}));
```

### 3. Minify Assets
Use tools like:
- `terser` for JavaScript
- `cssnano` for CSS
- `html-minifier` for HTML

## Monitoring 📊

### 1. Uptime Monitoring
- [UptimeRobot](https://uptimerobot.com)
- [Pingdom](https://pingdom.com)

### 2. Error Tracking
- [Sentry](https://sentry.io)
- [LogRocket](https://logrocket.com)

## Troubleshooting 🔧

### Common Issues:

1. **App not loading in Telegram:**
   - Check HTTPS is enabled
   - Verify domain is correct in BotFather
   - Test URL in browser first

2. **CORS errors:**
   - Add CORS headers to server
   - Check domain whitelist

3. **Performance issues:**
   - Enable compression
   - Optimize images
   - Use CDN for static assets

### Debug Commands:

```bash
# Check if server is running
curl -I https://yourdomain.com

# Test SSL certificate
openssl s_client -connect yourdomain.com:443

# Check response time
curl -w "@curl-format.txt" -o /dev/null -s "https://yourdomain.com"
```

## Security Checklist ✅

- [ ] HTTPS enabled
- [ ] Security headers set
- [ ] No sensitive data in client-side code
- [ ] Input validation implemented
- [ ] Rate limiting (if needed)
- [ ] Regular security updates

## Support 🆘

If you encounter issues:

1. Check the [Telegram Mini Apps documentation](https://core.telegram.org/bots/webapps)
2. Join the [Asteroid Community](https://t.me/asteroid_community)
3. Check platform-specific documentation

---

**Happy Deploying! 🎉**

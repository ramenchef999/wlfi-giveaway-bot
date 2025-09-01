# 🤖 Telegram Bot Setup Guide

## Bot đã được tạo thành công!

**Bot Token:** `8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s`

## 📋 Các bước tiếp theo:

### 1. Tìm Bot của bạn
- Tìm bot bằng username (sẽ hiện trong console khi chạy)
- Hoặc tìm bằng Bot ID: `8353170585`

### 2. Test Bot Commands
Gửi các lệnh sau cho bot:
- `/start` - Bắt đầu giveaway
- `/help` - Xem hướng dẫn
- `/info` - Thông tin giveaway

### 3. Deploy Mini App

#### Option A: Deploy lên Vercel (Khuyến nghị)

1. **Cài đặt Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```

3. **Làm theo hướng dẫn:**
   - Link to existing project: No
   - Project name: `wlfi-giveaway-bot`
   - Directory: `./`
   - Override settings: No

4. **Sau khi deploy xong, copy URL (ví dụ: `https://your-app.vercel.app`)**

#### Option B: Deploy lên Netlify

1. **Tạo file `netlify.toml`:**
   ```toml
   [build]
     publish = "."
     command = "npm install"
   
   [[redirects]]
     from = "/*"
     to = "/index.html"
     status = 200
   ```

2. **Upload files lên Netlify**
3. **Copy URL sau khi deploy**

### 4. Cấu hình Mini App với BotFather

1. **Gửi `/newapp` cho @BotFather**
2. **Chọn bot của bạn**
3. **Điền thông tin:**
   - **App title:** `WLFI Giveaway`
   - **Short description:** `Join our WLFI token giveaway!`
   - **App URL:** `https://your-deployed-url.com` (URL từ bước 3)
   - **App icon:** Upload icon 512x512 PNG

### 5. Cập nhật Mini App URL

Sau khi có URL deploy, cập nhật trong file `bot.js`:

```javascript
const MINI_APP_URL = 'https://your-deployed-url.com'; // Thay URL thật vào đây
```

### 6. Test hoàn chỉnh

1. **Gửi `/start` cho bot**
2. **Click "🎁 Tham Gia Giveaway"**
3. **Test toàn bộ flow:**
   - Nhập ví
   - Join community
   - Click claim
   - Xem prank message

## 🎯 Bot Features

### Commands:
- `/start` - Bắt đầu giveaway với nút Mini App
- `/help` - Hướng dẫn sử dụng
- `/info` - Thông tin về giveaway

### Mini App Integration:
- Nút "🎁 Tham Gia Giveaway" mở Mini App
- Nút "📱 Join Community" link tới @asteroid_community
- Nhận data từ Mini App khi user claim
- Log thông tin user và wallet

### Prank Flow:
1. User click "Tham Gia Giveaway"
2. Mini App mở với giao diện đẹp
3. User nhập ví và click claim
4. Loading 2 giây
5. **"Chúc mừng! Bạn bị lừa rồi haha! 😂"**

## 🔧 Troubleshooting

### Bot không phản hồi:
- Kiểm tra token có đúng không
- Đảm bảo server đang chạy
- Check console logs

### Mini App không mở:
- Đảm bảo URL deploy có HTTPS
- Kiểm tra URL trong BotFather
- Test URL trong browser trước

### Deploy lỗi:
- Kiểm tra file `vercel.json`
- Đảm bảo tất cả files được upload
- Check Vercel logs

## 📊 Monitoring

### Logs:
- Bot interactions được log trong console
- Claim attempts được ghi lại
- User info và wallet addresses

### Health Check:
- `https://your-domain.com/health`
- Trả về status của bot và Mini App

## 🚀 Production Tips

1. **Environment Variables:**
   - Sử dụng env vars cho bot token
   - Không commit token vào git

2. **Security:**
   - HTTPS bắt buộc cho Mini App
   - Validate tất cả inputs
   - Rate limiting nếu cần

3. **Performance:**
   - Cache static files
   - Optimize images
   - Use CDN

## 🎉 Kết quả mong đợi

Sau khi setup xong:
- Bot phản hồi các commands
- Mini App mở được từ bot
- Prank hoạt động hoàn hảo
- User bị lừa một cách vui vẻ! 😄

---

**Chúc bạn thành công với prank giveaway! 🚀**

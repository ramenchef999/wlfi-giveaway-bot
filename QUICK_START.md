# 🚀 WLFI Giveaway Bot - Quick Start

## ✅ Đã hoàn thành:

### 🤖 Bot đã sẵn sàng!
- **Bot Token:** `8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s`
- **Status:** ✅ Đang chạy tại `http://localhost:3000`
- **Health Check:** ✅ OK

### 📱 Mini App đã sẵn sàng!
- **Local URL:** `http://localhost:3000`
- **Status:** ✅ Hoạt động
- **Features:** ✅ Đầy đủ

## 🎯 Bước tiếp theo - Deploy lên hosting:

### 1. Deploy lên Vercel (Khuyến nghị)
```bash
npm i -g vercel
vercel
```

### 2. Sau khi có URL deploy, cập nhật trong `bot.js`:
```javascript
const MINI_APP_URL = 'https://your-deployed-url.vercel.app';
```

### 3. Setup Mini App với BotFather:
- Gửi `/newapp` cho @BotFather
- Chọn bot của bạn
- App title: `WLFI Giveaway`
- App URL: URL deploy từ bước 1

## 🧪 Test ngay bây giờ:

### Test Bot Commands:
1. Tìm bot bằng ID: `8353170585`
2. Gửi `/start`
3. Gửi `/help`
4. Gửi `/info`

### Test Mini App:
1. Mở `http://localhost:3000`
2. Nhập ví: `0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6`
3. Click "Join @asteroid_community"
4. Click "Claim WLFI Tokens"
5. **Kết quả:** "Chúc mừng! Bạn bị lừa rồi haha! 😂"

## 📁 Files quan trọng:

- `bot.js` - Bot chính với API key
- `index.html` - Giao diện Mini App
- `styles.css` - Styling đẹp
- `script.js` - Logic prank
- `vercel.json` - Cấu hình deploy
- `package.json` - Dependencies

## 🎉 Kết quả mong đợi:

1. **Bot phản hồi commands**
2. **Mini App mở từ bot**
3. **User nhập ví và claim**
4. **Prank message hiện ra**
5. **User bị lừa vui vẻ! 😄**

---

**Bot đã sẵn sàng! Chỉ cần deploy và setup Mini App! 🚀**

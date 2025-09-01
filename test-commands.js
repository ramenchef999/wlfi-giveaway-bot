const TelegramBot = require('node-telegram-bot-api');

// Bot configuration
const token = '8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s';
const bot = new TelegramBot(token, { polling: true });

console.log('🤖 Bot test started...');
console.log('📱 Send /start, /help, or /info to test commands');
console.log('🔗 Bot: @WLFI_AIR_BOT');

// Test commands
bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    const username = msg.from.first_name;
    
    console.log(`✅ Received /start from ${username} (${chatId})`);
    
    const welcomeMessage = `🚀 Chào mừng ${username} đến với WLFI Giveaway!

🎁 Tham gia giveaway $WLFI tokens ngay bây giờ!

📱 Click nút bên dưới để mở Mini App và tham gia giveaway.`;

    const keyboard = {
        inline_keyboard: [
            [{
                text: '🎁 Tham Gia Giveaway',
                web_app: { url: 'http://localhost:3000' }
            }],
            [{
                text: '📱 Join Community',
                url: 'https://t.me/asteroid_community'
            }]
        ]
    };

    bot.sendMessage(chatId, welcomeMessage, {
        reply_markup: keyboard
    }).then(() => {
        console.log('✅ Welcome message sent successfully');
    }).catch((error) => {
        console.error('❌ Error sending message:', error.message);
    });
});

bot.onText(/\/help/, (msg) => {
    const chatId = msg.chat.id;
    console.log(`✅ Received /help from ${msg.from.first_name} (${chatId})`);
    
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
    console.log(`✅ Received /info from ${msg.from.first_name} (${chatId})`);
    
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

// Handle all messages for debugging
bot.on('message', (msg) => {
    if (!msg.text?.startsWith('/')) {
        console.log(`📨 Received message: "${msg.text}" from ${msg.from.first_name}`);
    }
});

// Error handling
bot.on('error', (error) => {
    console.error('❌ Bot error:', error);
});

bot.on('polling_error', (error) => {
    console.error('❌ Polling error:', error);
});

console.log('🎉 Bot is ready to receive messages!');
console.log('💡 Send /start to test the giveaway flow');

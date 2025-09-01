const TelegramBot = require('node-telegram-bot-api');

// Bot configuration
const token = '8353170585:AAEReZBd8UslP_aTV9K7Au4VEPTQSu2FC9s';
const bot = new TelegramBot(token);

// Test bot info
async function testBot() {
    try {
        console.log('🤖 Testing bot...');
        
        // Get bot info
        const botInfo = await bot.getMe();
        console.log('✅ Bot info:');
        console.log(`   Name: ${botInfo.first_name}`);
        console.log(`   Username: @${botInfo.username}`);
        console.log(`   ID: ${botInfo.id}`);
        console.log(`   Can join groups: ${botInfo.can_join_groups}`);
        console.log(`   Can read all group messages: ${botInfo.can_read_all_group_messages}`);
        console.log(`   Supports inline queries: ${botInfo.supports_inline_queries}`);
        
        // Test webhook info
        const webhookInfo = await bot.getWebhookInfo();
        console.log('\n📡 Webhook info:');
        console.log(`   URL: ${webhookInfo.url || 'Not set'}`);
        console.log(`   Has custom certificate: ${webhookInfo.has_custom_certificate}`);
        console.log(`   Pending update count: ${webhookInfo.pending_update_count}`);
        console.log(`   Last error date: ${webhookInfo.last_error_date || 'None'}`);
        console.log(`   Last error message: ${webhookInfo.last_error_message || 'None'}`);
        
        console.log('\n🎉 Bot is working correctly!');
        console.log('📱 You can now test with commands: /start, /help, /info');
        
    } catch (error) {
        console.error('❌ Bot test failed:', error.message);
    }
}

// Run test
testBot();

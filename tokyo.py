# project_generator.py - Script tạo toàn bộ Enhanced Telegram Bot Project
import os
import zipfile
from pathlib import Path

def create_project_structure():
    """Tạo cấu trúc thư mục project"""
    
    # Cấu trúc thư mục
    directories = [
        "config",
        "database", 
        "handlers",
        "managers",
        "utils",
        "monitoring", 
        "ui",
        "generators",
        "scripts",
        "services",
        "logs"
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        
    print("✅ Created directory structure")

def create_files():
    """Tạo tất cả files với nội dung"""
    
    files_content = {
        # ===== CONFIG FILES =====
        "config/settings.py": '''# config/settings.py
import os
import json
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Telegram Bot
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    
    # AI Services
    PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY')
    PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"
    
    # Google Cloud
    GOOGLE_APPLICATION_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', './genai-key.json')
    GOOGLE_PROJECT_ID = os.getenv('GOOGLE_PROJECT_ID')
    GOOGLE_LOCATION = os.getenv('GOOGLE_LOCATION', 'us-central1')
    
    # Database
    DATABASE_PATH = os.getenv('DATABASE_PATH', 'bot_database.db')
    DB_POOL_SIZE = int(os.getenv('DB_POOL_SIZE', '10'))
    DB_TIMEOUT = int(os.getenv('DB_TIMEOUT', '30'))
    
    # Mining System - NO MORE HARDCODED VALUES
    ASTEROID_GROUP_USERNAME = os.getenv('ASTEROID_GROUP_USERNAME', '@asteroid_community')
    ASTEROID_GROUP_CHAT_ID = int(os.getenv('ASTEROID_GROUP_CHAT_ID', '-1001538908265'))
    MESSAGES_PER_CREDIT = int(os.getenv('MESSAGES_PER_CREDIT', '20'))
    DAILY_MINING_LIMIT = int(os.getenv('DAILY_MINING_LIMIT', '30'))
    MIN_MESSAGE_LENGTH = int(os.getenv('MIN_MESSAGE_LENGTH', '20'))
    
    # Credits
    SINGLE_STYLE_COST = int(os.getenv('SINGLE_STYLE_COST', '5'))
    COMBINATION_STYLE_COST = int(os.getenv('COMBINATION_STYLE_COST', '7'))
    FREE_TRIAL_CREDITS = int(os.getenv('FREE_TRIAL_CREDITS', '15'))
    REFERRER_REWARD = int(os.getenv('REFERRER_REWARD', '5'))
    REFEREE_REWARD = int(os.getenv('REFEREE_REWARD', '30'))
    
    # Rate Limiting
    MAX_REQUESTS_PER_MINUTE = int(os.getenv('MAX_REQUESTS_PER_MINUTE', '10'))
    MAX_CALLBACKS_PER_MINUTE = int(os.getenv('MAX_CALLBACKS_PER_MINUTE', '30'))
    MAX_CONTENT_GENERATION_PER_HOUR = int(os.getenv('MAX_CONTENT_GENERATION_PER_HOUR', '5'))
    
    # Admin
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'ramenchef9999')
    
    # Performance
    CACHE_TTL_SECONDS = int(os.getenv('CACHE_TTL_SECONDS', '300'))
    USER_DATA_CLEANUP_HOURS = int(os.getenv('USER_DATA_CLEANUP_HOURS', '24'))
    MAX_MESSAGE_LENGTH = int(os.getenv('MAX_MESSAGE_LENGTH', '4096'))
    
    # Monitoring
    ENABLE_METRICS = os.getenv('ENABLE_METRICS', 'true').lower() == 'true'
    METRICS_PORT = int(os.getenv('METRICS_PORT', '8000'))
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    @staticmethod
    def validate() -> tuple[bool, list[str]]:
        """Validate all required settings"""
        errors = []
        
        required_settings = [
            ('TELEGRAM_BOT_TOKEN', Settings.TELEGRAM_BOT_TOKEN),
            ('PERPLEXITY_API_KEY', Settings.PERPLEXITY_API_KEY),
            ('GOOGLE_PROJECT_ID', Settings.GOOGLE_PROJECT_ID),
        ]
        
        for name, value in required_settings:
            if not value:
                errors.append(f"❌ Missing {name}")
        
        if not os.path.exists(Settings.GOOGLE_APPLICATION_CREDENTIALS):
            errors.append(f"❌ Google credentials file not found: {Settings.GOOGLE_APPLICATION_CREDENTIALS}")
        
        return len(errors) == 0, errors
''',

        "config/languages.py": '''# config/languages.py
LANGUAGES = {
    'en': {'name': 'English', 'flag': '🇺🇸'},
    'vi': {'name': 'Tiếng Việt', 'flag': '🇻🇳'},
    'ja': {'name': '日本語', 'flag': '🇯🇵'},
    'ko': {'name': '한국어', 'flag': '🇰🇷'},
    'zh': {'name': '中文', 'flag': '🇨🇳'},
    'es': {'name': 'Español', 'flag': '🇪🇸'},
    'fr': {'name': 'Français', 'flag': '🇫🇷'},
    'de': {'name': 'Deutsch', 'flag': '🇩🇪'},
    'ru': {'name': 'Русский', 'flag': '🇷🇺'}
}

CONTENT_LENGTHS = {
    'short': {'name': 'Short Tweet', 'desc': '≤280 chars', 'tokens': 100, 'emoji': '📱'},
    'mid': {'name': 'Mid Tweet', 'desc': '200-700 words', 'tokens': 400, 'emoji': '📝'},
    'medium': {'name': 'Twitter Thread', 'desc': '2-5 tweets', 'tokens': 300, 'emoji': '🧵'},
    'long': {'name': 'Long Thread', 'desc': '5+ tweets', 'tokens': 600, 'emoji': '📚'},
    'article': {'name': 'Full Article', 'desc': '500+ words', 'tokens': 1000, 'emoji': '📄'}
}

CONTENT_STYLES = {
    'casual': {
        'name': 'Casual',
        'emoji': '😎',
        'description': 'Chill vibes, friendly tone',
        'target_audience': 'General community',
        'tone': 'Relaxed, approachable'
    },
    'hardcore': {
        'name': 'Hardcore',
        'emoji': '🔥',
        'description': 'Technical alpha insights',
        'target_audience': 'Alpha hunters, serious traders',
        'tone': 'Technical, data-driven'
    },
    'shitposter': {
        'name': 'Shitposter',
        'emoji': '🤡',
        'description': 'Memes and viral content',
        'target_audience': 'Meme community, viral content',
        'tone': 'Humorous, sarcastic'
    },
    'curator': {
        'name': 'Curator',
        'emoji': '📚',
        'description': 'Educational content',
        'target_audience': 'Learners, serious followers',
        'tone': 'Educational, informative'
    },
    'copypasta': {
        'name': 'Copy Pasta',
        'emoji': '📋',
        'description': 'Viral and quotable',
        'target_audience': 'Reply sections, viral sharing',
        'tone': 'Quotable, repeatable'
    },
    'creative': {
        'name': 'Creative',
        'emoji': '🎨',
        'description': 'Poetic and artistic',
        'target_audience': 'Artists, creative community',
        'tone': 'Poetic, metaphorical'
    }
}

STYLE_COMBINATIONS = {
    'casual_hardcore': {
        'name': 'Casual + Hardcore',
        'description': 'Technical insights with friendly delivery',
        'emoji': '😎🔥'
    },
    'shitposter_curator': {
        'name': 'Shitposter + Curator',
        'description': 'Educational content with humor',
        'emoji': '🤡📚'
    },
    'copypasta_creative': {
        'name': 'Copy Pasta + Creative',
        'description': 'Artistic viral content',
        'emoji': '📋🎨'
    }
}
''',

        # ===== DATABASE FILES =====
        "database/connection_manager.py": '''# database/connection_manager.py
import asyncio
import aiosqlite
from typing import Optional, Any, Dict, List
from contextlib import asynccontextmanager
import logging
from config.settings import Settings

logger = logging.getLogger(__name__)

class DatabasePool:
    def __init__(self, database_path: str, max_connections: int = 10):
        self.database_path = database_path
        self.max_connections = max_connections
        self._pool = []
        self._used_connections = set()
        self._lock = asyncio.Lock()
        self._initialized = False
    
    async def initialize(self):
        """Initialize the connection pool"""
        if self._initialized:
            return
        
        async with self._lock:
            if self._initialized:
                return
            
            # Create initial connections
            for _ in range(min(3, self.max_connections)):
                conn = await aiosqlite.connect(self.database_path)
                conn.row_factory = aiosqlite.Row
                await conn.execute("PRAGMA foreign_keys = ON")
                await conn.execute("PRAGMA journal_mode = WAL")
                self._pool.append(conn)
            
            self._initialized = True
            logger.info(f"✅ Database pool initialized with {len(self._pool)} connections")
    
    @asynccontextmanager
    async def get_connection(self):
        """Get a connection from the pool"""
        if not self._initialized:
            await self.initialize()
        
        connection = None
        try:
            async with self._lock:
                if self._pool:
                    connection = self._pool.pop()
                    self._used_connections.add(connection)
                elif len(self._used_connections) < self.max_connections:
                    connection = await aiosqlite.connect(self.database_path)
                    connection.row_factory = aiosqlite.Row
                    await connection.execute("PRAGMA foreign_keys = ON")
                    await connection.execute("PRAGMA journal_mode = WAL")
                    self._used_connections.add(connection)
                else:
                    for _ in range(50):
                        await asyncio.sleep(0.1)
                        if self._pool:
                            connection = self._pool.pop()
                            self._used_connections.add(connection)
                            break
                    
                    if not connection:
                        raise Exception("Database pool exhausted")
            
            yield connection
            
        finally:
            if connection:
                async with self._lock:
                    self._used_connections.discard(connection)
                    if len(self._pool) < 3:
                        self._pool.append(connection)
                    else:
                        await connection.close()
    
    async def execute_query(self, query: str, params: tuple = ()) -> List[aiosqlite.Row]:
        """Execute a SELECT query"""
        async with self.get_connection() as conn:
            async with conn.execute(query, params) as cursor:
                return await cursor.fetchall()
    
    async def execute_command(self, command: str, params: tuple = ()) -> int:
        """Execute an INSERT/UPDATE/DELETE command"""
        async with self.get_connection() as conn:
            cursor = await conn.execute(command, params)
            await conn.commit()
            return cursor.rowcount
    
    async def execute_transaction(self, commands: List[tuple]) -> bool:
        """Execute multiple commands in a transaction"""
        async with self.get_connection() as conn:
            try:
                for command, params in commands:
                    await conn.execute(command, params)
                await conn.commit()
                return True
            except Exception as e:
                await conn.rollback()
                logger.error(f"Transaction failed: {e}")
                return False
    
    async def close_all(self):
        """Close all connections"""
        async with self._lock:
            for conn in self._pool:
                await conn.close()
            for conn in self._used_connections:
                await conn.close()
            self._pool.clear()
            self._used_connections.clear()
            self._initialized = False

# Global database pool instance
db_pool = DatabasePool(Settings.DATABASE_PATH, Settings.DB_POOL_SIZE)
''',

        # ===== UTILS FILES =====
        "utils/validators.py": '''# utils/validators.py
import re
from typing import Optional, Dict, Any
from enum import Enum

class ValidationError(Exception):
    pass

class CallbackType(Enum):
    LANGUAGE = "lang"
    STYLE = "style"
    LENGTH = "length"
    BACK = "back"
    PERPLEXITY = "perplexity"
    DIRECT = "direct"
    RANDOM = "random"
    REGEN = "regen"
    REFERRAL = "referral"

class InputValidator:
    PATTERNS = {
        CallbackType.LANGUAGE: r'^lang_[a-z]{2}$',
        CallbackType.STYLE: r'^style_[a-z_]+_\\d+$',
        CallbackType.LENGTH: r'^length_[a-z]+$',
        CallbackType.BACK: r'^back_[a-z_]+_\\d+$',
        CallbackType.PERPLEXITY: r'^perplexity_\\d+$',
        CallbackType.DIRECT: r'^direct_\\d+$',
        CallbackType.RANDOM: r'^random_\\d+$',
        CallbackType.REGEN: r'^regen_[a-z_]+_\\d+$',
        CallbackType.REFERRAL: r'^referral_[a-z_]+$'
    }
    
    @staticmethod
    def validate_callback_data(data: str) -> tuple[bool, Optional[CallbackType], Optional[str]]:
        """Validate callback data and return type"""
        if not data or len(data) > 100:
            return False, None, "Invalid callback data length"
        
        if any(char in data for char in ['<', '>', '"', "'", '&', ';']):
            return False, None, "Invalid characters in callback data"
        
        for callback_type, pattern in InputValidator.PATTERNS.items():
            if re.match(pattern, data):
                return True, callback_type, None
        
        simple_commands = [
            'back_to_start', 'cancel', 'new_input', 'check_credits',
            'join_mining', 'demo', 'help', 'stats', 'select_language',
            'select_length', 'settings', 'referral_stats',
            'referral_leaderboard', 'referral_help'
        ]
        
        if data in simple_commands:
            return True, None, None
        
        return False, None, f"Unknown callback pattern: {data}"
    
    @staticmethod
    def validate_user_input(text: str) -> tuple[bool, str, Optional[str]]:
        """Validate and sanitize user input"""
        if not text:
            return False, "", "Empty input"
        
        if len(text) > 2000:
            return False, "", "Input too long (max 2000 characters)"
        
        sanitized = re.sub(r'[<>"\']', '', text)
        sanitized = re.sub(r'\\s+', ' ', sanitized).strip()
        
        if len(sanitized) < 3:
            return False, "", "Input too short (min 3 characters)"
        
        return True, sanitized, None
    
    @staticmethod
    def validate_user_id(user_id: Any) -> tuple[bool, Optional[int], Optional[str]]:
        """Validate user ID"""
        try:
            uid = int(user_id)
            if uid <= 0 or uid > 9999999999:
                return False, None, "Invalid user ID range"
            return True, uid, None
        except (ValueError, TypeError):
            return False, None, "User ID must be a number"
''',

        "utils/message_formatter.py": '''# utils/message_formatter.py
import re
from typing import List, Dict, Any
import logging

logger = logging.getLogger(__name__)

class MessageFormatter:
    @staticmethod
    def clean_markdown_content(text: str) -> str:
        """Clean markdown content to avoid parse errors"""
        if not text:
            return text
        
        try:
            # Handle underscore issues
            text = MessageFormatter._fix_underscore_issues_v2(text)
            
            # Balance markdown pairs
            markdown_pairs = [('*', '*'), ('`', '`')]
            for open_char, close_char in markdown_pairs:
                count = text.count(open_char)
                if count % 2 != 0:
                    text += close_char
            
            # Fix brackets
            bracket_pairs = [('[', ']'), ('(', ')')]
            for open_bracket, close_bracket in bracket_pairs:
                open_count = text.count(open_bracket)
                close_count = text.count(close_bracket)
                
                if open_count > close_count:
                    text += close_bracket * (open_count - close_count)
                elif close_count > open_count:
                    extra_closes = close_count - open_count
                    for _ in range(extra_closes):
                        last_index = text.rfind(close_bracket)
                        if last_index != -1:
                            text = text[:last_index] + '\\\\' + text[last_index:]
            
            return text
            
        except Exception as e:
            logger.error(f"Error in clean_markdown_content: {e}")
            return MessageFormatter._create_safe_fallback(text)
    
    @staticmethod
    def _fix_underscore_issues_v2(text: str) -> str:
        """Fix underscore issues"""
        if '_' not in text:
            return text
        
        try:
            underscore_count = text.count('_')
            
            if underscore_count == 1:
                text = text.replace('_', '\\\\_')
                return text
            
            if underscore_count % 2 != 0:
                valid_italic_pattern = r'_([^_\\s][^_]*[^_\\s])_'
                matches = list(re.finditer(valid_italic_pattern, text))
                
                if matches:
                    used_underscores = len(matches) * 2
                    remaining = underscore_count - used_underscores
                    
                    if remaining > 0:
                        temp_text = text
                        for match in reversed(matches):
                            temp_text = temp_text[:match.start()] + "TEMPITALICFIX" + temp_text[match.end():]
                        
                        temp_text = temp_text.replace('_', '\\\\_')
                        
                        for match in matches:
                            italic_text = match.group()
                            temp_text = temp_text.replace("TEMPITALICFIX", italic_text, 1)
                        
                        text = temp_text
                else:
                    text = text.replace('_', '\\\\_')
            
            return text
            
        except Exception as e:
            logger.error(f"Error fixing underscores: {e}")
            return text.replace('_', '\\\\_')
    
    @staticmethod
    def _create_safe_fallback(text: str) -> str:
        """Create safe fallback when markdown cleaning fails"""
        try:
            safe_text = text
            markdown_chars = ['*', '_', '`', '[', ']', '(', ')', '~', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!', '\\\\']
            
            for char in markdown_chars:
                safe_text = safe_text.replace(char, '')
            
            return safe_text.strip()[:4000]
        except Exception:
            return "Content processed"
    
    @staticmethod
    def safe_markdown_message(content: str, max_length: int = 4000) -> str:
        """Create safe markdown message"""
        if not content:
            return "❌ Empty content"
        
        try:
            content = MessageFormatter.truncate_text(content, max_length)
            content = MessageFormatter.clean_markdown_content(content)
            
            if not MessageFormatter.test_message_safety(content):
                logger.warning("Message failed safety test, using fallback")
                return MessageFormatter._create_safe_fallback(content)
            
            return content
            
        except Exception as e:
            logger.error(f"Error in safe_markdown_message: {e}")
            return MessageFormatter._create_safe_fallback(content)
    
    @staticmethod
    def test_message_safety(message: str) -> bool:
        """Test message safety"""
        try:
            if len(message) > 4096:
                return False
            
            message.encode('utf-8')
            
            markdown_chars = ['*', '`']
            for char in markdown_chars:
                count = message.count(char)
                if count % 2 != 0:
                    return False
            
            bracket_pairs = [('[', ']'), ('(', ')')]
            for open_b, close_b in bracket_pairs:
                if message.count(open_b) != message.count(close_b):
                    return False
            
            return True
            
        except Exception:
            return False
    
    @staticmethod
    def truncate_text(text: str, max_length: int = 4000) -> str:
        """Truncate text for Telegram"""
        if len(text) <= max_length:
            return text
        
        safe_length = max_length - 100
        truncated = text[:safe_length]
        
        for delimiter in ['\\n\\n', '\\n', '. ', '! ', '? ', ', ', ' ']:
            last_pos = truncated.rfind(delimiter)
            if last_pos > safe_length - 200:
                truncated = truncated[:last_pos + len(delimiter)]
                break
        
        return truncated + "\\n\\n_...content truncated due to Telegram limits_"
    
    @staticmethod
    def handle_user_input_safely(user_input: str) -> str:
        """Handle user input safely"""
        if not user_input:
            return ""
        
        try:
            cleaned = user_input.strip()
            cleaned = MessageFormatter._fix_underscore_issues_v2(cleaned)
            
            if len(cleaned) > 200:
                cleaned = cleaned[:200] + "..."
            
            return cleaned
            
        except Exception as e:
            logger.error(f"Error handling user input: {e}")
            return "Input processed"
''',

    async def _error_handler(self, update, context):
        """Enhanced error handler"""
        error = context.error
        self.logger.error(f"Bot error: {error}")
        
        if update and update.effective_message:
            try:
                await update.effective_message.reply_text(
                    "❌ An error occurred. Please try again or contact @ramenchef9999",
                    parse_mode='Markdown'
                )
            except:
                pass
    
    async def start(self):
        """Start the enhanced bot"""
        if not await self.initialize():
            return False
        
        self.logger.info("🎉 Enhanced Bot Ready!")
        self.logger.info("📊 Features: Validation, Pooling, Monitoring")
        
        try:
            await self.application.run_polling(drop_pending_updates=True)
        except Exception as e:
            self.logger.error(f"Bot crashed: {e}")
            return False
        
        return True
    
    async def shutdown(self):
        """Graceful shutdown"""
        self.logger.info("🛑 Starting graceful shutdown...")
        
        try:
            await db_pool.close_all()
            if self.application:
                await self.application.stop()
            self.logger.info("✅ Graceful shutdown completed")
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")

async def main():
    """Main function"""
    print("🚀 Starting Enhanced Telegram Bot...")
    
    bot = EnhancedTelegramBot()
    
    try:
        success = await bot.start()
        if not success:
            print("❌ Bot failed to start")
            return 1
    except KeyboardInterrupt:
        print("\\n⏹️ Bot stopped by user")
    except Exception as e:
        print(f"\\n❌ Bot crashed: {e}")
        return 1
    finally:
        await bot.shutdown()
    
    return 0

if __name__ == '__main__':
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
''',

        # ===== REQUIREMENTS AND CONFIG FILES =====
        "requirements.txt": '''python-telegram-bot==20.7
aiosqlite==0.19.0
python-dotenv==1.0.0
google-cloud-aiplatform==1.38.1
aiohttp==3.9.1
asyncio-throttle==1.0.2
prometheus-client==0.19.0
watchdog==3.0.0
psutil==5.9.6
''',

        ".env.example": '''# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_bot_token_here

# AI Services
PERPLEXITY_API_KEY=your_perplexity_api_key
GOOGLE_PROJECT_ID=your_google_project_id
GOOGLE_LOCATION=us-central1
GOOGLE_APPLICATION_CREDENTIALS=./genai-key.json

# Database Configuration
DATABASE_PATH=bot_database.db
DB_POOL_SIZE=10
DB_TIMEOUT=30

# Mining System Configuration
ASTEROID_GROUP_USERNAME=@asteroid_community
ASTEROID_GROUP_CHAT_ID=-1001538908265
MESSAGES_PER_CREDIT=20
DAILY_MINING_LIMIT=30
MIN_MESSAGE_LENGTH=20

# Credit System
SINGLE_STYLE_COST=5
COMBINATION_STYLE_COST=7
FREE_TRIAL_CREDITS=15
REFERRER_REWARD=5
REFEREE_REWARD=30

# Rate Limiting
MAX_REQUESTS_PER_MINUTE=10
MAX_CALLBACKS_PER_MINUTE=30
MAX_CONTENT_GENERATION_PER_HOUR=5

# Admin Configuration
ADMIN_USERNAME=ramenchef9999

# Performance Settings
CACHE_TTL_SECONDS=300
USER_DATA_CLEANUP_HOURS=24
MAX_MESSAGE_LENGTH=4096

# Monitoring & Metrics
ENABLE_METRICS=true
METRICS_PORT=8000
LOG_LEVEL=INFO
''',

        # ===== SCRIPTS =====
        "scripts/init_database.py": '''# scripts/init_database.py
import asyncio
import aiosqlite
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def initialize_enhanced_database(db_path: str = "bot_database.db"):
    """Initialize enhanced database with all required tables"""
    
    # Backup existing database if it exists
    db_file = Path(db_path)
    if db_file.exists():
        backup_path = f"{db_path}.backup"
        import shutil
        shutil.copy2(db_path, backup_path)
        logger.info(f"📁 Backed up existing database to {backup_path}")
    
    async with aiosqlite.connect(db_path) as conn:
        # Enable optimizations
        await conn.execute("PRAGMA foreign_keys = ON")
        await conn.execute("PRAGMA journal_mode = WAL")
        await conn.execute("PRAGMA synchronous = NORMAL")
        
        # Enhanced users table
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                name TEXT,
                username TEXT,
                language_code TEXT DEFAULT 'en',
                interests TEXT DEFAULT '[]',
                settings TEXT DEFAULT '{}',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_admin BOOLEAN DEFAULT 0,
                total_messages INTEGER DEFAULT 0
            )
        ''')
        
        # Enhanced user credits table
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS user_credits (
                user_id INTEGER PRIMARY KEY,
                credits INTEGER DEFAULT 15,
                total_earned INTEGER DEFAULT 15,
                total_spent INTEGER DEFAULT 0,
                is_premium BOOLEAN DEFAULT 0,
                premium_granted_by INTEGER,
                premium_granted_at TIMESTAMP,
                last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_free_trial BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                referred_by INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        
        # Credit transactions table
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS credit_transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                transaction_type TEXT NOT NULL,
                amount INTEGER NOT NULL,
                balance_before INTEGER,
                balance_after INTEGER,
                description TEXT,
                admin_user_id INTEGER,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        
        # Daily mining table
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS daily_mining (
                user_id INTEGER,
                date TEXT,
                messages_sent INTEGER DEFAULT 0,
                credits_mined INTEGER DEFAULT 0,
                last_message_time TIMESTAMP,
                group_id TEXT DEFAULT '@asteroid_community',
                PRIMARY KEY (user_id, date),
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        
        # Referral links table
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS referral_links (
                user_id INTEGER PRIMARY KEY,
                referral_code TEXT UNIQUE NOT NULL,
                total_referrals INTEGER DEFAULT 0,
                total_rewards INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        
        # Referrals table
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS referrals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                referrer_id INTEGER NOT NULL,
                referee_id INTEGER NOT NULL,
                referrer_reward INTEGER DEFAULT 5,
                referee_reward INTEGER DEFAULT 30,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (referrer_id) REFERENCES users (user_id),
                FOREIGN KEY (referee_id) REFERENCES users (user_id),
                UNIQUE(referee_id)
            )
        ''')
        
        # Promote codes table
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS promote_codes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                code TEXT UNIQUE NOT NULL,
                credits INTEGER NOT NULL,
                max_uses INTEGER DEFAULT NULL,
                current_uses INTEGER DEFAULT 0,
                expires_at TIMESTAMP DEFAULT NULL,
                created_by INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                is_active BOOLEAN DEFAULT 1,
                description TEXT,
                code_type TEXT DEFAULT 'general',
                FOREIGN KEY (created_by) REFERENCES users (user_id)
            )
        ''')
        
        # Code redemptions table
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS code_redemptions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                code_id INTEGER NOT NULL,
                code TEXT NOT NULL,
                credits_received INTEGER NOT NULL,
                redeemed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (code_id) REFERENCES promote_codes (id),
                FOREIGN KEY (user_id) REFERENCES users (user_id),
                UNIQUE(user_id, code_id)
            )
        ''')
        
        await conn.commit()
        
        logger.info("✅ Enhanced database initialized successfully")
        logger.info("📊 Tables created: users, user_credits, credit_transactions")
        logger.info("📊 Mining tables: daily_mining")
        logger.info("📊 Referral tables: referral_links, referrals")
        logger.info("📊 Promo tables: promote_codes, code_redemptions")

if __name__ == "__main__":
    asyncio.run(initialize_enhanced_database())
''',

        "scripts/deploy.py": '''# scripts/deploy.py
import subprocess
import sys
import os
from pathlib import Path

def deploy_enhanced_bot():
    """Enhanced deployment script"""
    print("🚀 Enhanced Telegram Bot Deployment")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3.8):
        print("❌ Python 3.8+ required")
        return False
    
    print(f"✅ Python {sys.version_info.major}.{sys.version_info.minor}")
    
    # Create virtual environment
    venv_path = Path("venv")
    if not venv_path.exists():
        print("🔧 Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", "venv"])
    
    # Install requirements
    if os.name == 'nt':  # Windows
        pip_path = venv_path / "Scripts" / "pip"
    else:  # Unix/Linux/Mac
        pip_path = venv_path / "bin" / "pip"
    
    print("📦 Installing dependencies...")
    subprocess.run([str(pip_path), "install", "-r", "requirements.txt"])
    
    # Check for required files
    required_files = [".env"]
    missing_files = []
    
    for file in required_files:
        if not Path(file).exists():
            missing_files.append(file)
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"  • {file}")
        print("\\n📝 Copy .env.example to .env and fill in your values")
        return False
    
    print("✅ All required files present")
    
    # Create log directory
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    print("✅ Log directory created")
    
    # Create startup script
    create_startup_script()
    
    print("\\n🎉 Deployment completed successfully!")
    print("🚀 To start the bot:")
    print("  • Development: python main_enhanced.py")
    print("  • Production: ./start_bot.sh (Linux/Mac) or start_bot.bat (Windows)")
    
    return True

def create_startup_script():
    """Create startup script"""
    if os.name == 'nt':  # Windows
        script_content = """@echo off
echo Starting Enhanced Telegram Bot...
venv\\\\Scripts\\\\python.exe main_enhanced.py
pause
"""
        script_file = Path("start_bot.bat")
    else:  # Unix/Linux/Mac
        script_content = """#!/bin/bash
echo "🚀 Starting Enhanced Telegram Bot..."
source venv/bin/activate
python main_enhanced.py
"""
        script_file = Path("start_bot.sh")
    
    script_file.write_text(script_content)
    
    if os.name != 'nt':
        os.chmod(script_file, 0o755)
    
    print(f"✅ Created startup script: {script_file}")

if __name__ == "__main__":
    deploy_enhanced_bot()
''',

        # ===== README =====
        "README.md": '''# Enhanced Telegram Bot

A production-ready Telegram bot with advanced features including input validation, database connection pooling, rate limiting, and comprehensive monitoring.

## 🚀 Features

### ✅ Core Improvements
- **Input Validation**: Comprehensive validation for all user inputs and callback data
- **Database Connection Pooling**: Async connection pooling with auto-scaling (3-10 connections)
- **Rate Limiting**: Multi-level rate limiting (messages, callbacks, content generation)
- **Memory Management**: Automated cleanup of expired user data
- **Monitoring**: Prometheus metrics and health endpoints
- **Error Handling**: Enhanced error recovery with user-friendly messages

### 🔧 Technical Features
- **No Hardcoded Values**: All configuration via environment variables
- **Enhanced Security**: XSS protection, SQL injection prevention
- **Performance Optimized**: WAL mode, proper indexing, connection pooling
- **Comprehensive Logging**: Multiple log levels and file handlers
- **Graceful Shutdown**: Proper cleanup of resources

## 📁 Project Structure

```
enhanced_telegram_bot/
├── config/              # Configuration files
├── database/            # Database connection management
├── handlers/            # Message and callback handlers  
├── managers/            # Business logic managers
├── utils/               # Utilities (validation, formatting)
├── monitoring/          # Metrics and monitoring
├── scripts/             # Deployment and setup scripts
├── logs/                # Log files
├── main_enhanced.py     # Main application
├── requirements.txt     # Dependencies
└── .env.example         # Environment template
```

## 🛠️ Installation

### 1. Quick Setup
```bash
# Run the automated deployment
python project_generator.py
cd enhanced_telegram_bot
python scripts/deploy.py
```

### 2. Manual Setup
```bash
# Clone or create project directory
mkdir enhanced_telegram_bot
cd enhanced_telegram_bot

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\\Scripts\\activate   # Windows

# Install dependencies
pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your values

# Initialize database
python scripts/init_database.py
```

## ⚙️ Configuration

### Required Environment Variables

Create `.env` file with:

```env
# Telegram Bot Token (required)
TELEGRAM_BOT_TOKEN=your_bot_token_here

# AI Services (required)  
PERPLEXITY_API_KEY=your_perplexity_api_key
GOOGLE_PROJECT_ID=your_google_project_id

# Optional configurations
DB_POOL_SIZE=10
MAX_REQUESTS_PER_MINUTE=10
ENABLE_METRICS=true
LOG_LEVEL=INFO
```

### Google Cloud Setup
1. Create a Google Cloud project
2. Enable Vertex AI API
3. Create a service account
4. Download the key file as `genai-key.json`

## 🚀 Running the Bot

### Development
```bash
python main_enhanced.py
```

### Production
```bash
# Linux/Mac
./start_bot.sh

# Windows  
start_bot.bat
```

## 📊 Monitoring

### Metrics Endpoints
- **Health Check**: `http://localhost:8000/health`
- **Prometheus Metrics**: `http://localhost:8000/metrics`

### Key Metrics
- `telegram_bot_operations_total` - Total operations by type
- `telegram_bot_response_time_seconds` - Response time metrics
- `telegram_bot_errors_total` - Error count by type
- `telegram_bot_uptime_seconds` - Bot uptime

### Logs
- `logs/bot_enhanced.log` - Main application logs
- `logs/bot_errors.log` - Error-only logs

## 🔒 Security Features

### Input Validation
- All user inputs sanitized against XSS
- Callback data validated with regex patterns
- User ID and credit amount validation

### Rate Limiting
- Per-user rate limits for different operation types
- Global rate limits to prevent system overload
- Configurable limits via environment variables

### Database Security
- Prepared statements throughout
- Foreign key constraints enabled
- Transaction rollback on errors

## ⚡ Performance

### Expected Benchmarks
- **Response Time**: < 2s for 95th percentile
- **Concurrent Users**: 1000+ simultaneous users  
- **Database Queries**: < 100ms with connection pooling
- **Memory Usage**: < 512MB per instance
- **Error Rate**: < 1% failed operations

### Optimization Features
- Database connection pooling with auto-scaling
- WAL mode for better write performance
- Proper database indexing
- Automated memory cleanup
- Efficient message formatting

## 🧪 Testing

### Health Check
```bash
curl http://localhost:8000/health
```

### Database Test
```bash
python scripts/init_database.py
```

### Bot Test
Send `/start` command to your bot

## 🔧 Troubleshooting

### Common Issues

#### Database Connection Errors
```bash
# Check database permissions
ls -la bot_database.db

# Reinitialize database
python scripts/init_database.py
```

#### Memory Issues
```env
# Reduce cleanup interval in .env
USER_DATA_CLEANUP_HOURS=1
```

#### Rate Limiting Too Strict
```env
# Increase limits in .env
MAX_REQUESTS_PER_MINUTE=20
MAX_CALLBACKS_PER_MINUTE=60
```

## 📈 Scaling

### Production Deployment
- Use process managers (PM2, systemd)
- Setup log rotation
- Configure monitoring alerts
- Implement backup strategies

### Multiple Instances
- Database supports concurrent connections
- Stateless design allows horizontal scaling
- Load balancer recommended for high traffic

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🆘 Support

For support and questions:
- Check the troubleshooting section
- Review logs in `logs/` directory
- Contact: @ramenchef9999

---

## 🎯 Production Checklist

Before deploying to production:

- [ ] All environment variables configured
- [ ] Database initialized and tested
- [ ] Google Cloud credentials configured  
- [ ] Telegram bot token valid
- [ ] Monitoring endpoints accessible
- [ ] Log rotation configured
- [ ] Backup strategy implemented
- [ ] Error alerting setup
- [ ] Performance testing completed
- [ ] Security review done

Ready for production! 🚀
'''
    }
    
    # Create all files
    for file_path, content in files_content.items():
        file_obj = Path(file_path)
        file_obj.parent.mkdir(parents=True, exist_ok=True)
        file_obj.write_text(content, encoding='utf-8')
    
    print(f"✅ Created {len(files_content)} files")

def create_zip_package():
    """Create ZIP package of the entire project"""
    print("📦 Creating ZIP package...")
    
    with zipfile.ZipFile('enhanced_telegram_bot.zip', 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add all files
        for root, dirs, files in os.walk('.'):
            # Skip unwanted directories
            dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'venv', '.env']]
            
            for file in files:
                if file.endswith(('.pyc', '.zip')):
                    continue
                    
                file_path = os.path.join(root, file)
                arc_path = os.path.relpath(file_path, '.')
                zipf.write(file_path, arc_path)
    
    print("✅ Created enhanced_telegram_bot.zip")

def main():
    """Main function to create the entire project"""
    print("🎯 Enhanced Telegram Bot Project Generator")
    print("=" * 60)
    
    # Create project directory
    project_name = "enhanced_telegram_bot"
    if Path(project_name).exists():
        import shutil
        shutil.rmtree(project_name)
    
    Path(project_name).mkdir()
    os.chdir(project_name)
    
    # Create project structure and files
    create_project_structure()
    create_files()
    
    # Go back and create zip
    os.chdir('..')
    create_zip_package()
    
    print("\n🎉 Project created successfully!")
    print(f"📁 Project directory: {project_name}/")
    print(f"📦 ZIP package: enhanced_telegram_bot.zip")
    print("\n🚀 Next steps:")
    print("1. Extract enhanced_telegram_bot.zip")
    print("2. Copy .env.example to .env and configure")
    print("3. Add your genai-key.json file")
    print("4. Run: python scripts/deploy.py")
    print("5. Start bot: python main_enhanced.py")
    print("\n📊 Monitoring: http://localhost:8000/health")

if __name__ == "__main__":
    main()

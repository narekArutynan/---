from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler
import os

class TelegramHandler:
    def __init__(self):
        self.app = ApplicationBuilder().token(os.getenv('TELEGRAM_TOKEN')).build()
        self.app.add_handler(CommandHandler('start', self.start))
    
    async def start(self, update: Update, context):
        await update.message.reply_text('Добро пожаловать!')

    def run(self):
        self.app.run_polling()

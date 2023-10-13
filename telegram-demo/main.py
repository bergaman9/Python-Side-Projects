from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes
import os
from dotenv import load_dotenv

# Çevresel değişkenleri yükler (örn. BOT_TOKEN)
load_dotenv()

# BOT_TOKEN'u çevresel değişkenlerden alır.
BOT_TOKEN = os.getenv("BOT_TOKEN")

# '/hello' komutu için işleyici.
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# Kullanıcının gönderdiği herhangi bir metni geri yollar.
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Yollanan mesajı geri yollar."""
    await update.message.reply_text(update.message.text)

# Botla ilk etkileşime geçildiğinde çalışır.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Bot başladığında selam verir."""
    await update.message.reply_text(f'Merhaba {update.effective_user.first_name}! Ben senin botunum. Nasıl yardımcı olabilirim?')

# Botu başlatmak ve komut işleyicilerini eklemek için bir uygulama oluşturur.
app = ApplicationBuilder().token(BOT_TOKEN).build()

# '/hello' ve '/start' komutları için işleyicileri ekler.
app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("start", start))

# Komut dışındaki tüm metin mesajları için 'echo' işlevini kullanır.

# Eğer bu dosya doğrudan çalıştırılırsa, botu başlatır.
if __name__ == "__main__":
    print("Bot hazır!")
    app.run_polling()

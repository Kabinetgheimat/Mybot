from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = ('7953709760:AAHWEfnr0l05aBTk07Qc5pHiO1a8b644a8g')

def start(update: Update, context: CallbackContext) -> None:
    welcome_text = (
        "سلام 👋\n"
        "به ربات محاسبه ابعاد و قیمت کابینت خوش آمدید!\n\n"
        "اینجا خودت می‌تونی قیمت کابینت رو محاسبه کنی.\n"
        "ابعاد رو به ترتیب *طول.عمق.ارتفاع* وارد کن (مثلاً 120.60.90)\n"
        "_ابعاد رو به سانتیمتر وارد کن._\n\n"
        "📌 قیمت‌ها حدودی هستند. برای بازدید، طراحی و قیمت دقیق‌تر تماس بگیر:\n"
        "📞 09150500593\n"
        "📷 ما رو در اینستاگرام دنبال کن: [Instagram](https://instagram.com/farhadpooryan)\n\n"
        "برای عملکرد بهتر از منوی پایین استفاده کن 👇"
    )
    update.message.reply_text(welcome_text, parse_mode='Markdown')

def handle_dimensions(update: Update, context: CallbackContext) -> None:
    try:
        parts = update.message.text.split(".")
        if len(parts) != 3:
            raise ValueError
        length, depth, height = map(float, parts)
        volume = (length / 100) * (depth / 100) * (height / 100)
        estimated_price = volume * 5500000  # قیمت حدودی هر متر مکعب
        update.message.reply_text(f"حجم کابینت: {volume:.2f} متر مکعب\n"
                                  f"قیمت حدودی: {estimated_price:,.0f} تومان")
    except:
        update.message.reply_text("❗ لطفاً ابعاد را به صورت صحیح و با نقطه وارد کن (مثلاً: 120.60.90)")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_dimensions))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

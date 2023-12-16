import requests
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Отримати токен бота від BotFather
TOKEN = "6331483828:AAFwNV7gS1ZmNM1M7KtUjxTgZ3L26DTV6QE"
# Отримати ключ API для CoinGecko
COINGECKO_API_KEY = "CG-r3Fj2ASNuzkYPZEfDo6bPyzP"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привіт! Я бот для відстеження цін криптовалют.')

def get_crypto_price(update: Update, context: CallbackContext) -> None:
    # Отримати назву криптовалюти з команди
    crypto_symbol = context.args[0].upper()

    # Отримати ціну криптовалюти з CoinGecko
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_symbol}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()

    # Вивести ціну криптовалюти
    if crypto_symbol in data:
        price = data[crypto_symbol]["usd"]
        update.message.reply_text(f"Ціна {crypto_symbol}: {price} USD")
    else:
        update.message.reply_text(f"Криптовалюта {crypto_symbol} не знайдена.")

def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("price", get_crypto_price, pass_args=True))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

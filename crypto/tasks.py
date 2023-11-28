from celery import shared_task
from crypto.models import CryptocurrencyQuote
import requests


@shared_task
def send_crypto_quote():
    bot_token = ""
    chat_username = ""
    try:
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        )
        data = response.json()
        price = data["bitcoin"]["usd"]

        CryptocurrencyQuote.objects.create(symbol="BTC/USD", price=price)
        message_text = f"Котировка BTC/USD: {price} USD"
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        data = {
            "chat_id": chat_username,
            "text": message_text,
        }
        response = requests.post(url, data=data)
        return response.json()

    except Exception as e:
        print(f"Error fetching cryptocurrency quote: {str(e)}")
        return {"error": str(e)}

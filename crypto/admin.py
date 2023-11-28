from django.contrib import admin
from crypto.models import Message, CryptocurrencyQuote

admin.site.register(Message)

admin.site.register(CryptocurrencyQuote)
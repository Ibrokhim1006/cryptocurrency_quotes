from django.db import models


class Message(models.Model):
    text = models.TextField()


class CryptocurrencyQuote(models.Model):
    symbol = models.CharField(max_length=30, null=True, blank=True)
    price = models.CharField(max_length=100, null=True, blank=True)

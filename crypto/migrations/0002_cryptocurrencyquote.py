# Generated by Django 4.2.7 on 2023-11-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CryptocurrencyQuote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]

import csv

from django.db.models import Q
from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from cryptocoins.models import Cryptocurrency, Exchange


class Command(BaseCommand):
    help = """
        Export all Cryptocurrencies in Database into a CSV file.
        An `exchange_id` option can be sent in order to filter the currencies
        before exporting them.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            '-e', '--exchange_id', required=False,
            help='Export only currencies from exchange with given id')

    def handle(self, *args, **options):
        exchange_id = options.get('exchange_id')
        query = Q()
        if exchange_id:
            try:
                exchange = Exchange.objects.get(id=exchange_id)
            except Exchange.DoesNotExist:
                raise CommandError(
                    'Exchange with id {} does not exist.'.format(exchange_id))

            query = Q(exchange=exchange)

        currencies = Cryptocurrency.objects.filter(query)

        with open('{}/currencies.csv'.format(settings.BASE_DIR), 'w') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                'Currency ID',
                'Name',
                'Exchange',
                'Exchange ID',
                'Price USD',
                'Market Cap',
                'Volume'
            ])
            for currency in currencies:
                writer.writerow([
                    currency.id,
                    currency.name,
                    currency.exchange.name,
                    currency.exchange.id,
                    '{} USD'.format(currency.price_usd),
                    currency.market_cap_usd,
                    currency.volume_usd_24h
                ])

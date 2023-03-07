import requests
import json
from config import keys


class ConvertionExeption(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты {quote}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Не удалост обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Не удалост обработать валюту {base}.')

        try:
            amount = float(amount)
        except KeyError:
            raise ConvertionExeption(f'Не удалост обработать количество {amount}.')
        headers = {
        "apikey": "u1Aa9zTGMxSFBWaUR8KxyVA90FTIDuJV"
        }
        r = requests.get(
        f'https://api.apilayer.com/exchangerates_data/convert?to={base_ticker}&from={quote_ticker}&amount={amount}',
        headers=headers)

        total_base = json.loads(r.content)['result']
        return total_base





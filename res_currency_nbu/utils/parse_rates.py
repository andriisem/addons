import requests


NBU_RATES_URL_JSON = \
    'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'


def _get_rates_in_json():
    """
    Get full list of NBU rates API currencies rate method
    :return: list of currencies dicts
    """
    data = requests.get(NBU_RATES_URL_JSON)

    return data.json()


def get_rates_by_code(codes):
    """
    Get rates for currencies of given codes
    :param codes: list of currency codes strings
                  EXAMPLE:
                  ['USD', 'RUB']

    :return: Dict {currency_name: currency_rate}

            EXAMPLE:
            {u'RUB': 0.46145, u'USD': 26.30439}
    """
    rates_json = _get_rates_in_json()

    rates = {
        currency['cc']: currency['rate'] for currency in rates_json
        if currency['cc'] in codes
    }

    rates['UAH'] = 1

    return rates

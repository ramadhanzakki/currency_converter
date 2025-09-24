EXCHANGE_RATES = {
    'IDR': 16500.0,
    'EUR': 0.85,
    'USD': 1.0,
    'JPY': 147.87
}


def currency_converter(amount, source):
    if source_currency not in EXCHANGE_RATES:
        return None
    convert_to_usd = amount / EXCHANGE_RATES[source]
    for currency_code, rate in EXCHANGE_RATES.items():
        if currency_code == source:
            continue
        converted_amount = convert_to_usd * rate
        print(f'- {converted_amount} {currency_code}')

while True:
    try:
        amount = float(input('Enter the amount: '))
        break
    except:
        print('Input just number!')
        continue

while True:
    source_currency = input(f'Source currency ({"/".join(EXCHANGE_RATES.keys())}): ').upper()
    if source_currency in EXCHANGE_RATES:
        break
    else:
        print('Invalid Input! Please chocie from the available currency')



print(f'{amount} {source_currency} is equal to: ')
currency_converter(amount,source_currency)

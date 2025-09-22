EXCHANGE_RATES = {
    'IDR': 16500.0,
    'EUR': 0.85,
    'USD': 1.0,
    'JPY': 147.87
}


def currency_converter(amount, source, target):
    if source_currency not in EXCHANGE_RATES or target_currency not in EXCHANGE_RATES:
        return None
    convert_to_usd = amount / EXCHANGE_RATES[source]
    convert_usd_to_target = convert_to_usd * EXCHANGE_RATES[target]
    return convert_usd_to_target


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

while True:
    target_currency = input(f'Target currency ({"/".join(EXCHANGE_RATES.keys())}): ').upper()
    if source_currency in EXCHANGE_RATES:
        break
    else:
        print('Invalid Input! Please chocie from the available currency')

results_conveter = currency_converter(amount, source_currency, target_currency)

print(f'{amount} {source_currency} is equal to {results_conveter} {target_currency}')

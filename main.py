def currency_converter(amount, source, target):
    if target == 'idr' and source == 'usd':
        return amount * 16500
    elif target == 'usd' and source == 'idr':
        return amount / 16500
    else:
        return amount


while True:

    while True:
        try:
            amount = int(input('Enter the amount: '))
            break
        except:
            print('Input just number!')
            continue

    while True:
        source_currency = input('Source currency (USD/IDR): ').lower()
        if source_currency == 'usd' or source_currency == 'idr':
            break
        else:
            print('Choice between USD or IDR')
            continue

    while True:
        target_currency = input('Target currency (USD/IDR): ').lower()
        if target_currency == 'usd' or target_currency == 'idr':
            break
        else:
            print('Choice between USD or IDR')
            continue
    
    break

results_conveter = currency_converter(amount, source_currency, target_currency)

print(f'{amount} {source_currency.capitalize()} is equal to {results_conveter} {target_currency.capitalize()}')
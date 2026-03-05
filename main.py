def exchange_money_usd():
    # Pedir al usuario la cantidad en USD
    budget = float(input("Ingresa la cantidad en USD: "))

    # Tasas de cambio fijas (ejemplo aproximado marzo 2026)
    rates = {
        "JPY": 157.128,   # 1 USD = 157.128 JPY
        "MXN": 17.673,    # 1 USD = 17.673 MXN
        "EUR": 0.85493,   # 1 USD = 0.85493 EUR
        "COP": 3802.62    # 1 USD = 3802.62 COP
    }

    print(f"\nConvirtiendo {budget} USD a otras monedas...\n")
    for currency, rate in rates.items():
        result = budget * rate
        print(f"{budget} USD = {result:.2f} {currency}")

# Ejecutar la calculadora
exchange_money_usd()

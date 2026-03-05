def exchange_money():
    # Tasas de cambio aproximadas (marzo 2026) respecto al USD
    rates = {
        "USD": 1.0,
        "JPY": 157.128,
        "MXN": 17.673,
        "EUR": 0.85493,
        "COP": 3802.62
    }

    # Pedir al usuario la moneda de origen
    from_currency = input("¿Qué moneda tienes? (USD, JPY, MXN, EUR, COP): ").upper()

    if from_currency not in rates:
        print("Moneda no soportada.")
        return

    # Pedir la cantidad
    amount = float(input(f"Ingresa la cantidad en {from_currency}: "))

    # Convertir primero a USD
    amount_in_usd = amount / rates[from_currency]

    print(f"\nConvirtiendo {amount} {from_currency} a otras monedas...\n")

    # Mostrar conversiones a todas las demás monedas
    for currency, rate in rates.items():
        if currency != from_currency:
            result = amount_in_usd * rate
            print(f"{amount} {from_currency} → {result:.2f} {currency}")

# Ejecutar la calculadora
exchange_money()

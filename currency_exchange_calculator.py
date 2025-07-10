rates = {
    "USD": 1.0,
    "EUR": 0.9,
    "JPY": 135.0,
    "GBP": 0.8,
}

while True:
    try:
        amount = float(input("How much do you want to convert?"))
    except ValueError:
        print("Please enter a valid number.")
        input("Press Enter to continue...")
        continue
        
        
    print("Available currencies and their exchange rates:")
    for currency, rate in rates.items():
        print(f"{currency}: {rate}")
  
    currency_1 = input("What currency to you want to convert from?").strip().upper()
    if currency_1 not in rates:
        print("Invalid currency. Please try again.")
        input("Press Enter to continue...")
        continue
    for currencies, info in rates.items():
        print(f"{currencies}: {info}")
    currency_2 = input("What currency do you want to convert into?").strip().upper()
    if currency_2 not in rates:
        print("Invalid currency. Please try again.")
        input("Press Enter to continue...")
        continue
    
    usd_amount = amount / rates[currency_1]
    converted_amount = usd_amount * rates[currency_2]
    
    print(f"{amount} {currency_1} is equal to {converted_amount: .2f} {currency_2}")
    
    again = input("Do you want to convert another amount? (y/n): ").strip().lower()
    if again != "y":
        break
def convert_currency(amount, from_curr, to_curr):
    # Base currency: USD
    rates = {
        "USD": 1,
        "INR": 83.0,
        "GBP": 0.79,
        "EUR": 0.92,
        "JPY": 150.0
    }
    
    usd_amount = amount / rates[from_curr]
    result = usd_amount * rates[to_curr]

    return result


def main():
    print("===== Currency Converter =====")
    print("Available currencies: USD, INR, GBP, EUR, JPY")

    amount = float(input("Enter amount: "))
    from_curr = input("From currency: ").upper()
    to_curr = input("To currency: ").upper()

    if from_curr not in ["USD", "INR", "GBP", "EUR", "JPY"] or \
       to_curr not in ["USD", "INR", "GBP", "EUR", "JPY"]:
        print("❌ Invalid currency!")
        return

    result = convert_currency(amount, from_curr, to_curr)

    print(f"\n💱 {amount} {from_curr} = {round(result, 2)} {to_curr}")


main()
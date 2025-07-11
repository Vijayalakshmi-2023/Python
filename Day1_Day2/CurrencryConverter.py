import requests

def convert_currency(from_currency, to_currency, amount):
    url = f"https://api.exchangerate.host/convert"
    params = {
        'from': from_currency.upper(),
        'to': to_currency.upper(),
        'amount': amount
    }
    response = requests.get(url, params=params)
    data = response.json()

    if data.get("success", False):
        result = data["result"]
        print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
    else:
        print("Error fetching conversion. Please check the currency codes.")

def main():
    print("💱 Currency Converter")
    from_currency = input("From currency (e.g., USD): ").strip()
    to_currency = input("To currency (e.g., EUR): ").strip()

    try:
        amount = float(input("Amount to convert: "))
        convert_currency(from_currency, to_currency, amount)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()

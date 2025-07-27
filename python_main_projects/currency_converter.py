import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# API endpoint and key
API_URL = "https://api.exchangerate-api.com/v4/latest/"
API_HISTORY_URL = "https://api.exchangerate-api.com/v4/history/"

# Initialize favorite currencies (empty list for now)
favorite_currencies = []

# Fetch real-time exchange rates from the API
def get_exchange_rates(base_currency="USD"):
    try:
        response = requests.get(f"{API_URL}{base_currency}")
        data = response.json()
        if response.status_code == 200:
            return data["rates"]
        else:
            print("Error fetching data from the API.")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Convert between currencies
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == to_currency:
        return amount
    return amount * rates[to_currency] / rates[from_currency]

# Historical rate lookup (last 7 days)
def get_historical_data(base_currency, target_currency):
    historical_data = []
    today = datetime.today()
    for i in range(7):
        date = today - timedelta(days=i)
        date_str = date.strftime("%Y-%m-%d")
        response = requests.get(f"{API_HISTORY_URL}{base_currency}/{date_str}")
        data = response.json()
        if response.status_code == 200 and target_currency in data["rates"]:
            historical_data.append((date_str, data["rates"][target_currency]))
        else:
            historical_data.append((date_str, None))
    return historical_data[::-1]

# Plot a simple trend graph
def plot_trend(data, currency):
    dates = [entry[0] for entry in data]
    rates = [entry[1] for entry in data]

    plt.figure(figsize=(10, 6))
    plt.plot(dates, rates, marker="o", color="b")
    plt.title(f"Currency Trend for {currency}")
    plt.xlabel("Date")
    plt.ylabel(f"Exchange Rate ({currency})")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Add or remove currencies to/from favorites list
def manage_favorites(currency, action="add"):
    global favorite_currencies
    if action == "add":
        if currency not in favorite_currencies:
            favorite_currencies.append(currency)
            print(f"{currency} added to favorites.")
        else:
            print(f"{currency} is already in your favorites.")
    elif action == "remove":
        if currency in favorite_currencies:
            favorite_currencies.remove(currency)
            print(f"{currency} removed from favorites.")
        else:
            print(f"{currency} is not in your favorites.")

def main():
    print("=== Currency Converter ===")
    
    while True:
        print("\nOptions:")
        print("1. Convert Currency")
        print("2. View Real-Time Exchange Rates")
        print("3. View Historical Trend")
        print("4. Manage Favorite Currencies")
        print("0. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            from_currency = input("From Currency (e.g., USD): ").upper()
            to_currency = input("To Currency (e.g., EUR): ").upper()
            amount = float(input(f"Amount in {from_currency}: "))
            rates = get_exchange_rates(from_currency)
            if rates:
                converted_amount = convert_currency(amount, from_currency, to_currency, rates)
                print(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

        elif choice == '2':
            base_currency = input("Base Currency (e.g., USD): ").upper()
            rates = get_exchange_rates(base_currency)
            if rates:
                print(f"\nReal-Time Exchange Rates for {base_currency}:")
                for currency, rate in rates.items():
                    print(f"{currency}: {rate}")

        elif choice == '3':
            base_currency = input("Base Currency (e.g., USD): ").upper()
            target_currency = input("Target Currency (e.g., EUR): ").upper()
            historical_data = get_historical_data(base_currency, target_currency)
            if historical_data:
                print(f"\nHistorical Trend for {base_currency} to {target_currency}:")
                plot_trend(historical_data, target_currency)

        elif choice == '4':
            print("\n1. Add to Favorites")
            print("2. Remove from Favorites")
            fav_choice = input("Choose an option: ")
            if fav_choice == '1':
                currency = input("Currency to add to favorites: ").upper()
                manage_favorites(currency, "add")
            elif fav_choice == '2':
                currency = input("Currency to remove from favorites: ").upper()
                manage_favorites(currency, "remove")
            else:
                print("Invalid choice.")
        
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
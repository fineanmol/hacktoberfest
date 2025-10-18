import requests
import json

# Replace with your API Key from freecurrencyapi.com
API_KEY = "REPLACE_WITH_FREE_CURRENCY_API_KEY"
FREE_CURRENCY_API_URL = "https://api.freecurrencyapi.com/v1/latest"

def get_exchange_rate(from_currency, to_currency, api_key):
    """
    Gets the exchange rate.
    Returns the rate or None in case of error
    """
    if api_key == "REPLACE_WITH_FREE_CURRENCY_API_KEY":
        print("Error: Please replace 'REPLACE_WITH_FREE_CURRENCY_API_KEY' with actual key.")
        return None

    params = {
        "apikey": api_key,
        "base_currency": from_currency
    }

    try:
        response = requests.get(FREE_CURRENCY_API_URL, params=params)
        response.raise_for_status()  # Raise an exception
        data = response.json()

        if 'data' in data and to_currency in data['data']:
            return data['data'][to_currency]
        else:
            print(f"Error: Exchange rate for {to_currency} not found in response.")
            print("API Response:", data)
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error decoding response: {e}")
        print("Raw API Response:", response.text if 'response' in locals() else "No response received")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    print("Starting the Currency Converter!")

    from_currency = input("Enter the currency to convert FROM (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert TO (e.g., EUR): ").upper()
    try:
         amount = float(input("Enter the amount to convert: "))
    except ValueError:
         print("Invalid amount. Please enter a number.")
         return

    print(f"\nConverting {amount:.2f} {from_currency} to {to_currency}...")

    exchange_rate = get_exchange_rate(from_currency, to_currency, API_KEY)

    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        print(f"{amount:.2f} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Currency conversion has failed.")

if __name__ == "__main__":
    main()

import requests

class CountryData:
    def __init__(self, url):
        self.url = url
    
    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data from the provided URL.")
            return None
    
    def display_country_info(self, data):
        print("Country Information:")
        for country in data:
            name = country.get('name', {}).get('common', 'N/A')
            currencies = country.get('currencies', {})
            if currencies:
                print(f"Country: {name}")
                for currency, info in currencies.items():
                    print(f"  Currency: {currency}")
                    print(f"    Currency Name: {info.get('name', 'N/A')}")
                    print(f"    Currency Symbol: {info.get('symbol', 'N/A')}")
                print()
    
    def display_dollar_countries(self, data):
        print("Countries with Dollar as Currency:")
        for country in data:
            currencies = country.get('currencies', {})
            for currency in currencies:
                if currency == 'USD':
                    print(country['name']['common'])
                    break
    
    def display_euro_countries(self, data):
        print("Countries with Euro as Currency:")
        for country in data:
            currencies = country.get('currencies', {})
            for currency in currencies:
                if currency == 'EUR':
                    print(country['name']['common'])
                    break

# Example usage:
url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)
data = country_data.fetch_data()

if data:
    country_data.display_country_info(data)
    country_data.display_dollar_countries(data)
    country_data.display_euro_countries(data)

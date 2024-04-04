import requests

class BreweryData:
    def __init__(self, url):
        self.url = url

    def fetch_breweries(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data from the API.")
            return None

    def filter_breweries_by_states(self, data, states):
        filtered_breweries = []
        for brewery in data:
            if brewery['state'] in states:
                filtered_breweries.append(brewery['name'])
        return filtered_breweries

    def count_breweries_by_states(self, data, states):
        state_counts = {}
        for state in states:
            state_counts[state] = sum(1 for brewery in data if brewery['state'] == state)
        return state_counts

    def count_brewery_types_by_cities(self, data, state):
        city_type_counts = {}
        for brewery in data:
            if brewery['state'] == state:
                city = brewery['city']
                brewery_type = brewery['brewery_type']
                if city not in city_type_counts:
                    city_type_counts[city] = {}
                if brewery_type not in city_type_counts[city]:
                    city_type_counts[city][brewery_type] = 0
                city_type_counts[city][brewery_type] += 1
        return city_type_counts

    def count_websites_by_states(self, data, states):
        website_counts = {}
        for state in states:
            website_counts[state] = sum(1 for brewery in data if brewery['state'] == state and brewery['website_url'])
        return website_counts

# URL for Open Brewery DB API
url = "https://api.openbrewerydb.org/breweries"

brewery_data = BreweryData(url)
all_breweries = brewery_data.fetch_breweries()

if all_breweries:
    # Task 1
    selected_states = ['Alaska', 'Maine', 'New York']
    breweries_in_selected_states = brewery_data.filter_breweries_by_states(all_breweries, selected_states)
    print("Breweries in the selected states:")
    for brewery in breweries_in_selected_states:
        print("-", brewery)
    print()

    # Task 2
    state_counts = brewery_data.count_breweries_by_states(all_breweries, selected_states)
    print("Count of breweries in each selected state:")
    for state, count in state_counts.items():
        print(f"- {state}: {count}")
    print()

    # Task 3
    for state in selected_states:
        print(f"Types of breweries in cities of {state}:")
        city_type_counts = brewery_data.count_brewery_types_by_cities(all_breweries, state)
        for city, counts in city_type_counts.items():
            print(f"- {city}:")
            for brewery_type, count in counts.items():
                print(f"  {brewery_type}: {count}")
        print()

    # Task 4
    website_counts = brewery_data.count_websites_by_states(all_breweries, selected_states)
    print("Count of breweries with websites in each selected state:")
    for state, count in website_counts.items():
        print(f"- {state}: {count}")

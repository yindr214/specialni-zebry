import requests

# Set a custom User-Agent as required by Nominatim's Usage Policy
headers = {"User-Agent": "OlomoucShopFinderApp/1.0 (hidden.reward628@passinbox.com)"}

# Query endpoint for Olomouc
url = "https://nominatim.openstreetmap.org/search"
params = {
    "q": "Lidl Olomouc",
    "format": "json",
    "limit": 10
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    if data:
        result = data[0]
        print(f"Place: {result['display_name']}")
        print(f"Latitude: {result['lat']}")
        print(f"Longitude: {result['lon']}")
    else:
        print("No results found.")
else:
    print(f"Error: {response.status_code}")
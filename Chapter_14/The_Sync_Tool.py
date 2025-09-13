import requests

# This URL is the address of the resource we want to retrieve.
url = "https://api.starwars.com/ships/millennium-falcon"

# The GET request is sent, and our script waits until a response is received.
response = requests.get(url)

# The script does not proceed past the line above until the response is back.
response.raise_for_status() # Raises an error for bad status codes
ship_data = response.json()

print(f"The ship is a {ship_data['ship_class']} with a top speed of {ship_data['max_atmosphering_speed']}!")
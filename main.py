# Kharkiv:
# latitude = 49.98985
# longitude = 36.22942
# Izyum
# latitude = 49.1892
# longitude = 37.2761


import requests

# Define the center coordinate of the search
latitude = 49.98985
longitude = 36.22942

# Define the radius of the search in meters
radius = 30000

# Define the Overpass API query
overpass_url = "https://overpass-api.de/api/interpreter"
overpass_query = f"""
    [out:json];
    way["bridge"]["railway"](around:{radius},{latitude},{longitude});
    out center;
"""

# way["bridge"]["railway"]["layer"=1](around:{radius},{latitude},{longitude});
# way["railway"="bridge"]["layer"=1](around:{radius},{latitude},{longitude});

# Send the Overpass API query
response = requests.get(overpass_url, params={"data": overpass_query})

# Parse the response JSON and save the coordinates to a file
try:
    data = response.json()
    with open('railway-bridge-locations.txt', 'w') as f:
        for element in data["elements"]:
            if element["type"] == "way":
                f.write(f"Railway bridge, {element['center']['lat']}, {element['center']['lon']}\n")
    print(f"Found {len(data['elements'])} railway bridges")
except ValueError as e:
    print("Error: Could not parse Overpass API response")
    print(e)

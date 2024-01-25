import json
from math import radians, sin, cos, sqrt, atan2

# Function to calculate the Haversine distance between two points
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) ** 2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    
    return distance

# Load the dataset
with open('countriesV2.json', 'r') as file:
    data = json.load(file)

# Set the population limit
population_limit =28875 


# Filter countries based on population and currency condition
filtered_countries = [country for country in data if country['population'] >= population_limit and len(country['currencies']) == 1]
print(filtered_countries)

# Sort countries by population in descending order
sorted_countries = sorted(filtered_countries, key=lambda x: x['population'], reverse=True)

# Initialize a list to store coordinates
coordinates = []

# Extract latitude and longitude for each country
for country in sorted_countries:
    if 'latlng' in country:
        lat, lon = country['latlng']
    else:
        lat, lon = 0.000, 0.000  # If coordinates are missing, use 0.000 N 0.000 E
    coordinates.append((lat, lon))

# Calculate the sum of the lengths of all lines
total_distance = 0
for i in range(len(coordinates) - 1):
    lat1, lon1 = coordinates[i]
    lat2, lon2 = coordinates[i + 1]
    total_distance += haversine(lat1, lon1, lat2, lon2)

# Round the total distance to 2 decimal points
total_distance = round(total_distance, 2)

print(f"Total distance between countries: {total_distance} km")
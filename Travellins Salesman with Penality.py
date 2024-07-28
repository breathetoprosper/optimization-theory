# Use the penalty for the ones they are not going to go to.

import numpy as np
from itertools import permutations

# Define the high penalty value
HIGH_PENALTY = 99999

# Create the distance matrix with missing entries
distance_matrix = np.array([
    [0, 40, 60, 50, HIGH_PENALTY, HIGH_PENALTY],
    [40, 0, 10, HIGH_PENALTY, 70, HIGH_PENALTY],
    [60, 10, 0, 20, HIGH_PENALTY, HIGH_PENALTY],
    [50, HIGH_PENALTY, 20, 0, HIGH_PENALTY, 50],
    [HIGH_PENALTY, 70, HIGH_PENALTY, HIGH_PENALTY, 0, 10],
    [HIGH_PENALTY, HIGH_PENALTY, HIGH_PENALTY, 50, 10, 0]
])

# List of cities
cities = ["ISEG", "A", "B", "C", "D", "T"]

# Function to calculate the total distance of a given tour
def calculate_tour_distance(tour, distance_matrix):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distance_matrix[tour[i], tour[i+1]]
    total_distance += distance_matrix[tour[-1], tour[0]]  # return to the start
    return total_distance

# Generate all possible tours (permutations)
city_indices = list(range(len(cities)))
all_tours = permutations(city_indices)

# Find the shortest tour
shortest_tour = None
min_distance = float('inf')

for tour in all_tours:
    current_distance = calculate_tour_distance(tour, distance_matrix)
    if current_distance < min_distance:
        min_distance = current_distance
        shortest_tour = tour

# Convert the tour indices back to city names
shortest_tour_cities = [cities[i] for i in shortest_tour]

# Output the results
print("Shortest tour:", shortest_tour_cities)
print("Minimum distance:", min_distance)

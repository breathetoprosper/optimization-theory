import random

def greedy_tsp(cities):
    unvisited = cities[1:]
    route = [cities[0]]
    while unvisited:
        last = route[-1]
        next_city = min(unvisited, key=lambda city: distance(last, city))
        route.append(next_city)
        unvisited.remove(next_city)
    return route + [cities[0]]

def distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2) ** 0.5

def total_distance(route):
    return sum(distance(route[i], route[i+1]) for i in range(len(route)-1))

# Example usage
cities = [(0, 0), (1, 5), (2, 2), (3, 3), (5, 1)]
route = greedy_tsp(cities)
print("Greedy TSP Route:", route)
print("Total distance:", total_distance(route))
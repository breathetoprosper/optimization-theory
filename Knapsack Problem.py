'''
The Knapsack Problem:
In the knapsack problem, you are given a set of items, 
each with a weight and a value, 
and a knapsack with a maximum weight capacity. 

The goal is to determine which items to include in the knapsack 
so that the total weight is less than or equal to the given limit 
and the total value is as large as possible.
There are several variants of this problem, but the two most common are:

0/1 Knapsack Problem: Each item can either be included in the knapsack or not. 
You can't take a fraction of an item or include it multiple times.
Fractional Knapsack Problem: You can take fractions of items, 
which makes the problem easier to solve using a greedy approach.
'''

def knapsack_01(values, weights, capacity):
    n = len(values)
    # Initialize the DP table with 0s
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
    
    # Return the maximum value
    return dp[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

max_value = knapsack_01(values, weights, capacity)
print(f"Maximum value in Knapsack = {max_value}")
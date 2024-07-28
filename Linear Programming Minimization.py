'''
Example Problem

Minimize f(x,y)=(x−1)2+(y−2.5)^2 # we can also maximize.

Subject to:
x+2y≤6
−x+2y≤2
x≥0
y≥0

'''

import numpy as np
from scipy.optimize import minimize

# Define the objective function
def objective(vars):
    x, y = vars
    return (x - 1)**2 + (y - 2.5)**2

# Define the constraints
constraints = [
    {'type': 'ineq', 'fun': lambda vars: 6 - (vars[0] + 2 * vars[1])},  # x + 2y <= 6
    {'type': 'ineq', 'fun': lambda vars: 2 - (-vars[0] + 2 * vars[1])}, # -x + 2y <= 2
]

# Define the bounds
bounds = [(0, None), (0, None)]  # x >= 0, y >= 0

# Initial guess
initial_guess = [0.5, 0.5]

# Solve the problem
result = minimize(objective, initial_guess, method='SLSQP', bounds=bounds, constraints=constraints)

print('Optimal value:', result.fun)
print('X:', result.x)
print('Success:', result.success)
print('Message:', result.message)

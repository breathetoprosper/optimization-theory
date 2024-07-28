# Gradient Descent explained

import numpy as np

# Define the function
def f(x, y):
    return (x - 3)**2 + (y + 4)**2

# Define the gradient of the function
def gradient(x, y):
    df_dx = 2 * (x - 3)
    df_dy = 2 * (y + 4)
    return np.array([df_dx, df_dy])

# Gradient descent parameters
alpha = 0.1  # Learning rate
tolerance = 1e-6  # Convergence criterion
max_iterations = 1000  # Maximum number of iterations

# Initial guess
x, y = 0.0, 0.0

# Gradient descent loop
for _ in range(max_iterations):
    grad = gradient(x, y)
    new_x, new_y = x - alpha * grad[0], y - alpha * grad[1]

    # Check for convergence
    if np.sqrt((new_x - x)**2 + (new_y - y)**2) < tolerance:
        break

    x, y = new_x, new_y

# Output the results
print(f'Optimal value: f({x:.6f}, {y:.6f}) = {f(x, y):.6f}')
print(f'Optimal x: {x:.6f}')
print(f'Optimal y: {y:.6f}')

'''
Example Problem

Maximize z= 3x1 + 2x2

Subject to:
x1 + x2 ≤ 4
x1 - x2 ≤ 2
x1, x2 ≥0​
'''

from scipy.optimize import linprog

# Coefficients of the objective function
c = [-3, -2]  # Maximize 3x1 + 2x2 (negative because linprog does minimization)

# Coefficients of the inequality constraints
A = [[1, 1], [1, -1]]
b = [4, 2]

# Bounds for x1 and x2
x0_bounds = (0, None)
x1_bounds = (0, None)

# Solve the problem
res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs') # highs is simplex

print('Optimal value:', -res.fun, '\nX:', res.x)
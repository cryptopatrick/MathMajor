import numpy as np

# Define the function to integrate
def f(x):
    return np.exp(-x**2)

# Define integration limits
a, b = 0, 3

# Number of rectangles (higher n gives better approximation)
n = 100

# Width of each rectangle
dx = (b - a) / n

# Right endpoints
x_right = np.linspace(a + dx, b, n)

# Compute the sum using the right rectangle method
approximation = np.sum(f(x_right) * dx)

# Round to four decimal places
approximation = round(approximation, 5)

print(approximation)

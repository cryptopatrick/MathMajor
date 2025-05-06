import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the range for x and y
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)

# Create a meshgrid
X, Y = np.meshgrid(x, y)

# Compute Z^2 values
Z_squared = (6 - 3*X**2 - Y**2) / 2

# Mask values where Z^2 is negative (no real solutions)
Z_squared[Z_squared < 0] = np.nan

# Compute positive and negative Z
Z1 = np.sqrt(Z_squared)
Z2 = -np.sqrt(Z_squared)

# Plot the surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(X, Y, Z1, color='b', alpha=0.6, edgecolor='k')
ax.plot_surface(X, Y, Z2, color='r', alpha=0.6, edgecolor='k')

# Labels
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("Surface Plot of 3x² + y² + 2z² = 6")

plt.show()

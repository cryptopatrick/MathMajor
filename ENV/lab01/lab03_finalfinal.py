# Display results
#import ace_tools as tools
import pandas as pd
import numpy as np

# Define the coefficient matrix A (9x9)
A = np.array([
    [ 4, -1,  0, -1,  0,  0,  0,  0,  0],
    [-1,  4, -1,  0, -1,  0,  0,  0,  0],
    [ 0, -1,  4,  0,  0, -1,  0,  0,  0],
    [-1,  0,  0,  4, -1,  0, -1,  0,  0],
    [ 0, -1,  0, -1,  4, -1,  0, -1,  0],
    [ 0,  0, -1,  0, -1,  4,  0,  0, -1],
    [ 0,  0,  0, -1,  0,  0,  4, -1,  0],
    [ 0,  0,  0,  0, -1,  0, -1,  4, -1],
    [ 0,  0,  0,  0,  0, -1,  0, -1,  4]
])

# Define the right-hand side vector b considering boundary conditions
b = np.array([
    35 + 35, 35, 35 + 63,
    35,      0, 63,
    35 + 7,  7,  7 + 63
])

# Solve the system Au = b
u = np.linalg.solve(A, b)

# Reshape the solution into a 3x3 grid
u_grid = u.reshape((3, 3))


#df = pd.DataFrame(u_grid, columns=['Node 1', 'Node 2', 'Node 3'], index=['Row 1', 'Row 2', 'Row 3'])
#tools.display_dataframe_to_user(name="Temperature Distribution", dataframe=df)

# Extract temperatures of Node 4 and Node 8 (1-based index)
node_4_temperature = u[3]  # Index 3 in zero-based Python index
node_8_temperature = u[7]  # Index 7 in zero-based Python index
node_2_temperature = u[1]  # Index 7 in zero-based Python index

print(node_4_temperature, node_8_temperature)
print(node_2_temperature)

import numpy as np
from sympy import Matrix
import pandas as pd

# Define the coefficient matrix A and the right-hand side vector b
A = np.array([
    [52, -1, 9, -11],
    [-1, 3, 3, -2],
    [9, 3, 5, -4],
    [-5, -1, -2, 2]
])

b = np.array([-56, 8, -2, 3])

# Augment the matrix [A | b]
augmented_matrix = np.column_stack((A, b))

# Convert to sympy Matrix and compute RREF
rref_matrix, pivot_columns = Matrix(augmented_matrix).rref()

# Convert the RREF matrix to a DataFrame for display
rref_df = pd.DataFrame(np.array(rref_matrix, dtype=float))

# Display the RREF result
print("Reduced Row Echelon Form (RREF):")
print(rref_df)
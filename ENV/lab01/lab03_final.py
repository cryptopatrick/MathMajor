import numpy as np
from sympy import Matrix
import pandas as pd


A = np.array([
    [17, 17, -17],
    [-12, -23, -21],
    [-22, 20, 148],
    [-13, 0, 52]
])

#b = np.array([-66, -76, -84, 73])
b = np.array([-34, 13, 86, 39])

# Compute the ranks
rank_A = np.linalg.matrix_rank(A)
rank_A_augmented = np.linalg.matrix_rank(np.column_stack((A, b)))
num_columns = A.shape[1]

# Determine the number of solutions
if rank_A < rank_A_augmented:
    solution_status = "No solution (inconsistent system)"
elif rank_A == num_columns:
    solution = np.linalg.lstsq(A, b, rcond=None)[0]
    solution_status = "Unique solution"
else:
    # Infinite solutions: find one particular solution
    solution = np.linalg.pinv(A) @ b
    solution_status = "Infinitely many solutions"

#print((rank_A, rank_A_augmented, solution_status))
print(solution_status)
print("Solution:")
print(solution)

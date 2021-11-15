"""
18. Write a Python program to create a 3-D array with ones on a diagonal and zeros elsewhere.
Expected Output:
[[ 1. 0. 0.]
[ 0. 1. 0.]
[ 0. 0. 1.]]
"""
import numpy as np

diagonal_matrix = np.eye(3, dtype=float)

print(diagonal_matrix)
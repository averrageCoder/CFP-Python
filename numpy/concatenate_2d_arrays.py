"""
20. Write a Python program to concatenate two 2-dimensional arrays. Expected Output:
Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]
Expected Output:
[[ 0 1 3 0 2 4]
[ 5 7 9 6 8 10]]
"""

import numpy as np

arr1 = [[0, 1, 3], [5, 7, 9]]
arr2 = [[0, 2, 4], [6, 8, 10]]

concatenated_array = np.concatenate((arr1, arr2), axis=1)

print(concatenated_array)

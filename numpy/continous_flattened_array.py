"""
16. Write a Python program to create a contiguous flattened array. Original array:
[[10 20 30]
[20 40 50]]
New flattened array:
[10 20 30 20 40 50]
"""

import numpy as np

array1 = np.array([[10, 20, 30], [20, 40, 50]])

result_array = array1.flatten()

print(result_array)
"""
14. Write a Python program to find the set exclusive-or of two arrays.
Set exclusive-or will return the sorted, unique values that are in only one (not both) of the input arrays.
Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70]
Unique values that are in only one (not both) of the input arrays:
[ 0 20 30 50 60 70 80]
"""

import numpy as np

arr1 = [0, 10, 20, 40, 60, 80]
arr2 = [10, 30, 40, 50, 70]

exclusive_or_set = np.setxor1d(arr1, arr2)

print("Unique values that are in only one (not both) of the input arrays: ", exclusive_or_set)

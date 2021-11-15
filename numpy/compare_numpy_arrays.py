"""
15. Write a Python program compare two arrays using numpy.
Array a: [1 2]
Array b: [4 5]
a > b
[False False]
a >= b
[False False]
a < b
[ True True]
a <= b
[ True True]
"""

import numpy as np

array1 = np.array([1, 2])
array2 = np.array([4, 5])

print(array1 > array2)
print(array1 >= array2)
print(array1 < array2)
print(array1 <= array2)
import numpy as np

"""
1. Write a Python program to convert a list of numeric value into a one-dimensional NumPy array. 
Expected Output: 
Original List: [12.23, 13.32, 100, 36.32] 
One-dimensional numpy array: [ 12.23 13.32 100. 36.32] 
"""
original_list = [12.23, 13.32, 100, 36.32]
my_numpy_array = np.asarray(original_list, dtype=np.float32)
print(my_numpy_array)
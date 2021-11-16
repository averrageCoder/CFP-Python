"""
1. Write a Python program to create and display a one-dimensional array-like object
containing an array of data using Pandas module.
"""

import pandas as pd
ds = pd.Series([2, 4, 6, 8, 10])
print(ds)

print(type(ds))
print("Convert Pandas Series to Python list")
print(ds.tolist())
print(type(ds.tolist()))
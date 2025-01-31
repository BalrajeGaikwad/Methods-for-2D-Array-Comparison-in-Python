"""
 Check if Arrays are Exactly Equal (Overall)

"""

import numpy as np

arr1 = np.array([[1, 2], [3, 4], [5, 6]])
arr2 = np.array([[1, 2], [3, 4], [5, 7]])

print(arr1)
print(arr2)

equal=np.array_equal(arr1,arr2)
print(equal)
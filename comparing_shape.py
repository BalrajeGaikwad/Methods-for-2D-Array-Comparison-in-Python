import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4]])

compare=arr1.shape==arr2.shape
print(compare)
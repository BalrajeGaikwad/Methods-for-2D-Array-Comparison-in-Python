"""
 Using np.allclose() (Floating Point Comparisons)
If you are dealing with floating point numbers and want to check if they are approximately equal (within a tolerance), you can use np.allclose().

"""
import numpy as np
arr1 = np.array([[1.0001, 2.0001], [3.0001, 4.0001]])
arr2 = np.array([[1.0002, 2.0002], [3.0002, 4.0002]])

approximately_equal=np.allclose(arr1,arr2, atol=0.001)
print(approximately_equal)
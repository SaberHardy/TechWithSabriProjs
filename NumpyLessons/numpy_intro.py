# list_nbrs = [0, 1, 2, 3, 4, 5]
# list_strs = ["1", "2", "3"]
# print(list_nbrs)
# print(list_strs)
#
# all_items = [list_nbrs, list_strs]
# print(all_items)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr[1:4])  # Output: [2 3 4]

# 2. Slicing with Step
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr[1:7:2])  # Output: [2 4 6]

# 3. Negative Indexing in Slicing
arr = np.array([10, 20, 30, 40, 50])
print(arr[-4:-1])  # Output: [20 30 40]

# 4.1 Slicing Multi-Dimensional Arrays
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[1:, 1:])  # Output: [[5 6], [8 9]]
# 4.2 3D
arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d[:, 1, :])  # Output: [[3 4], [7 8]]

# 5. Ellipsis Slicing
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[..., 1])  # Output: [[2 5], [8 11]]

# 6. Combining Slicing and Integer Indexing
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr_2d[1, 1:])  # Output: [5 6]

# 7. Slicing with Boolean Masks
arr = np.array([10, 20, 30, 40, 50])
mask = arr > 30
print(arr[mask])  # Output: [40 50]

# 8. Slicing Along Custom Axes
arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(arr_3d[1, :, 1])  # Output: [8 11]

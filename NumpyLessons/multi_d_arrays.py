import numpy as np

array = np.array([1, 2, 3, 4, 5, 6, 7, 3, 8, 9])

# for item in array:
#     print(item)
#
array_2d = np.array([[10, 30, 20], [2, 4, 6], [6, 9, 8]])
#
# for item in array_2d:
#     for sec in item:
#         print(sec)
#
# array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 6, 3], [5, 7, 9]], [[1, 2, 3], [4, 5, 6]], [[7, 6, 3], [5, 7, 9]]])
# print(f"shape: {array_3d.shape}")
# for index1 in array_3d:
#     for index2 in index1:
#         for index3 in index2:
#             print(index3)
#
# for item in np.nditer(array_3d):
#     print(item)

# item = np.where(array == 3)
# print(item)

# Search in 2D array

# number_6 = np.where(array_2d == 6)
# print(number_6)


items = np.where((array_2d > 2) & (array_2d < 7))

print(items)

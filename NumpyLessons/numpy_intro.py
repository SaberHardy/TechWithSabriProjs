# list_nbrs = [0, 1, 2, 3, 4, 5]
# list_strs = ["1", "2", "3"]
# print(list_nbrs)
# print(list_strs)
#
# all_items = [list_nbrs, list_strs]
# print(all_items)

import numpy as np

array_example = np.array([0, 1, 2, 3, 4, 5])
print(array_example)

print(array_example.shape)

array_example_2 = np.arange(0, 10)
print(array_example_2)

array_example_3 = np.arange(0, 10, 2)
print(array_example_3)

zero_array = np.zeros(10)
print(zero_array)

ones_array = np.ones(10)
print(ones_array)

multi_dim_ones = np.zeros((3, 3))
print(multi_dim_ones)

multi_fours = np.full((5, 5), 4)
print(multi_fours)

print(multi_fours * 2)

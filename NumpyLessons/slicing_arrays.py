import numpy as np

# example_array = np.array([0, 1, 2, 3, 4, 5, 6])
# example_array = np.arange(0, 10)
# print(example_array)
#
# from_one_to_five = example_array[1:6]
# print(from_one_to_five)
#
# print(example_array[3:])
#
# print(example_array[-4:-1])
#
# print(example_array[0:7:2])

two_d_array = np.array([
   # 0  1  2  3  4
    [1, 2, 3, 4, 5],    # 0
    [6, 7, 8, 9, 0],    # 1
    [2, 99, 7, 8, 9],    # 2
    [34, 56, 76, 9, 0]  # 3
])

print(two_d_array)
print(two_d_array[2, 1])

print(two_d_array[1:3, 1:4])


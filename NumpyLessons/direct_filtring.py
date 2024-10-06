import numpy as np


# Direct Comparison

# arr_1 = np.array([1, 2, 3, 4, 5, 20, 10, 69, 30])
# filtered_arr = arr_1[arr_1 >= 3]
#
# print(filtered_arr)

# Boolean indexing
# condition = arr_1 % 2 != 0  # odd numbers
# filtered_arr = arr_1[condition]
#
# print(filtered_arr)

# Multi-Conditions

# condition_1 = arr_1 > 2
# condition_2 = arr_1 < 20
#
# filtered_arr = arr_1[(condition_1 & condition_2)]
# print(filtered_arr)

# Logical Operation
# filtered_arr = arr_1[(arr_1 > 2) | (arr_1 < 3)]
# print(filtered_arr)

# indexes = np.where((arr_1 > 2) & (arr_1 < 5))
# filt = arr_1[indexes]
# print(filt)

# Filter by Nan values
# arr_1 = np.array([np.nan, 6, np.nan, 9, 435, 789, np.nan, 7])
# indexes = arr_1[~np.isnan(arr_1)]
# print(indexes)

def is_even(nbr):
    return nbr % 2 == 0


array = np.array([2, 5, 79, 4478, 78, 945, 6, 43, 689, 346])
filtered_array = array[np.vectorize(is_even)(array)]

print(filtered_array)

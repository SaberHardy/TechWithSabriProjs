import numpy as np

# array_1 = np.array([1, 2])
# array_2 = np.array([3, 4])
# array_3 = np.array([3, 5])
#
# # Stacking arrays vertically
# v_stack = np.vstack((array_1, array_2, array_3))
# print(f"V_stack array\n{v_stack}")
# print(f"Shape of my new array: {v_stack.shape}")
#
# concatenated = np.concatenate((array_1, array_2))
# print(f"Concatenated arrays: {concatenated} ")

# Transposing a 2D array
array_np = np.array([[1, 2], [3, 4]])

print("original array:\n", array_np)
transposed_array = array_np.T
print(f"Transposed Array:\n {transposed_array}")

random_sample = np.random.choice([2, 8, 0, 4], size=8)
print(f"Random Simple:\n{random_sample}")

arra_non_null = np.array([1, 2, np.nan, np.inf])
nan_check = np.isnan(arra_non_null)
print(f"nan_check is: {nan_check}")

null_check = np.isinf(arra_non_null)
print(f"null_check is: {null_check}")


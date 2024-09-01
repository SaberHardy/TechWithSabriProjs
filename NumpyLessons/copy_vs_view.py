import numpy as np
#
# my_array = np.array([1, 2, 3, 4, 5])
# print(f"Original array: {my_array}")
#
# my_view_arr = my_array.view()
# print(f"My view is: {my_view_arr}")
#
# my_view_arr[0] = 50
# print(f"My new view is: {my_view_arr}")
# print(f"Original array after modification: {my_array}")

# Copy
my_array = np.array([1, 2, 3, 4, 5])

copy_arr = my_array.copy()
print(f"Copy array is: {copy_arr}")

copy_arr[0] = 90
print(f"Copy array after modification: {copy_arr}")
print(f"Original array after modification: {my_array}")

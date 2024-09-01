import numpy as np

# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# #               [5  7  9]
# sum_arrays = np.add(arr1, arr2)
# print(f"The sum of the array: {sum_arrays}")
#
# mult_array = np.multiply(arr1, arr2)
# print(f"The multiplication of two arrays is: {mult_array}")
#
# print(f"The Square Root is: {np.sqrt(arr2)}")
#
# angles = np.array([0, np.pi / 2, np.pi])
#
# output = np.sin(angles)
# print(f"Sin: {output}")
#
# cos_result = np.cos(angles)
# print(f"Cos: {cos_result}")
#
# expon = np.exp(angles)
# print(f"Exp: {expon}")
#
# array_log = np.array([1, np.e, np.e ** 2])
# log_res = np.log(array_log)
# print(f"Log results: {log_res}")
#
# max = np.max(arr1)
# min = np.min(arr2)
# print(f"max {max} and min: {min}")
#

array_1 = np.array([True, False, True, True, False])
array_2 = np.array([False, True, False, True, False])

and_res = np.logical_and(array_1, array_2)
print(and_res)  # False, False, False, False

logic_or = np.logical_or(array_1, array_2)
print(logic_or)  # True,True,True,True

logic_not = np.logical_not(array_1, array_2)
print(logic_not)  # False, True, False, False, True

# Bitwise functions

arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])

res1 = np.bitwise_and(arr_1, arr_2)
print(res1)

res2 = np.bitwise_or(arr_1, arr_2)
print(res2)

res3 = np.bitwise_xor(arr_1, arr_2)
print(res3)

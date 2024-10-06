import numpy as np

# arr1 = np.random.randint(0, 5, size=(3, 4))
# arr2 = np.random.randint(0, 100, size=(4, 4))
#
# print("Original array 1: \n", arr1)
# print("\n")
# print("Original array 2: \n", arr2)

# Extract the second row of the array
# print("\n")
# print("The extracted rows: ")
# second_row = arr[1, :]
# print(second_row)

# Replace the third column of the array with zeros
# arr[:, 2] = 0
# print(arr)

# reshape the array to 2, 6
# reshaped_array = arr.reshape(6, 2)
# print(f"Reshaped array: \n {reshaped_array}")


# Transposing arrays
# print(arr.T)

# Concatenate arrays

# concatinated_arrys = np.concatenate((arr1, arr2), axis=0)
# print(concatinated_arrys)

# split arrays:
# sub_array1, sub_array2 = np.vsplit(arr1, 2)
# print(sub_array1)
# print("\n")
# print(sub_array2)

# arr1 = np.random.rand(2, 3, 4)
# print(f"Array 1: \n{arr1}")
#
# sub_array = arr1[:2, :, -2:]
#
# print(f"\n\nsub array:\n {sub_array}")


# dot_product = np.dot(arr1, arr2)
# print(f"dot product: {dot_product}")
#
#
# # apply a custom function to each element
# def my_custom_func(x):
#     return x ** 2
#
#
# squared_array = np.apply_along_axis(my_custom_func, 0, arr1)
# print(f"squared_array: \n{squared_array}")
#
import matplotlib.pyplot as plt
# import matplotlib.image as img
# import cv2 as cv2
#
# image = img.imread('/Users/macbook/PycharmProjects/TechWithSabri/static_files/kid.jpg')
#
#
# plt.imshow(image)
# # plt.axis('off')  # Optional: Hide the axis

import seaborn as sns

tips = sns.load_dataset("tips")
sns.relplot(data=tips, x='total_bill', y='tip')

plt.show()

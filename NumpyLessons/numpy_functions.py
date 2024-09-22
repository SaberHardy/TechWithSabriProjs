import numpy as np

# my_array = np.array([3, 5, 8, 1])
#
# print("Aggregation Functions")
# print(f"Sum elements: {np.sum(my_array)}")
#
# print(f"Mean of the elements: {np.mean(my_array)}")
# print(f"Median of the array is: {np.median(my_array)}")
# print(f"Standard Deviation is: {np.std(my_array)}")
# print(f"Variance is {np.var(my_array)}")
#


# print("Correlation and Covariance")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([5, 4, 3, 2, 1])
#
# print(f"Correlation Coefficient: \n{np.corrcoef(arr1, arr2)}")
#
# print(f"Covariance: {np.cov(arr1, arr2)}")

# Maximum & Minimum
print(f"Max: {np.max(arr1)}")
print(f"Max: {np.max(arr2)}")
print(f"Min: {np.min(arr1)}")
print(f"Min: {np.min(arr2)}")

# Percentile & Quantiles
print(f"Percentile: {np.percentile(arr1, 25)}")
print(f"Quantile: {np.quantile(arr1, 0.25)}")



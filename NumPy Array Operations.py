# Task 1: Create a 5x5 matrix where border elements are 1 and interior is 0

import numpy as np

#create 5*5 matrix 
matrix = np.ones((5, 5))

matrix[1:-1, 1:-1] = 0

print("5x5 border Matrix:")
print(matrix)

np.random.seed(42)
random_data = np.random.randn(100, 3)



#TASK 2: # Task 2: Normalize a random array
# Column normalization
mean = np.mean(random_data, axis=0)
std = np.std(random_data, axis=0)

normalized_data = (random_data - mean) / std

print("Means after normalization (should be ~0):")
print(np.mean(normalized_data, axis=0))

print("\nStd dev after normalization (should be ~1):")
print(np.std(normalized_data, axis=0))


#TASK 3: Task 3: Implement linear regression solution using normal equation
# Data generation
X = np.random.randn(50, 3)
true_theta = np.array([2.5, -1.2, 3.7])
y = X @ true_theta + np.random.randn(50) * 0.1

# Normal equation: theta = (X^T X)^(-1) X^T y
theta_hat = np.linalg.inv(X.T @ X) @ X.T @ y

print("True theta:")
print(true_theta)

print("\nEstimated theta_hat:")
print(theta_hat)
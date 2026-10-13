#Write a Python program to flatten the image matrix into a one-dimensional vector and  calculate the sum of all pixel intensities. 


import numpy as np
import matplotlib.pyplot as plt

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print("Vector A:", a)
print("Vector B:", b)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Dot Product:", np.dot(a, b))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("\nMatrix Addition:\n", A + B)
print("Matrix Multiplication:\n", A @ B)
print("Transpose of A:\n", A.T)

plt.plot(a, label="Vector A", marker="o")
plt.plot(b, label="Vector B", marker="o")
plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Vector Visualization")
plt.legend()
plt.show()

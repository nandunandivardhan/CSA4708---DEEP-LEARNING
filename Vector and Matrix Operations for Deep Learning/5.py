#Write a Python program to perform vector addition and calculate the dot product of the two  movie feature vectors. Display both results.
import numpy as np

A = np.array([2, 4, 6])
B = np.array([1, 3, 5])

addition = A + B
dot_product = np.dot(A, B)

print("Vector A:", A)
print("Vector B:", B)
print("Combined Vector:", addition)
print("Dot Product:", dot_product)

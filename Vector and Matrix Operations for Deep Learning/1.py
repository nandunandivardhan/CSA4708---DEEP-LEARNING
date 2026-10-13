
import numpy as np

A = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

vector = A.flatten()

print("Image Matrix:")
print(A)
print("Flattened Vector:", vector)
print("Total Pixel Intensity:", np.sum(A))

#Covariance between study hours and marks

import numpy as np
import matplotlib.pyplot as plt

hours = np.array([2, 4, 6, 8, 10])
marks = np.array([35, 45, 60, 75, 85])

cov = np.cov(hours, marks)[0, 1]

print("Study Hours:", hours)
print("Marks:", marks)
print("Sample Covariance:", cov)

plt.scatter(hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.grid(True)
plt.show()

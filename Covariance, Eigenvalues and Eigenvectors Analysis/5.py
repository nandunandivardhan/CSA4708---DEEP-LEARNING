#Identify the principal direction of sensor data

import numpy as np
import matplotlib.pyplot as plt

C = np.array([[5, 2],
              [2, 2]])

values, vectors = np.linalg.eigh(C)

print("Covariance Matrix:")
print(C)
print("Eigenvalues:", values)
print("Eigenvectors:")
print(vectors)

index = np.argmax(values)
principal = vectors[:, index]

print("Largest Eigenvalue:", values[index])
print("Principal Eigenvector:", principal)

for i in range(len(values)):
    v = vectors[:, i]
    plt.quiver(0, 0, v[0], v[1],
               angles="xy", scale_units="xy",
               scale=1, label=f"Eigenvalue {values[i]}")

plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Principal Direction of Sensor Data")
plt.grid(True)
plt.legend()
plt.show()

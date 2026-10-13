#Calculate and plot eigenvectors

import numpy as np
import matplotlib.pyplot as plt

C = np.array([[3, 1],
              [1, 3]])

values, vectors = np.linalg.eigh(C)

print("Covariance Matrix:")
print(C)
print("Eigenvalues:", values)
print("Eigenvectors:")
print(vectors)

for i in range(len(values)):
    v = vectors[:, i]
    plt.quiver(0, 0, v[0], v[1],
               angles="xy", scale_units="xy",
               scale=1, label=f"Eigenvalue {values[i]}")

plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Eigenvectors")
plt.grid(True)
plt.legend()
plt.show()

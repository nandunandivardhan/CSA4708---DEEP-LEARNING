#Calculate cross-entropy loss

import numpy as np
import matplotlib.pyplot as plt

Y = np.array([1, 0, 0])
P = np.array([0.7, 0.2, 0.1])

loss = -np.sum(Y * np.log(P))

print("Actual Distribution:", Y)
print("Predicted Probabilities:", P)
print("Cross-Entropy Loss:", round(loss, 4))

labels = ["Cat", "Dog", "Bird"]
x = np.arange(len(labels))
width = 0.35

plt.bar(x - width/2, Y, width, label="Actual")
plt.bar(x + width/2, P, width, label="Predicted")
plt.xticks(x, labels)
plt.ylabel("Probability")
plt.title("Actual vs Predicted Probabilities")
plt.legend()
plt.show()

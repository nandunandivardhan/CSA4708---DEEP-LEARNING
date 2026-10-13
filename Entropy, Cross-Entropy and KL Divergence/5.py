#Calculate cross-entropy and KL divergence

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

Y = np.array([0, 1, 0, 0])
P = np.array([0.1, 0.6, 0.2, 0.1])

cross_entropy = -np.sum(Y * np.log(P))
kl = entropy(Y, P)

print("Actual Distribution:", Y)
print("Predicted Distribution:", P)
print("Cross-Entropy Loss:", round(cross_entropy, 4))
print("KL Divergence:", round(kl, 4))

labels = ["Class 1", "Class 2", "Class 3", "Class 4"]
x = np.arange(len(labels))
width = 0.35

plt.bar(x - width/2, Y, width, label="Actual")
plt.bar(x + width/2, P, width, label="Predicted")
plt.xticks(x, labels)
plt.ylabel("Probability")
plt.title("Actual vs Predicted Distribution")
plt.legend()
plt.show()

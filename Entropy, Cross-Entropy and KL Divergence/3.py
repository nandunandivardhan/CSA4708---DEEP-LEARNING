#Calculate KL divergence

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

P = np.array([0.5, 0.3, 0.2])
Q = np.array([0.4, 0.4, 0.2])

kl = entropy(P, Q)

print("Distribution P:", P)
print("Distribution Q:", Q)
print("KL Divergence:", round(kl, 4))

labels = ["Word 1", "Word 2", "Word 3"]
x = np.arange(len(labels))
width = 0.35

plt.bar(x - width/2, P, width, label="P")
plt.bar(x + width/2, Q, width, label="Q")
plt.xticks(x, labels)
plt.ylabel("Probability")
plt.title("Comparison of Probability Distributions")
plt.legend()
plt.show()

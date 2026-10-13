#Calculate entropy of weather predictions

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

P = np.array([0.6, 0.3, 0.1])

H = entropy(P, base=2)

print("Probabilities:", P)
print("Entropy:", round(H, 4), "bits")

labels = ["Sunny", "Rainy", "Cloudy"]
plt.bar(labels, P)
plt.xlabel("Weather Condition")
plt.ylabel("Probability")
plt.title("Weather Probability Distribution")
plt.show()

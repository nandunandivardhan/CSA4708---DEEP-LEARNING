#Poisson distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lam = 4

probability = poisson.pmf(6, lam)

print("Probability of exactly 6 customers:",
      round(probability, 4))

x = np.arange(0, 13)
y = poisson.pmf(x, lam)

plt.bar(x, y)
plt.xlabel("Number of Customers")
plt.ylabel("Probability")
plt.title("Poisson Distribution")
plt.xticks(x)
plt.grid(axis="y")
plt.show()

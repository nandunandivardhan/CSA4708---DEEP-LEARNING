#Binomial distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 20
p = 0.1

probability = binom.pmf(3, n, p)

print("Probability of exactly 3 defective components:",
      round(probability, 4))

x = np.arange(0, 21)
y = binom.pmf(x, n, p)

plt.bar(x, y)
plt.xlabel("Number of Defective Components")
plt.ylabel("Probability")
plt.title("Binomial Distribution")
plt.show()

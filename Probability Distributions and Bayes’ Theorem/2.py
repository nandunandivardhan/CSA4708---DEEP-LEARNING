#Normal distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean = 70
sd = 10

probability = norm.cdf(80, mean, sd) - norm.cdf(60, mean, sd)

print("Probability of scoring between 60 and 80:",
      round(probability, 4))

x = np.linspace(40, 100, 300)
y = norm.pdf(x, mean, sd)

plt.plot(x, y, label="Normal Distribution")

x_fill = np.linspace(60, 80, 150)
plt.fill_between(x_fill, norm.pdf(x_fill, mean, sd),
                 alpha=0.4, label="Between 60 and 80")

plt.xlabel("Examination Marks")
plt.ylabel("Probability Density")
plt.title("Normal Distribution of Marks")
plt.legend()
plt.grid(True)
plt.show()

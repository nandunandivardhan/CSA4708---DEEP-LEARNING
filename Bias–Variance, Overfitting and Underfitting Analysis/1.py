#Compare polynomial regression models

import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

np.random.seed(42)

X = np.linspace(50, 200, 20).reshape(-1, 1)
y = 1000 + 20 * X.ravel() + 0.5 * X.ravel()**2
y += np.random.normal(0, 300, len(X))

X_plot = np.linspace(50, 200, 200).reshape(-1, 1)

plt.scatter(X, y, color="black", label="Actual Data")

for degree in [1, 2, 10]:
    model = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )
    model.fit(X, y)
    predictions = model.predict(X_plot)
    plt.plot(X_plot, predictions, label=f"Degree {degree}")

plt.xlabel("House Area")
plt.ylabel("House Price")
plt.title("Polynomial Regression Comparison")
plt.legend()
plt.grid(True)
plt.show()

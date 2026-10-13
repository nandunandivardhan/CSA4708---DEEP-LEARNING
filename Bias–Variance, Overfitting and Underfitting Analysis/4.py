#Select a suitable polynomial degree

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

np.random.seed(42)

X = np.linspace(0, 10, 60).reshape(-1, 1)
y = 20 + 3 * X.ravel() + 5 * np.sin(X.ravel())
y += np.random.normal(0, 1.5, len(X))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

X_plot = np.linspace(0, 10, 200).reshape(-1, 1)

for degree in [1, 3, 12]:
    model = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )
    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    print("Degree:", degree)
    print("Training MSE:",
          round(mean_squared_error(y_train, train_pred), 4))
    print("Testing MSE:",
          round(mean_squared_error(y_test, test_pred), 4))

    plt.plot(X_plot, model.predict(X_plot),
             label=f"Degree {degree}")

plt.scatter(X, y, label="Actual Temperature")
plt.xlabel("Time")
plt.ylabel("Temperature")
plt.title("Temperature Prediction Comparison")
plt.legend()
plt.grid(True)
plt.show()

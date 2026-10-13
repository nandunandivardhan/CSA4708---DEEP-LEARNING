#Compare degree 2 and degree 15 models

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

np.random.seed(42)

X = np.linspace(0, 1, 40).reshape(-1, 1)
y = np.sin(2 * np.pi * X).ravel()
y += np.random.normal(0, 0.15, len(X))

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

X_plot = np.linspace(0, 1, 200).reshape(-1, 1)

plt.scatter(X_train, y_train, label="Training Data")
plt.scatter(X_test, y_test, label="Testing Data")

for degree in [2, 15]:
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

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Polynomial Regression: Overfitting Analysis")
plt.legend()
plt.grid(True)
plt.show()

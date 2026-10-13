#Learning curves for bias and variance

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline

np.random.seed(42)

X = np.linspace(0, 1, 80).reshape(-1, 1)
y = np.sin(2 * np.pi * X).ravel()
y += np.random.normal(0, 0.2, len(X))

models = {
    "Linear Regression": LinearRegression(),
    "Polynomial Degree 15": make_pipeline(
        PolynomialFeatures(15),
        LinearRegression()
    )
}

for name, model in models.items():
    sizes, train_scores, val_scores = learning_curve(
        model, X, y,
        cv=5,
        train_sizes=np.linspace(0.2, 1.0, 5),
        scoring="neg_mean_squared_error"
    )

    train_error = -train_scores.mean(axis=1)
    val_error = -val_scores.mean(axis=1)

    print("\nModel:", name)
    print("Training Errors:", np.round(train_error, 4))
    print("Validation Errors:", np.round(val_error, 4))

    plt.plot(sizes, train_error, marker="o",
             label=f"{name} Training")
    plt.plot(sizes, val_error, marker="s",
             linestyle="--", label=f"{name} Validation")

plt.xlabel("Number of Training Samples")
plt.ylabel("Mean Squared Error")
plt.title("Learning Curves: Bias and Variance")
plt.legend()
plt.grid(True)
plt.show()

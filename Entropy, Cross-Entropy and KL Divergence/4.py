#Compare entropy of two predictions

import matplotlib.pyplot as plt
from scipy.stats import entropy

P = [0.9, 0.1]
Q = [0.5, 0.5]

H_P = entropy(P, base=2)
H_Q = entropy(Q, base=2)

print("Entropy of P:", round(H_P, 4), "bits")
print("Entropy of Q:", round(H_Q, 4), "bits")

labels = ["P: [0.9, 0.1]", "Q: [0.5, 0.5]"]
values = [H_P, H_Q]

plt.bar(labels, values)
plt.ylabel("Entropy (bits)")
plt.title("Comparison of Prediction Entropy")
plt.show()

if H_P > H_Q:
    print("P has greater uncertainty")
else:
    print("Q has greater uncertainty")

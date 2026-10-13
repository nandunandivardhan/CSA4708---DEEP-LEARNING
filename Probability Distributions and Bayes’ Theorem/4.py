#Bayes' theorem for disease testing

import matplotlib.pyplot as plt

p_disease = 0.02
p_positive_given_disease = 0.95
p_positive_given_no_disease = 0.05

p_positive = (
    p_positive_given_disease * p_disease
    + p_positive_given_no_disease * (1 - p_disease)
)

posterior = (
    p_positive_given_disease * p_disease
) / p_positive

print("Prior Probability of Disease:",
      round(p_disease, 4))
print("Probability of Positive Test:",
      round(p_positive, 4))
print("Probability of Disease Given Positive Test:",
      round(posterior, 4))
print("Posterior Percentage:", round(posterior * 100, 2), "%")

labels = ["Prior Probability", "Posterior Probability"]
values = [p_disease, posterior]

plt.bar(labels, values)
plt.ylabel("Probability")
plt.title("Disease Probability Before and After Test")
plt.ylim(0, 1)
plt.show()

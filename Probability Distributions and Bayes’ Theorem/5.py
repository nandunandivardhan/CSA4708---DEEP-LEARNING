#Bayes' theorem for spam email detection

import matplotlib.pyplot as plt

p_spam = 0.30
p_prize_given_spam = 0.70
p_prize_given_not_spam = 0.10

p_prize = (
    p_prize_given_spam * p_spam
    + p_prize_given_not_spam * (1 - p_spam)
)

posterior = (
    p_prize_given_spam * p_spam
) / p_prize

print("Prior Probability of Spam:", round(p_spam, 4))
print("Probability of Word Prize:", round(p_prize, 4))
print("Probability of Spam Given Prize:",
      round(posterior, 4))
print("Posterior Percentage:", round(posterior * 100, 2), "%")

labels = ["Prior Probability", "Posterior Probability"]
values = [p_spam, posterior]

plt.bar(labels, values)
plt.ylabel("Probability")
plt.title("Spam Probability Before and After Word Detection")
plt.ylim(0, 1)
plt.show()

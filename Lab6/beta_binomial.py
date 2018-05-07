import numpy as np
from scipy.stats import beta
from scipy.stats import binom
from scipy.stats import bernoulli


def likelihood(theta, data):
    ones = np.count_nonzero(data)
    return binom.pmf(ones, len(data) - ones, theta)


def prior(theta, a, b):
    return beta.pdf(theta, a, b)


def posterior(theta, data):
    return beta.pdf()


class BetaBinomial:
    def __init__(self, theta, a, b):
        self.a = a
        self.b = b
        self.theta = theta

    def likelihood(self, data):
        ones = np.count_nonzero(data)
        return binom.pmf(ones, len(data), self.theta)

    def prior(self):
        return beta.pdf(self.theta, self.a, self.b)

    def posterior(self, data):
        ones = np.count_nonzero(data)
        return beta.pdf(self.theta, ones + self.a, len(data) - ones + self.b)


if __name__ == '__main__':
    model = BetaBinomial(theta=None, a=2, b=2)
    data = [1]
    thetas = np.arange(0, 1, 0.01)

    for theta in thetas:
        model.theta = theta
    print(model.likelihood([1, 1, 1, 0, 0, 0]))

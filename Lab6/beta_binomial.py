import numpy as np
from scipy.stats import beta


def likelihood(theta, data):
    return (np.power(theta, np.count_nonzero(data))) * np.power((1 - theta), len(data) - np.count_nonzero(data))


def prior(theta, a, b):
    return beta.pdf(theta, a, b)


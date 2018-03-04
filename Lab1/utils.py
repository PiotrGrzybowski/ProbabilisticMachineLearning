import numpy as np
import random


def integer_generator_from_range(start, stop):
    while True:
        yield random.randint(start, stop - 1)


def normal_distribution_generator(mean, variance):
    while True:
        yield np.random.normal(mean, variance)


def multivariate_normal_distribution_generator(mean, cov):
    while True:
        yield np.random.multivariate_normal(mean, cov)
import numpy as np


def likelihood(data, concept):
    return np.power(1 / len(concept.extension), len(data))

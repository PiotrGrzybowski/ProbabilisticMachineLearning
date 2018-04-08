import numpy as np

from Lab4.concept import concept_power, concept_label


def likelihood(data, concept):
    return np.power(1 / concept_power(concept), len(data))


def likelihoods(data, concepts):
    return [(concept_label(concept), likelihood(data, concept)) for concept in concepts]


def posterior(data, concept, concepts, prior):
    return (prior[concept] * likelihood(data, concept)) / np.sum([prior[con] * likelihood(data, con) for con in concepts])


def posteriors(data, concepts, prior):
    return [(concept_label(concept), posterior(data, concept, concepts, prior)) for concept in concepts]


def maximum_a_posteriori_estimator(data, concepts, prior):
    return max([(concept_label(concept), (likelihood(data, concept)) * (prior[concept])) for concept in concepts], key=lambda x: x[1])


def maximum_likelihood_estimator(data, concepts):
    return max([(concept_label(concept), (likelihood(data, concept))) for concept in concepts], key=lambda x: x[1])
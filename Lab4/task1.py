from functools import partial

from Lab4.bayesian import maximum_a_posteriori_estimator, likelihoods, posteriors, maximum_likelihood_estimator
from Lab4.concept import is_odd, is_even, is_divisible_by_n, does_data_satisfy_concept
from Lab4.settings import STOP
from Lab4.utils import results_log, priors_log

if __name__ == "__main__":
    concepts = [is_odd, is_even] + [partial(is_divisible_by_n, n=i) for i in range(3, STOP + 1)]
    data = [6, 48]
    print("Data = {}".format(data))

    fine_concepts = [concept for concept in concepts if does_data_satisfy_concept(data, concept)]
    print(fine_concepts)
    results = likelihoods(data, fine_concepts)
    print("Likelihood: {}".format(results_log(results)))

    p = 0.1
    prior = {concept: (1 - p) / len(concepts) for concept in fine_concepts}
    prior[concepts[1]] = p
    print("Prior: {}".format(priors_log(prior)))

    results = posteriors(data, fine_concepts, prior)
    print("Posterior: {}".format(results_log(results)))

    results = maximum_a_posteriori_estimator(data, fine_concepts, prior)
    print("Maximum a posteriori estimator: {} -> {}".format(results[0], results[1]))

    results = maximum_likelihood_estimator(data, fine_concepts)
    print("Maximum likelihood estimator: {} -> {}".format(results[0], results[1]))

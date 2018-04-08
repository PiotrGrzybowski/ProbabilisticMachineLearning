from functools import partial

from Lab4.bayesian import likelihoods, posteriors, maximum_a_posteriori_estimator, maximum_likelihood_estimator
from Lab4.concept import is_even, is_odd, is_divisible_by_n, does_data_satisfy_concept
from Lab4.settings import START, STOP
import matplotlib.pyplot as plt

import numpy as np

from Lab4.utils import priors_log, results_log

if __name__ == "__main__":
    even_numbers = [k for k in range(START, STOP + 1) if is_even(k)]
    odd_numbers = [k for k in range(START, STOP + 1) if is_odd(k)]
    divisible_by_3 = [k for k in range(START, STOP + 1) if is_divisible_by_n(k, 3)]
    divisible_by_4 = [k for k in range(START, STOP + 1) if is_divisible_by_n(k, 4)]
    divisible_by_12 = [k for k in range(START, STOP + 1) if is_divisible_by_n(k, 12)]

    concepts = [is_even, is_odd, partial(is_divisible_by_n, n=3), partial(is_divisible_by_n, n=4), partial(is_divisible_by_n, n=12)]
    np.random.shuffle(divisible_by_12)

    prior = {concepts[0]: 0.35,
             concepts[1]: 0.35,
             concepts[2]: 0.15,
             concepts[3]: 0.1,
             concepts[4]: 0.05}

    print("Prior: {}".format(priors_log(prior)))

    data = []
    maps = []
    mles = []

    for item in divisible_by_12:
        data.append(item)
        print(data)
        fine_concepts = [concept for concept in concepts if does_data_satisfy_concept(data, concept)]
        print(fine_concepts)
        results = likelihoods(data, fine_concepts)
        print("Likelihood: {}".format(results_log(results)))

        results = posteriors(data, fine_concepts, prior)
        print("Posterior: {}".format(results_log(results)))

        results = maximum_a_posteriori_estimator(data, fine_concepts, prior)
        print("Maximum a posteriori estimator: {} -> {}".format(results[0], results[1]))
        maps.append(results[1])

        results = maximum_likelihood_estimator(data, fine_concepts)
        print("Maximum likelihood estimator: {} -> {}".format(results[0], results[1]))
        mles.append(results[1])

    plt.plot(list(range(1, len(data) + 1)), maps, label='MAP')
    plt.plot(list(range(1, len(data) + 1)), mles, label='MLE')
    plt.xlabel('Data size')
    plt.legend()

    plt.show()
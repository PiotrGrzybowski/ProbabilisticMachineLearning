import numpy as np
import itertools


def student_application(tries, successes, probabilities):
    faculties = set(np.arange(tries))
    combinations = set(itertools.combinations(faculties, successes))

    return np.sum([np.prod([probabilities[i] for i in combination]) *
                   np.prod([1 - probabilities[i] for i in faculties - set(combination)])
                   for combination in combinations])


if __name__ == "__main__":
    print(student_application(9, 0, [0.01] * 9))

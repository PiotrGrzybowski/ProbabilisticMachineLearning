import numpy as np
import scipy.special


def student_application(tries, successes, p):
    return scipy.special.binom(tries, successes) * np.power(p, successes) * np.power((1 - p), tries - successes)


if __name__ == "__main__":
    print(student_application(9, 0, 0.01))

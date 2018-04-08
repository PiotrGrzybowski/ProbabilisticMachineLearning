from functools import partial

from Lab4.settings import START, STOP


def is_even(x):
    return x % 2 == 0


def is_odd(x):
    return x % 2 == 1


def is_divisible_by_n(x, n):
    return x % n == 0


def does_data_satisfy_concept(data, concept):
    return all(concept(item) for item in data)


def concept_power(concept):
    return len([i for i in range(START, STOP + 1) if concept(i)])


def concept_label(concept):
    if isinstance(concept, partial):
        return "{}, n = {}".format(concept.func.__name__, concept.keywords['n'])
    else:
        return concept.__name__


if __name__ == "__main__":
    pass
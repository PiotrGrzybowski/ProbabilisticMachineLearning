import random


def integer_generator_from_range(start, stop):
    while True:
        yield random.randint(start, stop - 1)

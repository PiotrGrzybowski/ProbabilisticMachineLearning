from abc import abstractmethod


class Concept:
    def __init__(self, start, stop, name):
        self.extension = self.generate_extension(start, stop)
        self.name = name

    @abstractmethod
    def generate_extension(self, start, stop):
        pass

    def satisfy_concept(self, numbers):
        return set(numbers).issubset(self.extension)

    @property
    def size(self):
        return len(self.extension)


class OddNumbersConcept(Concept):
    def generate_extension(self, start, stop):
        if start % 2 == 0:
            start += 1
        return set(range(start, stop + 1, 2))


class EvenNumbersConcept(Concept):
    def generate_extension(self, start, stop):
        if start % 2 == 1:
            start += 1
        return set(range(start, stop + 1, 2))


class ArithmeticSequencesConcept(Concept):
    def generate_extension(self, start, stop):
        return set(range(start, stop + 1, start))


def generate_concepts(start, stop):
    return [OddNumbersConcept(start, stop, 'Odd Numbers'), EvenNumbersConcept(start, stop, 'Even Numbers')] + \
           [ArithmeticSequencesConcept(i, stop, "Sequence {}".format(i)) for i in range(start, stop)]


if __name__ == "__main__":
    pass


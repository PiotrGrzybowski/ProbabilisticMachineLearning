import unittest

from Lab4.concept import OddNumbersConcept, EvenNumbersConcept, ArithmeticSequencesConcept


class TestOddNumbersConcept(unittest.TestCase):
    def setUp(self):
        self.concept = OddNumbersConcept(1, 100, 'Odd Numbers')

    def test_odd_number_in_scope_satisfies_concept(self):
        self.assertTrue(self.concept.satisfy_concept([1]))
        self.assertTrue(self.concept.satisfy_concept([51]))
        self.assertTrue(self.concept.satisfy_concept([99]))

    def test_list_of_odd_numbers_in_scope_satisfies_concept(self):
        self.assertTrue(self.concept.satisfy_concept([1, 59, 99]))
        self.assertTrue(self.concept.satisfy_concept([1, 1, 1, 1, 7, 7, 7, 7, 99, 99, 99]))
        self.assertTrue(self.concept.satisfy_concept([99, 97, 7]))

    def test_odd_number_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([101]))
        self.assertFalse(self.concept.satisfy_concept([103]))
        self.assertFalse(self.concept.satisfy_concept([0]))

    def test_list_of_odd_numbers_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([101, 1, 59, 99]))
        self.assertFalse(self.concept.satisfy_concept([101, 1, 1, 1, 1, 7, 7, 7, 7, 99, 99, 99]))
        self.assertFalse(self.concept.satisfy_concept([101, 99, 97, 7]))

    def test_even_number_in_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([2]))
        self.assertFalse(self.concept.satisfy_concept([100]))
        self.assertFalse(self.concept.satisfy_concept([50]))

    def test_list_with_even_number_in_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([3, 2, 4, 48]))
        self.assertFalse(self.concept.satisfy_concept([48, 4, 2, 8, 48]))
        self.assertFalse(self.concept.satisfy_concept([100, 4, 2, 8, 48]))

    def test_even_number_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([202]))
        self.assertFalse(self.concept.satisfy_concept([402]))
        self.assertFalse(self.concept.satisfy_concept([0]))

    def test_list_of_even_numbers_with_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([2, 0, 202]))
        self.assertFalse(self.concept.satisfy_concept([2, 0, 402]))
        self.assertFalse(self.concept.satisfy_concept([2, 0, 602]))


class TestEvenNumbersConcept(unittest.TestCase):
    def setUp(self):
        self.concept = EvenNumbersConcept(1, 100, 'Even Numbers')

    def test_even_number_in_scope_satisfies_concept(self):
        self.assertTrue(self.concept.satisfy_concept([2]))
        self.assertTrue(self.concept.satisfy_concept([100]))
        self.assertTrue(self.concept.satisfy_concept([50]))

    def test_list_with_even_number_in_scope_satisfies_concept(self):
        self.assertTrue(self.concept.satisfy_concept([6, 2, 4, 48]))
        self.assertTrue(self.concept.satisfy_concept([48, 4, 2, 8, 48]))
        self.assertTrue(self.concept.satisfy_concept([100, 4, 2, 8, 48]))

    def test_even_number_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([202]))
        self.assertFalse(self.concept.satisfy_concept([402]))
        self.assertFalse(self.concept.satisfy_concept([0]))

    def test_list_of_even_numbers_with_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([2, 0, 202]))
        self.assertFalse(self.concept.satisfy_concept([2, 0, 402]))
        self.assertFalse(self.concept.satisfy_concept([2, 0, 602]))

    def test_odd_number_in_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([1]))
        self.assertFalse(self.concept.satisfy_concept([51]))
        self.assertFalse(self.concept.satisfy_concept([99]))

    def test_list_of_odd_numbers_in_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([1, 59, 99]))
        self.assertFalse(self.concept.satisfy_concept([1, 1, 1, 1, 7, 7, 7, 7, 99, 99, 99]))
        self.assertFalse(self.concept.satisfy_concept([99, 97, 7]))

    def test_odd_number_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([101]))
        self.assertFalse(self.concept.satisfy_concept([103]))
        self.assertFalse(self.concept.satisfy_concept([0]))

    def test_list_of_odd_numbers_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([101, 1, 59, 99]))
        self.assertFalse(self.concept.satisfy_concept([101, 1, 1, 1, 1, 7, 7, 7, 7, 99, 99, 99]))
        self.assertFalse(self.concept.satisfy_concept([101, 99, 97, 7]))


class TestArithmeticSequencesConceptDiff2(unittest.TestCase):
    def setUp(self):
        self.concept = ArithmeticSequencesConcept(2, 100, 'Sequence 2')

    def test_arithmetic_sequence_in_scope_satisfies_concept(self):
        self.assertTrue(self.concept.satisfy_concept([2, 4]))
        self.assertTrue(self.concept.satisfy_concept([48, 96]))
        self.assertTrue(self.concept.satisfy_concept([96, 98, 100]))
        self.assertTrue(self.concept.satisfy_concept([20, 40, 60, 80]))

    def test_arithmetic_sequence_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([96, 98, 100, 102]))
        self.assertFalse(self.concept.satisfy_concept([0, 1, 2, 3]))
        self.assertFalse(self.concept.satisfy_concept([0]))

    def test_random_sequence_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([1, 96, 98, 6, 100, 102]))
        self.assertFalse(self.concept.satisfy_concept([0, 1, 2, 3, 99]))


class TestArithmeticSequencesConceptDiff20(unittest.TestCase):
    def setUp(self):
        self.concept = ArithmeticSequencesConcept(20, 100, 'Sequence 20')

    def test_arithmetic_sequence_in_scope_satisfies_concept(self):
        self.assertTrue(self.concept.satisfy_concept([20, 40]))
        self.assertTrue(self.concept.satisfy_concept([40, 60, 60, 80, 100]))
        self.assertTrue(self.concept.satisfy_concept([20, 80, 100]))
        self.assertTrue(self.concept.satisfy_concept([20, 100]))

    def test_arithmetic_sequence_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([96, 98, 100, 102]))
        self.assertFalse(self.concept.satisfy_concept([0, 1, 2, 3]))
        self.assertFalse(self.concept.satisfy_concept([0]))

    def test_random_sequence_out_of_scope_satisfies_concept(self):
        self.assertFalse(self.concept.satisfy_concept([1, 96, 98, 6, 100, 102]))
        self.assertFalse(self.concept.satisfy_concept([0, 1, 2, 3, 99]))


if __name__ == "__main__":
    unittest.main()

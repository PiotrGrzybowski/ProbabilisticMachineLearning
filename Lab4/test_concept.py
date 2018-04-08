import unittest
from functools import partial

from Lab4.concept import is_even, is_odd, is_divisible_by_n, does_data_satisfy_concept, concept_power


class TestConcept(unittest.TestCase):
    def test_is_even_number(self):
        self.assertTrue(is_even(10))
        self.assertTrue(is_even(8))
        self.assertTrue(is_even(0))

        self.assertFalse(is_even(1))
        self.assertFalse(is_even(3))
        self.assertFalse(is_even(99))

    def test_is_odd_number(self):
        self.assertFalse(is_odd(10))
        self.assertFalse(is_odd(8))
        self.assertFalse(is_odd(0))

        self.assertTrue(is_odd(1))
        self.assertTrue(is_odd(3))
        self.assertTrue(is_odd(99))

    def test_is_divisible_by_4(self):
        self.assertTrue(is_divisible_by_n(4, 4))
        self.assertTrue(is_divisible_by_n(8, 4))
        self.assertTrue(is_divisible_by_n(16, 4))

        self.assertFalse(is_divisible_by_n(1, 4))
        self.assertFalse(is_divisible_by_n(2, 4))
        self.assertFalse(is_divisible_by_n(5, 4))

    def test_does_data_satisfy_concept(self):
        self.assertTrue(does_data_satisfy_concept([2, 4, 6, 8], is_even))
        self.assertFalse(does_data_satisfy_concept([2, 4, 6, 8, 9], is_even))

        self.assertTrue(does_data_satisfy_concept([1, 3, 9], is_odd))
        self.assertFalse(does_data_satisfy_concept([1, 3, 9, 8], is_odd))

        self.assertTrue(does_data_satisfy_concept([3, 9, 12], partial(is_divisible_by_n, n=3)))
        self.assertFalse(does_data_satisfy_concept([1, 3, 9, 12], partial(is_divisible_by_n, n=3)))

    def test_concept_power(self):
        self.assertEquals(concept_power(is_even), 50)
        self.assertEquals(concept_power(is_odd), 50)
        self.assertEquals(concept_power(partial(is_divisible_by_n, n=20)), 5)


if __name__ == "__main__":
    unittest.main()

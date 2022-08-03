import unittest

from src.compare import compare

class TestCompare(unittest.TestCase):

    def test_compare_3_1_returns_3_is_greater_than_1(self):
        self.assertEqual("3 is greater than 1", compare(3, 1))
    
    def test_compare_14_20_returns_5_is_less_than_10(self):
        self.assertEqual("14 is less than 20", compare(14, 20))

    def test_compare_15_15_returns_numbers_are_the_same(self):
        self.assertEqual("15 is equal to 15", compare(15, 15))
    
    def test_compare_40_19_returns_40_is_greater_than_19(self):
        self.assertEqual("40 is greater than 19", compare(40, 19))

    def test_compare_50_50_returns_numbers_are_the_same(self):
        self.assertEqual("50 is equal to 50", compare(50, 50))

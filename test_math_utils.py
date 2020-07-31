import unittest
import math_utils

class TestMain(unittest.TestCase):


    def setUp(self) -> None:
        pass

    def test_add(self):
        self.assertEqual(9, math_utils.add(4, 5))

    def test_subtract(self):
        self.assertEqual(-1, math_utils.subtract(4, 5))

    def test_multiply(self):
        self.assertEqual(20, math_utils.multiply(4, 5))

    def test_divide(self):
        self.assertEqual(0.8, math_utils.divide(4, 5))


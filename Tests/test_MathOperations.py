import unittest

from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction


class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1,2))

    def test_calculator_subtraction(self):
        self.assertEqual(-1, Subtraction.difference(1,2))


if __name__ == '__main__':
    unittest.main()

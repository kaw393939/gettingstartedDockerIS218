import unittest


class MyTestCase(unittest.TestCase):

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)


if __name__ == '__main__':
    unittest.main()

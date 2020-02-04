from MathOperations.addition import Addition
from MathOperations.subtraction import Subtraction


class Calculator:

    def __init__(self):
        pass

    def Sum(self, a, b):
        return Addition.sum(a, b);

    def Difference(self, a, b):
        return Subtraction.difference(a, b)

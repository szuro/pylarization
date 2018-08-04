import unittest
import math
from math import sqrt
from pylarization.vectors import JonesVector
from tests import DummyVector


class JonesVectorValues(DummyVector.DummyVectorValues):
    def setUp(self):
        self.linear_horizontal = JonesVector(1, 0)
        self.linear_vertical = JonesVector(0, 1)
        a = sqrt(2) * 0.5
        self.linear_plus45 = JonesVector(a, a)
        self.linear_minus45 = JonesVector(a, -a)
        self.elliptic = JonesVector(0.89 * 0.5, 0.89 * 1j)


if __name__ == '__main__':
    unittest.main()

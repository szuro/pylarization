import unittest
from math import sqrt
import math
from pylarization.vectors import StokesVector
from tests import DummyVector


class StokesVectorValues(DummyVector.DummyVectorValues):
    def setUp(self):
        self.linear_horizontal = StokesVector(1, 1, 0, 0)
        self.linear_vertical = StokesVector(1, -1, 0, 0)
        self.linear_plus45 = StokesVector(1, 0, 1, 0)
        self.linear_minus45 = StokesVector(1, 0, -1, 0)
        self.elliptic = StokesVector(1.2371, -0.3471, 0, 0.7921)


if __name__ == '__main__':
    unittest.main()

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


class StokesVectorNormalization(DummyVector.DummyVectorNormalization):
    def setUp(self):
        self.linear_horizontal = StokesVector(1, 1, 0, 0)
        self.linear_vertical = StokesVector(1, -1, 0, 0)
        self.linear_plus45 = StokesVector(1, 0, 1, 0)
        self.linear_minus45 = StokesVector(1, 0, -1, 0)
        self.elliptic = StokesVector(1.2371, -0.3471, 0, 0.7921)

        self.linear_horizontal_normalized = StokesVector(1, 1, 0, 0)
        self.linear_horizontal_normalized.normalize()

        self.linear_vertical_normalized = StokesVector(1, -1, 0, 0)
        self.linear_vertical_normalized.normalize()

        self.linear_plus45_normalized = StokesVector(1, 0, 1, 0)
        self.linear_plus45_normalized.normalize()

        self.linear_minus45_normalized = StokesVector(1, 0, -1, 0)
        self.linear_minus45_normalized.normalize()

        self.elliptic_normalized = StokesVector(1.2371, -0.3471, 0, 0.7921)
        self.elliptic_normalized.normalize()


if __name__ == '__main__':
    unittest.main()

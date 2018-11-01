import unittest
from numpy import sqrt
from pylarization.vectors import StokesVector
from tests import DummyVector


class TestStokesVectorValues(DummyVector.TestDummyVectorValues):
    def setUp(self):
        self.linear_horizontal = StokesVector(1, 1, 0, 0)
        self.linear_vertical = StokesVector(1, -1, 0, 0)
        self.linear_plus45 = StokesVector(1, 0, 1, 0)
        self.linear_minus45 = StokesVector(1, 0, -1, 0)
        self.elliptic = StokesVector(0.990125, -0.594075, 0, 0.7921)
        self.circular_left_handed = StokesVector(1, 0, 0, -1)
        self.circular_right_handed = StokesVector(1, 0, 0, 1)


class TestStokesVectorNormalization(DummyVector.TestDummyVectorNormalization):
    def setUp(self):
        self.linear_horizontal = StokesVector(1, 1, 0, 0)
        self.linear_vertical = StokesVector(1, -1, 0, 0)
        self.linear_plus45 = StokesVector(1, 0, 1, 0)
        self.linear_minus45 = StokesVector(1, 0, -1, 0)
        self.elliptic = StokesVector(1.2371, -0.3471, 0, 0.7921)
        self.circular_left_handed = StokesVector(1, 0, 0, -1)
        self.circular_right_handed = StokesVector(1, 0, 0, 1)

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

        self.circular_left_handed_normalized = StokesVector(1, 0, 0, -1)
        self.circular_left_handed_normalized.normalize()

        self.circular_right_handed_normalized = StokesVector(1, 0, 0, 1)
        self.circular_right_handed_normalized.normalize()


class TestStokesVectorAddition(unittest.TestCase):
    def setUp(self):
        self.linear_horizontal = StokesVector(1, 1, 0, 0)
        self.linear_vertical = StokesVector(1, -1, 0, 0)

    def test_addition(self):
        expected_sum = StokesVector(2, 0, 0, 0)
        vector_sum = self.linear_horizontal + self.linear_vertical
        self.assertEqual(expected_sum.vector.all(), vector_sum.vector.all())


if __name__ == '__main__':
    unittest.main()

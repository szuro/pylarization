import unittest
import numpy as np
from numpy import pi, array_equal
from pylarization.matrices import JonesMatrix
from pylarization.elements import JonesMatrixOpticalElements


class TestJonesMatrix(unittest.TestCase):
    def setUp(self):
        self.linear_horizontal = JonesMatrix()
        self.linear_vertical = JonesMatrix(angle=pi/2)

    def test_init(self):
        self.assertTrue(np.allclose(
            self.linear_horizontal.matrix,
            JonesMatrixOpticalElements.HORIZONTAL_LINEAR_POLARIZER.value.matrix
            ))
        print(self.linear_vertical.matrix)
        self.assertTrue(np.allclose(
            self.linear_vertical.matrix,
            JonesMatrixOpticalElements.VERTICAL_LINEAR_POLARIZER.value.matrix
            ))


class TestJonesMatrixClassmethods(unittest.TestCase):
    def test_device_factor(self):
        self.assertAlmostEqual(JonesMatrix.device_factor(), 0.0)
        self.assertAlmostEqual(JonesMatrix.device_factor(1, pi/2), 1j)
        self.assertAlmostEqual(JonesMatrix.device_factor(1, pi), -1)

    def test_from_matrix(self):
        self.assertTrue(array_equal(
                JonesMatrix.from_matrix([[1., 0.],
                                         [0., 0.]]
                                        ).matrix,
                np.array([[1., 0.],
                          [0., 0.]],
                         dtype=complex)
                         )
                        )

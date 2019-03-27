import unittest
import numpy as np
from numpy import pi, array_equal
from pylarization.vectors import JonesVector
from pylarization.polarizations import JonesVectorState
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


class TestJonesMatrixCalculations(unittest.TestCase):
    def setUp(self):
        self.vector = JonesVector(1, 1)
        self.matrix = JonesMatrix.from_matrix([[1, 0],
                                               [0, -1j]])

    def test_vector_multiplication(self):
        result = self.matrix @ self.vector
        self.assertIsInstance(result, JonesVector)
        self.assertTrue(np.allclose(result.vector, JonesVector(1, -1j).vector))

    def test_vector_multiplication_with_wrong_order(self):
        with self.assertRaises(ValueError):
            self.vector @ self.matrix

    def test_matrix_multiplication(self):
        result = self.matrix @ self.matrix
        self.assertIsInstance(result, JonesMatrix)
        self.assertTrue(np.allclose(result.matrix, np.array([[1, 0],
                                                             [0, -1]])))

    def test_cascade_multiplication(self):
        result = self.matrix @ self.matrix @ self.vector
        self.assertIsInstance(result, JonesVector)
        self.assertTrue(np.allclose(result.vector, JonesVector(1, -1).vector))

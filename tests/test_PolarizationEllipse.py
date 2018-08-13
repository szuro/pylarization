import unittest
from math import sqrt, pi
import math
from pylarization.ellipse import PolarizationEllipse
from tests import DummyVector


class PolarizationEllipseValues(DummyVector.DummyVectorValues):
    def setUp(self):
        self.linear_horizontal = PolarizationEllipse(1.0, 0.0, 0.0)
        self.linear_vertical = PolarizationEllipse(0.0, 1.0, 0.0)
        self.linear_plus45 = PolarizationEllipse(0.7071068, 0.7071068, 0.0)
        self.linear_minus45 = PolarizationEllipse(0.7071068, -0.7071068, 0.0)
        self.elliptic = PolarizationEllipse(0.445, 0.89, pi/2)
        self.circular_left_handed = PolarizationEllipse(0.7071068, 0.7071068, -pi/2)
        self.circular_right_handed = PolarizationEllipse(0.7071068, 0.7071068, pi/2)


if __name__ == '__main__':
    unittest.main()

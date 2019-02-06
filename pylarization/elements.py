"""
Enums for popular optical elements.
"""

from enum import Enum
from math import sqrt, pi
from pylarization.matrices import JonesMatrix


class JonesMatrixOpticalElements(Enum):
    HORIZONTAL_LINEAR_POLARIZER = JonesMatrix.from_matrix([[1.0, 0.0],
                                                           [0.0, 0.0]])
    VERTICAL_LINEAR_POLARIZER = JonesMatrix.from_matrix([[0.0, 0.0],
                                                         [0.0, 1.0]])

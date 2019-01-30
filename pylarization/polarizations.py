"""
Enums for edge cases of polarizarion.
NOTE!
Enums presented here confirm to the IEEE convention of left-/righ-handedness.
"""

from enum import Enum
from math import sqrt, pi
from pylarization.ellipse import PolarizationEllipse
from pylarization.vectors import JonesVector, StokesVector


class JonesVectorState(Enum):
    LINEAR_HORIZONTAL = JonesVector(1, 0)
    LINEAR_VERTICAL = JonesVector(0, 1)
    LINEAR_DIAGONAL = JonesVector(sqrt(2) * 0.5, sqrt(2) * 0.5)
    LINEAR_ANTIDIAGONAL = JonesVector(sqrt(2) * 0.5, -sqrt(2) * 0.5)
    CIRCULAR_LEFT_HANDED = JonesVector(sqrt(2) * 0.5, sqrt(2) * 0.5 * 1j)
    CIRCULAR_RIGHT_HANDED = JonesVector(sqrt(2) * 0.5, -sqrt(2) * 0.5 * 1j)


class StokesVectorState(Enum):
    LINEAR_HORIZONTAL = StokesVector(1, 1, 0, 0)
    LINEAR_VERTICAL = StokesVector(1, -1, 0, 0)
    LINEAR_DIAGONAL = StokesVector(1, 0, 1, 0)
    LINEAR_ANTIDIAGONAL = StokesVector(1, 0, -1, 0)
    CIRCULAR_LEFT_HANDED = StokesVector(1, 0, 0, 1)
    CIRCULAR_RIGHT_HANDED = StokesVector(1, 0, 0, -1)


class PolarizationEllipseState(Enum):
    LINEAR_HORIZONTAL = PolarizationEllipse(1.0, 0.0, 0.0)
    LINEAR_VERTICAL = PolarizationEllipse(0.0, 1.0, 0.0)
    LINEAR_DIAGONAL = PolarizationEllipse(sqrt(2) * 0.5, sqrt(2) * 0.5, 0.0)
    LINEAR_ANTIDIAGONAL = PolarizationEllipse(sqrt(2) * 0.5, sqrt(2) * 0.5, pi)
    CIRCULAR_LEFT_HANDED = PolarizationEllipse(sqrt(2) * 0.5, sqrt(2) * 0.5, pi/2)
    CIRCULAR_RIGHT_HANDED = PolarizationEllipse(sqrt(2) * 0.5, sqrt(2) * 0.5, -pi/2)
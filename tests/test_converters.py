import unittest
from pylarization.vectors import JonesVector
from pylarization.polarizations import JonesVectorState
from pylarization.vectors import StokesVector
from pylarization.polarizations import StokesVectorState
from pylarization.converters import stokes_to_jones, jones_to_stokes


class TestJonesMatrix(unittest.TestCase):
    def test_stokes_to_jones(self):
        jones = stokes_to_jones(StokesVectorState.LINEAR_HORIZONTAL.value)
        self.assertAlmostEqual(jones.E0x, JonesVectorState.LINEAR_HORIZONTAL.value.E0x)
        self.assertAlmostEqual(jones.E0y, JonesVectorState.LINEAR_HORIZONTAL.value.E0y)
        self.assertAlmostEqual(jones.phase, JonesVectorState.LINEAR_HORIZONTAL.value.phase)

    def test_jones_to_stokes(self):
        stokes = jones_to_stokes(JonesVectorState.LINEAR_HORIZONTAL.value)
        self.assertAlmostEqual(stokes.E0x, StokesVectorState.LINEAR_HORIZONTAL.value.E0x)
        self.assertAlmostEqual(stokes.E0y, StokesVectorState.LINEAR_HORIZONTAL.value.E0y)
        self.assertAlmostEqual(stokes.phase, StokesVectorState.LINEAR_HORIZONTAL.value.phase)

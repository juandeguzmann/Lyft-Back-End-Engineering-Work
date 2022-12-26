from tires.carrigan import CarriganTires
from tires.octoprime import OctoprimeTires
import unittest

class TestCarriganTires(unittest.TestCase):
    def test_if_should_be_serviced(self):
        tires = [0.1, 0.4, 0.9, 0.95]
        ct = CarriganTires(tires)
        self.assertTrue(ct.needs_service())

    def test_if_should_not_be_serviced(self):
        tires = [0.1, 0.4, 0.3, 0.55]
        ct = CarriganTires(tires)
        self.assertFalse(ct.needs_service())

class TestOctoprimeTires(unittest.TestCase):
    def test_if_should_be_serviced(self):
        tires = [0.8, 0.9, 0.9, 0.95]
        ot = OctoprimeTires(tires)
        self.assertTrue(ot.needs_service())

    def test_if_should_not_be_serviced(self):
        tires = [0.1, 0.05, 0.3, 0.6]
        ot = OctoprimeTires(tires)
        self.assertFalse(ot.needs_service())

unittest.main()
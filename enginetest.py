import unittest
import datetime as dt
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapuletEngine(unittest.TestCase):
    def test_if_engine_should_be_serviced(self):
        current_mileage = 30002
        last_service_mileage = 1
        ce = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(ce.needs_service())

    def test_if_engine_should_not_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 1
        ce = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(ce.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_if_engine_should_be_serviced(self):
        warning_light_on = True
        se = SternmanEngine(warning_light_on)
        self.assertTrue(se.needs_service())

    def test_if_engine_should_not_be_serviced(self):
        warning_light_on = False
        se = SternmanEngine(warning_light_on)
        self.assertFalse(se.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_if_engine_should_be_serviced(self):
        current_mileage = 60002
        last_service_mileage = 1
        we = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertTrue(we.needs_service())

    def test_if_engine_should_not_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 1
        we = WilloughbyEngine(last_service_mileage, current_mileage)
        self.assertFalse(we.needs_service())




unittest.main()
import unittest
import datetime as dt
from battery.spindler import SpindlerBattery
from battery.nubbin import NubbinBattery

class SpindlerBatteryTest(unittest.TestCase):
    def test_if_battery_should_be_serviced(self):
        today = dt.datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        sb = SpindlerBattery(last_service_date, today)
        self.assertTrue(sb.needs_service())
    
    def test_if_battery_should_not_be_serviced(self):
        today = dt.datetime.today()
        last_service_date = today.replace(year=today.year - 1)
        sb = SpindlerBattery(last_service_date, today)
        self.assertFalse(sb.needs_service())
    
class NubbinBatteryTest(unittest.TestCase):
    def test_if_battery_should_be_serviced(self):
        today = dt.datetime.today()
        last_service_date = today.replace(year=today.year - 4)
        nb = NubbinBattery(last_service_date, today)
        self.assertTrue(nb.needs_service())

    def test_if_battery_should_not_be_serviced(self):
        today = dt.datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        nb = NubbinBattery(last_service_date, today)
        self.assertFalse(nb.needs_service())


unittest.main()

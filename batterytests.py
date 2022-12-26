from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
import datetime as dt
import unittest

class NubbinBatteryTest(unittest.TestCase):
    def test_if_battery_should_be_serviced(self):
        today = dt.datetime.today()
        last_service_date = today.replace(year=today.year - 4)
        nb = NubbinBattery(today, last_service_date)
        self.assertTrue(nb.needs_service())

    def test_if_battery_should_not_be_serviced(self):
        today = dt.datetime.today()
        last_service_date = today.replace(year=today.year - 2)
        nb = NubbinBattery(today, last_service_date)
        self.assertFalse(nb.needs_service())

class SpindlerBatteryTest(unittest.TestCase):
    def test_if_battery_should_be_serviced(self):
        today = dt.datetime.today()
        last_service_date = today.replace(year=today.year - 2)
        sb = SpindlerBattery(today, last_service_date)
        self.assertTrue(sb.needs_service())

    def test_if_battery_should_not_be_serviced(self):
        today = dt.datetime.today()
        last_service_date = today.replace(year=today.year - 1)
        sb = SpindlerBattery(today, last_service_date)
        self.assertFalse(sb.needs_service())

unittest.main()

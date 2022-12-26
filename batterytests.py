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

unittest.main()

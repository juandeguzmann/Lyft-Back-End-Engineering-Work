from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
import datetime as dt
import unittest

class NubbinBattery(unittest.TestCase):
    def test_if_should_be_serviced(self):
        today = dt.datetime.today()
        last_service_date = today.replace(year=today.year - 3)
        nb = NubbinBattery(last_service_date, today)

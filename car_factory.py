from battery.nubbin import NubbinBattery
from battery.spindler import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from engine.engine import Engine
from battery.battery import Battery
from car import Car

import datetime as dt

class CarFactory():

    @staticmethod
    def create_calliope(current_date: dt.date, last_service_date: dt.date, current_mileage: int, last_service_mileage: int):
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(spindler_battery, capulet_engine)
    
    @staticmethod
    def create_glissade(current_date: dt.date, last_service_date: dt.date, current_mileage: int, last_service_mileage: int):
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(spindler_battery, willoughby_engine)
    
    @staticmethod
    def create_palindrome(current_date: dt.date, last_service_date: dt.date, warning_light_on: bool):
        sternman_engine = SternmanEngine(warning_light_on)
        spindler_battery = SpindlerBattery(last_service_date, current_date)
        return Car(spindler_battery, sternman_engine)
    
    @staticmethod
    def create_rorschach(current_date: dt.date, last_service_date: dt.date, current_mileage: int, last_service_mileage: int):
        willoughby_engine = WilloughbyEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Car(nubbin_battery, willoughby_engine)

    @staticmethod
    def create_thovex(current_date: dt.date, last_service_date: dt.date, current_mileage: int, last_service_mileage: int):
        capulet_engine = CapuletEngine(last_service_mileage, current_mileage)
        nubbin_battery = NubbinBattery(last_service_date, current_date)
        return Car(nubbin_battery, capulet_engine)


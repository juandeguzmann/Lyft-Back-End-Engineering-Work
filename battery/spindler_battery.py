from abc import ABC
from car import Car

import datetime as dt


class SpindlerBattery(Car, ABC):
    def __init__(self, last_service_date: dt, current_date: dt):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def battery_should_be_serviced(self):
        time_difference = self.__current_date - self.__last_service_date
        return (time_difference//365) >= 2
from battery.battery import Battery

import datetime as dt


class NubbinBattery(Battery):
    def __init__(self, current_date: dt, last_service_date: dt):
        self.__current_date = current_date
        self.__last_service_date = last_service_date
        
    def needs_service(self):
        time_difference = self.__current_date - self.__last_service_date
        return (time_difference.days//365) >= 4
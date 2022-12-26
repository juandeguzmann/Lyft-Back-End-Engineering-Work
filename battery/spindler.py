from battery.battery import Battery
import datetime as dt

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: dt, current_date: dt):
        self.__last_service_date = last_service_date
        self.__current_date = current_date
    
    def needs_service(self):
        time_difference = self.__current_date - self.__last_service_date
        return (time_difference.days//365) >= 3


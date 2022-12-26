from engine.engine import Engine
from battery.battery import Battery
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, battery: Battery, engine: Engine):
        self.__battery = battery
        self.__engine = engine
    
    def needs_service(self):
        return self.__engine.needs_service() or self.__battery.needs_service()
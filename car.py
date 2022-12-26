from engine.engine import Engine
from battery.battery import Battery
from tires.tires import Tires
from serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, battery: Battery, engine: Engine, tires: Tires):
        self.__engine = engine
        self.__battery = battery
        self.__tires = tires
    
    def needs_service(self):
        print(f"Engine: {self.__engine.needs_service()}.\nBattery: {self.__battery.needs_service()}\nTires: {self.__tires.needs_service()}")

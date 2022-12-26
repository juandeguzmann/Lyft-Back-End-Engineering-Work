from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, tires):
        self.__tires = tires
    
    def needs_service(self):
        dead_tires = 0
        for i in range(len(self.__tires)):
            if self.__tires[i] > 0.9 and self.__tires[i] < 1:
                dead_tires += 1
        if dead_tires >= 1:
            return True
        else:
            return False
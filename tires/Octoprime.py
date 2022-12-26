from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tires):
        self.__tires = tires
    
    def needs_service(self):
        dead_tires = 0
        for i in range(len(self.__tires)):
            dead_tires += self.__tires[i]
        if dead_tires >= 3:
            return True
        else:
            return False   
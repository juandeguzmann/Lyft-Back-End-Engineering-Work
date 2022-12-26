from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, tires):
        self.__tires = tires
    
    def needs_service(self):
        sum = 0
        for i in range(len(self.__tires)):
            sum += self.__tires[i]
        if sum >= 3:
            return True
        else:
            return False        
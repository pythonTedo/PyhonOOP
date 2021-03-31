#from skeleton.project.hardware.hardware import Hadware
from hardware.hardware import Hadware

class HeavyHardware(Hadware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, type="Heavy", capacity=capacity*2, memory=memory*0.75)



#from skeleton.project.hardware.hardware import Hadware
from hardware.hardware import Hadware

class PowerHardware(Hadware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, type="Power", capacity=capacity*0.25, memory=memory*0.75+memory)

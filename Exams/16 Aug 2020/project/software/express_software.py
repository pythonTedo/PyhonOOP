#from skeleton.project.software.software import Software
from software.software import Software

class ExpressSoftware(Software):
    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, type="Express", capacity_consumption=capacity_consumption,
                         memory_consumption=memory_consumption*2)


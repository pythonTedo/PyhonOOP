#from skeleton.project.software.software import Software
from software.software import Software

class Hadware:
    def __init__(self, name, type, capacity, memory):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []
        self.total_capacity = capacity
        self.total_memory = memory

    def install(self, software: Software):
        if self.memory >= software.memory_consumption and self.capacity >= software.capacity_consumption:
            self.software_components.append(software)
            self.capacity -= software.capacity_consumption
            self.memory -= software.memory_consumption
        else:
            raise Exception("Software cannot be installed")

    def unistall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)
            self.capacity += software.capacity_consumption
            self.memory += software.memory_consumption

    def __repr__(self):
        return f"{self.name} --> Total capacity: {self.total_capacity} --> {self.capacity}\n" \
               f"Total mem: {self.total_memory} --> {self.memory}"
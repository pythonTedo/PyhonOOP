from Inheritance.mix_it_06.technology.technology import Technology

class Laptop(Technology):

    def __init__(self, memory: float, memory_taken: float):
        super().__init__(memory, memory_taken)

    def install_software(self, software, software_memory):
        try:
            self.get_capacity(self.memory, self.memory_taken + software_memory)
            self.memory -= software_memory
            self.memory_taken += software_memory
            return self.memory

        except Exception as ex:
            return f"You don't have enough space for {software}"

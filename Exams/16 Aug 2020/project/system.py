# from skeleton.project.hardware.hardware import Hadware
# from skeleton.project.hardware.power_hardware import PowerHardware
# from skeleton.project.hardware.heavy_hardware import HeavyHardware
# from skeleton.project.software.express_software import ExpressSoftware
# from skeleton.project.software.light_software import LightSoftware
# from software.software import Software

from hardware.hardware import Hadware
from hardware.power_hardware import PowerHardware
from hardware.heavy_hardware import HeavyHardware
from software.express_software import ExpressSoftware
from software.light_software import LightSoftware
from software.software import Software

class System:
    _hardware = []
    _software = []


    @staticmethod
    def register_power_hardware(name, memory, capacity):
        power = PowerHardware(name, memory, capacity)
        System._hardware.append(power)

    @staticmethod
    def register_heavy_hardware(name, memory, capacity):
        heavy = HeavyHardware(name, memory, capacity)
        System._hardware.append(heavy)


    @staticmethod
    def register_express_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            current_hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except:
            raise Exception("Hardware does not exist")

        express = ExpressSoftware(name, capacity_consumption, memory_consumption)
        try:
            Hadware.install(current_hardware, express)
            System._software.append(express)
        except Exception as ex:
            return "Software cannot be installed"


    @staticmethod
    def register_light_software(hardware_name, name, capacity_consumption, memory_consumption):
        try:
            current_hardware = [h for h in System._hardware if h.name == hardware_name][0]
        except:
            raise Exception("Hardware does not exist")

        light = LightSoftware(name, capacity_consumption, memory_consumption)
        try:
            current_hardware.install(light)
            System._software.append(light)
        except Exception as ex:
            return "Software cannot be installed"


    @staticmethod
    def release_software_component(hardware_name, software_name):
        try:
            curr_hardware = [h for h in System._hardware if h.name == hardware_name][0]
            curr_software = [s for s in System._software if s.name == software_name][0]
            if curr_software and curr_hardware:
                Hadware.unistall(curr_hardware, curr_software)
        except:
            raise Exception("Some of the components do not exist")

    @staticmethod
    def analyze():

        used_operation_mem = sum([s.memory_consumption for s in System._software])
        total_operation_mem = sum([h.total_memory for h in System._hardware])

        used_capacity = sum([s.capacity_consumption for s in System._software])
        total_capacity = sum([h.total_capacity for h in System._hardware])

        result = "System Analysis\n"
        result += f"Hardware Components: {len(System._hardware)}\n"
        result += f"Software Components: {len(System._software)}\n"
        result += f"Total Operational Memory: {used_operation_mem} / {total_operation_mem}\n"
        result += f"Total Capacity Taken: {used_capacity} / {total_capacity}"

        return result

    @staticmethod
    def system_split():
        result = ""
        counter = 0

        for h in System._hardware:
            counter += 1

            soft_components = ""
            if len(h.software_components) > 0:
                soft_components += ", ".join([s.name for s in h.software_components])
            else:
                result += "None\n"

            result += f"Hardware Component - {h.name}\n" \
            f"Express Software Components: {len([s for s in h.software_components if s.__class__.__name__ == 'ExpressSoftware'])}\n" \
            f"Light Software Components: {len([s for s in h.software_components if s.__class__.__name__ == 'LightSoftware'])}\n" \
            f"Memory Usage: {sum([s.memory_consumption for s in h.software_components])} / {h.total_memory}\n" \
            f"Capacity Usage: {sum([s.capacity_consumption for s in h.software_components])} / {h.total_capacity}\n" \
            f"Type: {h.type}\n"

            if counter == len(h.software_components):
                result += f"Software Components: {soft_components}"
            else:
                result += f"Software Components: {soft_components}\n"

        return result


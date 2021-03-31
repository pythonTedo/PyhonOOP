from unittest import TestCase

from software.software import Software
from hardware.hardware import Hadware

class TestHardware(TestCase):
    def setUp(self):
        self.hardware = Hadware("SSD", "Heavy", 200, 200)

    def test_hardware__init__expect_to_initialized(self):
        self.assertEqual("SSD", self.hardware.name)
        self.assertEqual("Heavy", self.hardware.type)
        self.assertEqual(200, self.hardware.capacity)
        self.assertEqual(200, self.hardware.memory)
        self.assertEqual([], self.hardware.software_components)

    def test_hardware_install_when_capacity_less_than_consumption(self):
        software = Software("Linux", 'Light', 250, 10)
        with self.assertRaises(Exception) as context:
            self.hardware.install(software)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_hardware_install__when_enogh_memory_and_capacity(self):
        software = Software('Linux', 'Light', 10, 20)
        self.hardware.install(software)
        self.assertIn(software, self.hardware.software_components)

    def test_hardware_uninstall__when_software_in_software_components(self):
        software = Software('Linux', 'Light', 10, 20)
        self.hardware.install(software)
        self.hardware.unistall(software)
        self.assertEqual([], self.hardware.software_components)
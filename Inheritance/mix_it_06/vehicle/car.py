from Inheritance.mix_it_06.vehicle.vehicle import Vehicle
from Inheritance.mix_it_06.capacity_mixin import CapacityMixin

class Car(Vehicle):

    def __init__(self, available_seats: int, fuel_tank: int, fuel_consumption: float, fuel: float):
        super().__init__(available_seats)
        self.fuel_tank = fuel_tank
        self.fuel_consumption = fuel_consumption
        self._fuel = fuel

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, val):
        if val <= self.fuel_tank:
            self._fuel = val


    def drive(self, distance):
        fuel_needed = self.fuel_consumption * distance
        if fuel_needed <= self._fuel:
            self._fuel -= fuel_needed
            return "We've enjoyed the travel!"

    def refuel(self, litres):
        try:                     ## return type na func dali e string ili int
            self.get_capacity(self.fuel_tank, self._fuel + litres)
            self._fuel += litres
            return self._fuel
        except Exception as ex:
            return str(ex)            ## if its string

#
car = Car(4, 50, 5, 10)
#
car.fuel = 60
# print(car.refuel("nz brat"))
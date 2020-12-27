from Polymorphism.vechicle01.vehicle import Vehicle


class Car(Vehicle):

    FUEL_CONS_SUMMER = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + Car.FUEL_CONS_SUMMER) * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)


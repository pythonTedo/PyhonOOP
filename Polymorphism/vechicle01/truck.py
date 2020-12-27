from Polymorphism.vechicle01.vehicle import Vehicle

class Truck(Vehicle):

    FUEL_CONS_SUMMER = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        fuel_needed = (self.fuel_consumption + Truck.FUEL_CONS_SUMMER) * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel*0.95



truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

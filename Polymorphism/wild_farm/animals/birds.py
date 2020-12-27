from abc import abstractmethod
from Polymorphism.wild_farm.animals.animal import Animal, Bird
from Polymorphism.wild_farm.food import Meat


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if isinstance(food, Meat):
            self.weight += 0.25*food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluk"

    def feed(self, food):
        self.weight += 0.35*food.quantity
        self.food_eaten += food.quantity
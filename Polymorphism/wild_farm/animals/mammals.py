from abc import abstractmethod
from Polymorphism.wild_farm.animals.animal import Animal, Mammal
from Polymorphism.wild_farm.animals.birds import Owl, Hen
from Polymorphism.wild_farm.food import Meat, Food, Vegetable, Fruit


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if isinstance(food, Vegetable) or isinstance(food, Fruit):
            self.weight += 0.1*food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Wof"

    def feed(self, food: Food):
        if isinstance(food, Meat):
            self.weight += 0.40*food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if isinstance(food, Vegetable) or isinstance(food, Meat):
            self.weight += 0.3*food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Roar"

    def feed(self, food: Food):
        if isinstance(food, Meat):
            self.weight += 1*food.quantity
            self.food_eaten += food.quantity
        else:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)

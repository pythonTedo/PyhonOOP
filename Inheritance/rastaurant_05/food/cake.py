from Inheritance.rastaurant_05.food.dessert import Dessert

class Cake(Dessert):
        CAKE_GRAMS = 250
        CAKE_CALORIES = 100
        CAKE_PRICE = 5

        def __init__(self, name, price, grams, calories):
            super().__init__(
                name,
                self.__class__.CAKE_PRICE,
                self.__class__.CAKE_GRAMS,
                self.__class__.CAKE_CALORIES
            )

from Inheritance.rastaurant_05.beverage.hot_beverage import HotBeverage

class Coffee(HotBeverage):
    COFFEE_MILLILITRES = 50
    COFFEE_PRICE = 3.50

    def __init__(self, name, caffeine):
        super().__init__(
            name, self.__class__.COFFEE_PRICE, self.__class__.COFFEE_MILLILITRES)
        self._caffeine = caffeine

    @property
    def caffeine(self):
        return self._caffeine

    @caffeine.setter
    def caffeine(self, val):
        self._caffeine = val

c = Coffee('mono', 50)
print(c._caffeine)
b = HotBeverage('kakao', 3.50, 350)
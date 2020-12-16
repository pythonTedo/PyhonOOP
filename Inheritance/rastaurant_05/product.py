# _price - se vijda ot naslednicite
# __price - nqma da se vijda

class Product:

    def __init__(self, name, price):
        self._name = name       ##samo da pokajem da ne se promenq
        self._price = price

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @name.setter
    def name(self, val):
        self._name = val

    @price.setter
    def price(self, val):
        self._price = val



class Customer:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvd = []

    def __repr__(self):

        rep = ""
        for name in self.rented_dvd:
            if name == len(self.rented_dvd) - 1:
                rep += name
            else:
                rep += f"{name}, "
        return f"{self.id}: {self.name} of age {self.age} has {len(self.rented_dvd)} rented DVD's ({rep})"

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __add__(self, other):
        return Person(name=self.name, surname=other.surname)

    def __repr__(self):
        return self.name + " " + self.surname

# p1 = Person("Gosho", "Ivanov")
# p2 = Person("Tedor", "Petkov")
# p3 = p1+p2
#
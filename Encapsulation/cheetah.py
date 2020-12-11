class Cheetah:

    money_for_animal = 60

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs(self):
        return Cheetah.money_for_animal

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

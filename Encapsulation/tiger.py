class Tiger:
    money_for_animal = 45

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    @staticmethod
    def get_needs(self):
        return Tiger.money_for_animal

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Hero:

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def __repr__(self):
        return f"{self.name} of type {self.__class__.__name__} has level {self.level}"

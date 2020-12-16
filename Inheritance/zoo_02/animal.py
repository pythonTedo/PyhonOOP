class Animal:
    __name: str

    def __init__(self, name):
        self.__name = name

    @property           ## getter
    def name(self):
        return self.__name

    @name.setter        ## setter
    def name(self, val):
        self.__name = val
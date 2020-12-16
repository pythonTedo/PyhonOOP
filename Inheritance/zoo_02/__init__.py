from Inheritance.zoo_02 import *
from Inheritance.zoo_02.Bear import Bear
from Inheritance.zoo_02.Gorilla import Gorilla
from Inheritance.zoo_02.Lizard import Lizard
from Inheritance.zoo_02.animal import Animal
from Inheritance.zoo_02.mammal import Mammal
from Inheritance.zoo_02.reptile import Reptile
from Inheritance.zoo_02.snake import Snake

if __name__ == '__main__':

    animals = [
        Animal('animal'),
        Reptile('reptile'),
        Mammal('mammal'),
        Lizard('lizard'),
        Snake('snake'),
        Gorilla('gorilla'),
        Bear('bear')
    ]
    for a in animals:
        print(a.__dict__)
        print(a.name)
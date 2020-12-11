from Encapsulation.wild_zoo_01.lion import Lion
from Encapsulation.wild_zoo_01.tiger import Tiger
from Encapsulation.wild_zoo_01.cheetah import Cheetah
from Encapsulation.wild_zoo_01.keeper import Keeper
from Encapsulation.wild_zoo_01.caretaker import Caretaker
from Encapsulation.wild_zoo_01.vet import Vet
from Encapsulation.wild_zoo_01.zoo import Zoo

if __name__ == '__main__':

    zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
    animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
    prices = [200, 190, 204, 156, 211, 140]

# Workers creation
    workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
    for i in range(len(animals)):
        animal = animals[i]
        price = prices[i]
        print(zoo.add_animal(animal, price))

# Adding all workers
    for worker in workers:
        print(zoo.hire_worker(worker))

# Tending animals
    print(zoo.tend_animals())

# Paying keepers
    print(zoo.pay_workers())

# Fireing worker
    print(zoo.fire_worker("Adam"))

# Printing statuses
    print(zoo.animals_status())
    print(zoo.workers_status())
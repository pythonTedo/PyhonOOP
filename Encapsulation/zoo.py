from Encapsulation.wild_zoo_01.lion import Lion
from Encapsulation.wild_zoo_01.tiger import Tiger
from Encapsulation.wild_zoo_01.cheetah import Cheetah
from Encapsulation.wild_zoo_01.keeper import Keeper
from Encapsulation.wild_zoo_01.caretaker import Caretaker
from Encapsulation.wild_zoo_01.vet import Vet

class Zoo:

    def __init__(self, name, budget, animal_capacity, workers_capacity):

        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price

            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__animal_capacity >= len(self.animals) and self.__budget < price:
            return "Not enough budget"

        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)

            return f"{worker.name} the {worker.__class__.__name__} hired successfully"

        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        try:        ## ako imame 0 elementa shte grumne za tova pravim try
            curr_worker = [worker for worker in self.workers if worker.name == worker_name][0]
            self.workers.remove(curr_worker)
            return f"{worker_name} fired successfully"
        except IndentationError:  #### ne e imalo element v lista s index 0 (nqma nikakvi elementi)
            return f"There is no {worker_name}"

    def pay_workers(self):
        sum_sal = 0 # sum([worker.salary for worker in self.workers])
        for worker in self.workers:
            sum_sal += worker.salary
        if self.__budget >= sum_sal:
            self.__budget -= sum_sal
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_money = 0
        for animal in self.animals:
            tending_money += animal.get_needs(self)
        if self.__budget >= tending_money:
            self.__budget -= tending_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        lion = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tiger = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetah = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result = f"You have {len(self.animals)} animals:\n"
        result += f"----- {len(lion)} Lions:"
        result += "\n".join([l.__repr__() for l in lion]) + "\n"
        result += f"----- {len(tiger)} Tigers: \n"
        result += "\n".join([t.__repr__() for t in tiger]) + "\n"
        result += f"----- {len(cheetah)} Cheetahs: \n"
        result += "\n".join([c.__repr__() for c in cheetah]) + "\n"

        return result

    def workers_status(self):

        keeper = [a for a in self.workers if a.__class__.__name__ == "Keeper"]
        caretaker = [a for a in self.workers if a.__class__.__name__ == "Caretaker"]
        vet = [a for a in self.workers if a.__class__.__name__ == "Vet"]

        result = f"You have {len(self.workers)} workers:\n"
        result += f"----- {len(keeper)} Keepers: \n"
        result += "\n".join([k.__repr__() for k in keeper]) + "\n"
        result += f"----- {len(caretaker)} Caretaker: \n"
        result += "\n".join([c.__repr__() for c in caretaker]) + "\n"
        result += f"----- {len(vet)} Vet: \n"
        result += "\n".join([v.__repr__() for v in vet]) + "\n"

        return result

# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())

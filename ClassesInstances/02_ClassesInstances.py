# class Smartphone:
#     def __init__(self, memory):
#         self.memory = memory
#         self.apps = []
#         self.is_on = False

#     def power(self):
#         if self.is_on:
#             self.is_on = False
#         else:
#             self.is_on = True

#     def install(self, app, app_memmory):
#         if app_memmory <= self.memory and self.is_on == False:
#             return "Turn on the phone to install {app}"
#         if app_memmory <= self.memory and self.is_on:
#             self.apps.append(app)
#             self.memory -= app_memmory
#         else:
#             return f"Not enough memory to insatll {app}"
#     def status(self):
#         return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


# smartphone = Smartphone(100)
# print(smartphone.install("Facebook", 60))
# smartphone.power()
# print(smartphone.install("Facebook", 60))
# print(smartphone.install("Messenger", 20))
# print(smartphone.install("Instagram", 40))
# print(smartphone.status())
############################################################################################################################
# class Vet:

#     animals = []                      ## class attribute total num of animals for all vets
#     space = 5

#     def __init__(self, name):
#         self.name = name
#         self.animals = []

#     def register_animal(self, animal_name):
#         if Vet.space > len(Vet.animals):              ### v bolnicata dali ima mqsto 
#             self.animals.append(animal_name)
#             Vet.animals.append(animal_name)
#             return f"{animal_name} was registered in the clinic"
#         return "Not enough space"
    
#     def unregister_animal(self, animal_name):
#         if animal_name in self.animals:
#             self.animals.remove(animal_name)
#             Vet.animals.remove(animal_name)
#             return f"{animal_name} unregistered successfuly"
#         return f"{animal_name} not in the clinic"

#     def info(self):
#         return f"{self.name} has {len(self.animals)}. {Vet.space - len(Vet.animals) } space left in the clinic."

# peter = Vet("Peter")
# george = Vet("George")
# print(peter.register_animal("Tom"))
# print(george.register_animal("Cory"))
# print(peter.register_animal("Fishy"))
# print(peter.register_animal("Bobby"))
# print(george.register_animal("Kay"))
# print(george.unregister_animal("Cory"))
# print(peter.register_animal("Silky"))
# print(peter.unregister_animal("Molly"))
# print(peter.unregister_animal("Tom"))
# print(peter.info())
# print(george.info())
############################################################################################################################
# class Glass:

#     capacity = 250

#     def __init__(self):
#         self.content = 0
    
#     def fill(self, ml):
#         self.content += ml
#         if Glass.capacity >= self.content:
#             return f"Glass filled with {ml} ml"

#         return f"Cannot add {ml} ml"

#     def empty(self):
#         self.content = 0
#         return "Glass is now empty"

#     def info(self):
#         return f"{Glass.capacity - self.content} ml left"

# glass = Glass()
# print(glass.fill(100))
# print(glass.fill(200))
# print(glass.empty())
# print(glass.fill(200))
# print(glass.info())
############################################################################################################################
# class Circle:

#     pi =3.14

#     def __init__(self, radius):
#         self.radius = radius
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#     def get_area(self):
#         return f"{Circle.pi * self.radius**2}"
#     def get_circumference(self):
#         return f"{round(2*Circle.pi*self.radius,2)}"

# circle = Circle(10)
# print(circle.set_radius(12))
# print(circle.get_area())
# print(circle.get_circumference())
############################################################################################################################
# class Account:
#     def __init__(self, id, name, balance = 0):   ## balance is optional and by default is 0
#         self.id = id
#         self.name = name
#         self.balance = balance
    
#     def credit(self, ammount):
#         self.balance += ammount
#         return self.balance
    
#     def debit(self, ammount):
#         if self.balance >= ammount:
#             self.balance -= ammount
#             return self.balance
#         return "Amount exceeded balance"
    
#     def info(self):
#         return f"User {self.name} with account {self.id} has {self.balance} balance."

# account = Account(5411256, "Peter")
# print(account.debit(500))
# print(account.credit(1000))
# print(account.debit(500))
# print(account.info())
############################################################################################################################
# from datetime import datetime, timedelta

# class Time:

#     def __init__(self, hours, minutes, seconds):
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds
#         self.time_obj = datetime(100, 1, 1, hours, minutes, seconds)

#     def set_time(self, hours, minutes, seconds):
#         self.time_obj = datetime(100, 1, 1, hours, minutes, seconds)
#         self.hours = hours
#         self.minutes = minutes
#         self.seconds = seconds

#     def get_time(self):
#         return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

#     def next_second(self):
#         self.time_obj  += timedelta(seconds=1)   # +1 sec
#         self.hours = self.time_obj.hour
#         self.minutes = self.time_obj.minute
#         self.seconds = self.time_obj.second

#         return self.get_time()
        

# time = Time(10, 59, 59)
# print(time.next_second())
############################################################################################################################
# class PizzaDelivery:

#     ordered = False

#     def __init__(self, name: str, price: float, ingredients: dict):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
    
#     def add_extra(self, ingredient: str, quantity: int, ingredient_price: float):
#         if ingredient in self.ingredients.keys():
#             self.ingredients[ingredient] += quantity
#             self.price += quantity * ingredient_price
#         else:
#             self.ingredients[ingredient] = quantity
#             self.price += quantity * ingredient_price
    
#     def remove_ingredient(self, ingredient: str, quantity: int, ingredient_price: float):
#         if ingredient not in self.ingredients.keys():
#             return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}"

#         if ingredient in self.ingredients.keys() and quantity > self.ingredients[ingredient]:
#             return f"Please check again the desired quantity of {ingredient}"
        
#         else:
#             self.ingredients[ingredient] -= quantity
#             self.price -= quantity * ingredient_price

#     def pizza_ordered(self):
#         ing = ""
#         for k, v in self.ingredients.items():
#             ing += f"{k}: {v}, "

#         PizzaDelivery.ordered = True
#         return f"Youve ordered pizza {self.name} prepared with {ing}and the price will be {self.price} lv."

# Margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
# Margarita.add_extra('mozzarella', 1, 0.5)
# Margarita.add_extra('cheese', 1, 1)
# Margarita.remove_ingredient('cheese', 1, 1)
# print(Margarita.remove_ingredient('bacon', 1, 2.5))
# print(Margarita.remove_ingredient('tomatoes', 2, 0.5))
# Margarita.remove_ingredient('cheese', 2, 1)
# print(Margarita.pizza_ordered())
# print(Margarita.add_extra('cheese', 1, 1))

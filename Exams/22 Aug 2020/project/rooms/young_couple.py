from aug_twentytwo.project.rooms.room import Room
from aug_twentytwo.project.appliances.tv import TV
from aug_twentytwo.project.appliances.fridge import Fridge
from aug_twentytwo.project.appliances.laptop import Laptop

class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, budget=salary_one+salary_two, members_count=2)
        self.room_cost = 20
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.appliances)


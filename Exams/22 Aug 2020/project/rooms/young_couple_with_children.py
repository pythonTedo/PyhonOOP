from aug_twentytwo.project.rooms.room import Room
from aug_twentytwo.project.appliances.tv import TV
from aug_twentytwo.project.appliances.fridge import Fridge
from aug_twentytwo.project.appliances.laptop import Laptop
from aug_twentytwo.project.people.child import Child

class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, budget=salary_two+salary_one, members_count=(2+len(children)))
        self.room_cost = 30
        self.children = list(children)
        self.appliances = [TV(), Fridge(), Laptop()] * self.members_count
        self.expenses = self.calculate_expenses(self.children, self.appliances)


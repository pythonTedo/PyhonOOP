from aug_twentytwo.project.rooms.room import Room
from aug_twentytwo.project.appliances.tv import TV
from aug_twentytwo.project.appliances.fridge import Fridge
from aug_twentytwo.project.appliances.stove import Stove

class OldCouple(Room):

    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, budget=pension_one+pension_two, members_count=2)
        self.room_cost = 15
        self.appliances = [TV(), Fridge(), Stove()] * self.members_count

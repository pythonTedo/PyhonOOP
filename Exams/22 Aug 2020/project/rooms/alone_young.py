from aug_twentytwo.project.rooms.room import Room
from aug_twentytwo.project.appliances.tv import TV

class AloneYoung(Room):

    def __init__(self, family_name, salary):
        super().__init__(family_name, budget=salary, members_count=1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)

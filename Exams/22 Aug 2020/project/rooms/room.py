from aug_twentytwo.project.appliances.appliance import Appliance
from aug_twentytwo.project.people.child import Child

class Room:

    def __init__(self, family_name, budget, members_count):
        self.family_name = family_name
        self.budget = budget
        self.members_count = members_count
        self.children = []
        self.expenses = 0

    @property
    def expenses(self):
        return self._expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError('Expenses cannot be negative')
        self._expenses = value

    def calculate_expenses(self, *args):
        total_expenses = 0
        for list_obj in args:
            for obj in list_obj:
                if isinstance(obj, Appliance):
                    total_expenses += obj.get_monthly_expense()
                elif isinstance(obj, Child):
                    total_expenses += obj.cost
        self.expenses = total_expenses
        return self.expenses



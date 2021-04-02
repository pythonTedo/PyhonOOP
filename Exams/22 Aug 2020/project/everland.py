from aug_twentytwo.project.rooms.room import Room

class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += room.expenses + room.room_cost

        return f'Monthly consumptions: {total_consumption:.2f}$.'

    def pay(self):
        result = ""

        for room in self.rooms:
            if room.budget >= room.expenses:
                total_expenses = room.expenses + room.room_cost
                new_budget = room.budget - total_expenses
                result += f"{room.family_name} paid {total_expenses:.2f}$ and have {room.budget:.2f}$ left.\n"
                room.budget = new_budget
            else:
                result += f"{room.family_name} does not have enough budget and must leave the hotel.\n"
                self.rooms.remove(room)
        return result[:-1]

    def status(self):
        final_text = ""
        total_people = sum([room.members_count for room in self.rooms])
        final_text += f"Total population: {total_people}\n"

        for room in self.rooms:
            final_text += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$," \
                          f" Expenses: {room.expenses:.2f}$\n"
            if room.__class__.__name__ == "YoungCoupleWithChildren":
                for index, child in enumerate(room.children):
                    final_text += f"--- Child {index} monthly cost: {child.cost:.2f}$\n"

            appliances_cost = sum([app.get_monthly_expense() for app in room.appliances])
            final_text += f"--- Appliances monthly cost: {appliances_cost:.2f}$\n"
        return final_text[:-1]
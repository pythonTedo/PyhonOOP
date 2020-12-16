from Inheritance.mix_it_06.capacity_mixin import CapacityMixin
from Inheritance.mix_it_06.vehicle.vehicle import Vehicle

class Bus(Vehicle):

    def __init__(self, available_seats: int, ticket_price: float, tickets_sold=0):
        super().__init__(available_seats)
        self.ticket_price = ticket_price
        self.tickets_sold = tickets_sold

    def get_ticket(self, tickets_count):
        try:
            CapacityMixin.get_capacity(self.available_seats, self.tickets_sold + tickets_count)
            self.available_seats -= tickets_count
            self.tickets_sold += tickets_count
        except Exception as ex:
            str(ex)

    def get_total_profit(self):
        return self.ticket_price * self.tickets_sold

# b = Bus(5, 4.5, 0)
#
# print(b.get_ticket(5))
# print(b.get_total_profit())
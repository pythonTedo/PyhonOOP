from Inheritance.mix_it_06.vehicle.vehicle import Vehicle

class Plane(Vehicle):

    def __init__(self, available_seats: int, rows: int, seats_per_row: int):
        super().__init__(available_seats)
        self.rows = rows
        self.seats_per_row = seats_per_row
        self.seats_available = {}

        self.temp_dict = {row_num: self.seats_per_row for row_num in range(1, self.rows+1)}

    def buy_tickets(self, row_number, tickets_count):

        if row_number not in range(1, self.rows+1): ## check if we have this key(row number)
            return f"There is no row {row_number} in the plane!"

        try:
            seats = self.seats_available[row_number] if row_number in self.seats_available else self.seats_per_row
            self.get_capacity(seats, tickets_count)
            self.seats_available[row_number] = self.seats_per_row - tickets_count
            self.available_seats -= tickets_count
            return tickets_count
        except Exception as ex:
            return f"Not enough tickets on row {row_number}!"


# p = Plane(20, 4, 5)
# print(p.buy_tickets(2, 4))
from AttributesMethods.movie_word_02.customer import Customer
from AttributesMethods.movie_word_02.dvd import DVD

class MovieWorld:

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []
        # self.dvd_ids = {}
        # self.customer_ids = {}

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer):
        if len(self.customers) <= MovieWorld.customer_capacity():
            self.customers.append(customer)
            ## self.customer_ids[customer.id] = customer  :::: dict ot cutomers id: value(stoinosti na obj)

    def add_dvd(self, dvd):
        if len(self.dvds) <= MovieWorld.dvd_capacity():
            self.dvds.append(dvd)
            ## self.dvd_ids[dvd.id] = dvd ::::: dict ot dvd_id: value(dvd obj)

    def rent_dvd(self, customer_id, dvd_id):
        curr_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        curr_customer = [c for c in self.customers if c.id == customer_id][0]

        if curr_dvd.is_rented:
            return "DVD is already rented"
        if curr_customer.age <= curr_dvd.age_restriction:
            return f"{curr_customer.name} should be at least {curr_dvd.age_restriction} to rent this movie"
        if curr_dvd in curr_customer.rented_dvd:
            return f"{curr_customer.name} has already rented {curr_dvd.name}"
        else:
            curr_dvd.is_rented = True
            curr_customer.rented_dvd.append(curr_dvd.name)
            return f"{curr_customer.name} has successfully rented {curr_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        curr_dvd = [d for d in self.dvds if d.id == dvd_id][0]
        curr_customer = [c for c in self.customers if c.id == customer_id][0]

        if curr_dvd.name in curr_customer.rented_dvd:
            curr_customer.rented_dvd.remove(curr_dvd.name)
            curr_dvd.is_rented = False
            return f"{curr_customer.name} has successfully returned {curr_dvd.name}"
        else:
            return f"{curr_customer.name} does not have that DVD"

        # curr_dvd = self.dvd_ids.get(dvd_id)
        # curr_cust = self.customer_ids.get(customer_id)
        #
        # if curr_cust.is_rented:
        #     return f"{curr_customer.name} does not have that DVD"
        # else:sdfsf

    def __repr__(self):
        string = []

        for i in self.customers:
            string.append(i)
        for i in self.dvds:
            string.append(i)
        return "\n".join([str(i) for i in string])



c1 = Customer("John", 16, 1)
c2 = Customer("Anna", 55, 2)

d1 = DVD("Black Widow", 1, 2020, "April", 18)
d2 = DVD.from_date(2, "The Croods 2", "23.12.2020", 3)

movie_world = MovieWorld("The Best Movie Shop")

movie_world.add_customer(c1)
movie_world.add_customer(c2)

movie_world.add_dvd(d1)
movie_world.add_dvd(d2)

print(movie_world.rent_dvd(1, 1))
print(movie_world.rent_dvd(2, 1))
print(movie_world.rent_dvd(1, 2))
print(movie_world.return_dvd(1, 2))
print(movie_world.return_dvd(2, 1))
#print(movie_world)

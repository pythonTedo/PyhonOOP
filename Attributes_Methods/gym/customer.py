import itertools

class Customer():

    id_iter = itertools.count(start = 1)

    def __init__(self, name: str, address: str, email: str):

        self.id = next(Customer.id_iter)
        self.name = name
        self.address = address
        self.email = email

    def __repr__(self):             ## za konzola ako debugvame da izpolzvame za pomosht
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
    
    @staticmethod        ## nqma znanie za instanciqta, ne raboti sus objecta
    def get_next_id():
        return next(Customer.id_iter)



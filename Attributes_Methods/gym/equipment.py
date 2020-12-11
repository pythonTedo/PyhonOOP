import itertools

class Equipment:

    id_iter = itertools.count(start = 1)
    def __init__(self, name: str):
        self.id = next(Equipment.id_iter)
        self.name = name
    
    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"
    
    @staticmethod        # nqma znanie za instanciqta, ne raboti sus objecta
    def get_next_id():
        return next(Equipment.id_iter)

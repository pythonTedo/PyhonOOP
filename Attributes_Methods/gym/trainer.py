import itertools

class Trainer:

    id_iter = itertools.count(start = 1)
    def __init__(self, name: str):
        self.id = next(Trainer.id_iter)
        self.name = name

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
    
    @staticmethod
    def get_next_id():
        return next(Trainer.id_iter)
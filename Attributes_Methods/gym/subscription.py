import itertools

class Subscription:

    id_iter = itertools.count(start = 1)
    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.id = next(Subscription.id_iter)
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
    
    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"
    
    @staticmethod
    def get_next_id():
        return next(Subscription.id_iter)


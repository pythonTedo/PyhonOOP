import itertools

class ExercisePlan:

    id_iter = itertools.count(start = 1)

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.id = next(ExercisePlan.id_iter)
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
    
    @classmethod              ## classmethods creatvat nova instanciq na class, suvdavat nov object v clasa
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):

        return cls(trainer_id, equipment_id, hours*60)
        ## cls zamestva ExercisePlan klasa

    @staticmethod        # nqma znanie za instanciqta, ne raboti sus objecta
    def get_next_id():
        return next(ExercisePlan.id_iter)

    def __repr__(self):
        return f"Plan <{self.id}> with duration {self.duration} minutes"

# c = ExercisePlan(5, 4, 5)
# c1 = ExercisePlan(8, 10, 1)

# c2 = ExercisePlan.from_hours(88, 88, 111)
# print(c.trainer_id)
# print(c2.trainer_id)
# print(c2.get_next_id())


class Gym:

    def __init__(self):
        self.cutomers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer):
        if customer not in self.cutomers:
            self.cutomers.append(customer)

    def add_trainer(self, trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: int):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id):
        subscription = [s for s in self.subscriptions if s.id == subscription_id][0]  ## prehodi mi prez vseki subscription
        customer = [c for c in self.cutomers if c.id == subscription.customer_id][0]  #s.id - tova e na class Subscription = self.id  [vrushta list][0-nuleviq element da mi go dade za da e int]

        # za klient v spisuka ako clienta id = Subscription.customer_id
        trainer = [t for t in self.trainers if t.id == subscription.trainer_id][0]  ## tova sa celi obekti 
        equipment = [e for e in self.equipment if e.id == subscription.exercise_id][0]
        plan = [p for p in self.plans if p.id == subscription.exercise_id][0]

        result = subscription.__repr__() + "\n" + customer.__repr__() + "\n" + trainer.__repr__() + "\n" + \
                 equipment.__repr__() + "\n" + plan.__repr__()
        return result


from AttributesMethods.gym_04.customer import Customer
from AttributesMethods.gym_04.equipment import Equipment
from AttributesMethods.gym_04.exercise_plan import ExercisePlan
#from AttributesMethods.gym_04.gym import Gym
from AttributesMethods.gym_04.subscription import Subscription
from AttributesMethods.gym_04.trainer import Trainer

customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))

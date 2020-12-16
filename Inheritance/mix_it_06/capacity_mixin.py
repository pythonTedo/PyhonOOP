class CapacityMixin:
    #
    # def __init__(self, capacity, amount):
    #     self.capacity = capacity
    #     self.amount = amount
    @staticmethod
    def get_capacity(capacity, amount):
        if amount > capacity:
            raise Exception("Capacity reached!")
        return capacity - amount
from Inheritance.mix_it_06.parking_mall.parking_mall import ParkingMall

class Level1(ParkingMall):
    PARKING_LOTS = 150

    def __init__(self):
        super().__init__(parking_lots=Level1.PARKING_LOTS)


# l1 = Level1()
#
# print(l1.PARKING_LOTS)
# print(l1.check_availability())
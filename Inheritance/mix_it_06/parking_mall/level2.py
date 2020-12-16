from Inheritance.mix_it_06.parking_mall.parking_mall import ParkingMall


class Level2(ParkingMall):
    PARKING_LOTS = 100

    def __init__(self):
        super().__init__(parking_lots=Level2.PARKING_LOTS)

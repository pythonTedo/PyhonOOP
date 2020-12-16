from Inheritance.mix_it_06.parking_mall.parking_mall import ParkingMall


class Level3(ParkingMall):
    PARKING_LOTS = 80

    def __init__(self):
        super().__init__(parking_lots=Level3.PARKING_LOTS)

class car:
    def __init__(self, c_color, c_band, c_name, c_price):
        self.color = c_color
        self.band = c_band
        self.name = c_name
        self.price = c_price


car1 = car("red", "奔驰", "e300", 1000000)
car2 = car("black", "宝马", "x5", 800000)
print(car1.__dict__)
print(car2.__dict__)

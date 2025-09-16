class Vehicle():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)

class Car(Vehicle):
    def __init__(self, make, model, year, body_style):
        super().__init__(make, model, year)
        self.body_style = body_style

class ElectricCar(Car):
    def __init__(self, make, model, year, body_style, battery_capacity):
        super().__init__(make, model, year, body_style)
        self.battery_capacity = battery_capacity
    def charge(self):
        print("Charging car")
tesla = ElectricCar("Tesla", "Cybertruck", 2025, "rectangle", 94.3)
tesla.display_info()
print("Body style:",tesla.body_style)
print("Battery capacity:",tesla.battery_capacity)
tesla.charge()
tesla.display_info()
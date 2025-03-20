class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year, num_doors):
        super().__init__(brand, model, year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.num_doors}")

class Bike(Vehicle):
    def __init__(self, brand, model, year, bike_type):
        super().__init__(brand, model, year)
        self.bike_type = bike_type

    def display_info(self):
        super().display_info()
        print(f"Type: {self.bike_type}")

# Create instances of Car and Bike
car = Car("Toyota", "Camry", 2020, 4)
bike = Bike("Giant", "Escape 3", 2021, "road")

car.display_info()
bike.display_info()

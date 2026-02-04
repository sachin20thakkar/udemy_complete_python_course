class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, index):
        return self.cars[index]
    
    def __repr__(self):
        return f"Garage({self.cars})"
    
    def __str__(self):
        return f"Garage with {len(self.cars)} cars"

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        for car in self.cars:
            print(car.get_info())

garage = Garage()
garage.add_car("Ford Mustang")
garage.add_car("Chevrolet Camaro")
garage.add_car("Dodge Challenger")

print(garage)  # Output: Garage with 3 cars
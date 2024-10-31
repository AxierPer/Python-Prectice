# Vehicle dealership exercise

class Vehicle:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
        self.availability = True

    def sell (self):
        if self.availability:
            self.availability =  False
            print(f"The vehicle {self.model} has been sold.")
        
        else:
            print(f"The vehicle {self.model} is not available.")

    def add_vehicle(self):
        self.availability = True
        print(f"The vahivle {self.model} is available.")


class Client:
    def __init__(self, name, id_client):
        self.name = name
        self.id_client = id_client
        self.owned_vehicles = []

    def buy_vehicle (self, vehicle):
        if vehicle.available:
            vehicle.sell()
            self.owned_vehicles.append(vehicle)
        else:
            print(f"The vehicle {vehicle.model} is not available")

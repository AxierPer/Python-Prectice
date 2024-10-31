# Vehicle dealership exercise

class Vehicle:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price
        self.availability = True

    def sell (self):
        if self.availability:
            self.availability = False
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
        if vehicle.availability:
            vehicle.sell()
            self.owned_vehicles.append(vehicle)
        else:
            print(f"The vehicle {vehicle.model} is not available")

class Vehicle_leadership:
    def __init__(self, ):
        self.vehicles = []
        self.clients = []

    def add_cars(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"The vehicle {vehicle.model} is add to inventory")

    def register_user(self, client):
        self.clients.append(client)
        print(f"The client {client.name} is add to client list.")

    def show_vehicles(self):
        print("Available vehicles: ")
        for car in self.vehicles:
            if car.availability:
                print(f"Model: {car.model}\nYear: {car.year}\nPrice: ${car.price}\n\n")

# Define all cars
vehicle_1 = Vehicle('Mazda',1990,2500)
vehicle_2 = Vehicle('Honda',2000,5000)
vehicle_3 = Vehicle('Chevrolet',2010,7500)

# Define user
client_special = Client("Axier", "001")

# Define Vehicle leadership
vehicle_leadership = Vehicle_leadership()
vehicle_leadership.add_cars(vehicle_1)
vehicle_leadership.add_cars(vehicle_2)
vehicle_leadership.add_cars(vehicle_3)
vehicle_leadership.register_user(client_special)

# Show vehicles
vehicle_leadership.show_vehicles()

# Client buy a vehicle
client_special.buy_vehicle(vehicle_3)

# Show vehicles
vehicle_leadership.show_vehicles()




class Vehicle:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"The vehicle {self.brand}. Has been sold.")

            print(f"The vehicle {self.brand} is not available.")

    def check_availability(self):
        return self.is_available

    def get_price(self):
        return self.price

    def start_engine(self):
        raise NotImplementedError("This method must be implemented by the subclass")

    def stop_engine(self):
        raise NotImplementedError("This method must be implemented by the subclass")


class Car(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The engine of car {self.brand} is start"
        else:
            return f"The car {self.brand} is not available"

    def stop_engine(self):
        if self.is_available:
            return f"The engine of car {self.brand} is stop."
        else:
            return f"The car {self.brand} is not available"

class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The bike {self.brand} is start"
        else:
            return f"The bike {self.brand} is not available"

    def stop_engine(self):
        if self.is_available:
            return f"The bike {self.brand} is stop."
        else:
            return f"The bike {self.brand} is not available"

class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"The engine of Truck {self.brand} is start"
        else:
            return f"The truck {self.brand} is not available"

    def stop_engine(self):
        if self.is_available:
            return f"The engine of truck {self.brand} is stop."
        else:
            return f"The truck {self.brand} is not available"


class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self,vehicle: Vehicle):
        if vehicle.check_availability():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print(f"Sorry, {vehicle.brand} is not available")

    def inquire_vehicle (self, vehicle: Vehicle):
        if vehicle.check_availability():
            availablility = "available"
        else:
            availablility = "not available"
        print(f"{vehicle.brand} is {availablility} and price is {vehicle.price}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_cars (self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"{vehicle.brand} is add to inventory")

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"The customer {customer.name} is add")

    def show_available_vehicles(self):
        print("The available: ")
        for vehicle in self.inventory:
            if vehicle.check_availability():
                print(f"Brand: {vehicle.brand}\nPrice: {vehicle.price}\n")

car1 = Car("Toyota", "Corola", 20000)
bike1 = Bike("Yamaha", "MT-09", 15000)
truck1 = Truck("Volvo", "FH16", 80000)

customer1 = Customer("Axier")

dealership = Dealership()

dealership.add_cars(car1)
dealership.add_cars(bike1)
dealership.add_cars(truck1)

dealership.show_available_vehicles()

customer1.inquire_vehicle(bike1)

customer1.buy_vehicle(bike1)

dealership.show_available_vehicles()

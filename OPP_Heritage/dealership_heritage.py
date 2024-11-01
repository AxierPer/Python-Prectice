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
        else:
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

    # def buy_vehicle()

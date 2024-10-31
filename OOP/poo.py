class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nobre es {self.name} y tengo {self.age}")

person_jhon = Person("Jhon Doe", 25)

person_jhon.greet()

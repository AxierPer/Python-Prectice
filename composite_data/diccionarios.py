numbers = {1: "uno", 2: "dos", 3: "tres"}

print(numbers)

informacion = {"nombre": "Axier", "apellido": "Perlaza", "edad": "20", "altura": 1.71}
print(informacion)
del informacion["altura"]
print(informacion)

claves = informacion.keys()
values = informacion.values()
# print(type(claves))
print(claves)
print(values)

pairs = informacion.items()
print(pairs)

contacts = {
    "Axier": {"apellido": "Perlaza", "edad": "20", "altura": 1.71},
    "Luis": {"apellido": "Alegria", "edad": "22", "altura": 1.81},
}
print(contacts["Axier"])

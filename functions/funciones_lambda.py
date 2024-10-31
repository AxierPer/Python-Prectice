add = lambda a,b : a + b

print(add(2,3))

multiply = lambda a,b : a * b

print(multiply(2,3))

# Cuadrado de cada numero en una lista

number =  range(11)
square = list(map(lambda x: x**2, number))

print(square)
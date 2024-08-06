def greet (name, last_name = "Doe"): #* Se le puede dar un valor por defecto
  print(f"Hello World {name} {last_name}")

# greet('Axier', 'Perlaza')
# greet(last_name='Perlaza', name='Axier')

def add (num1, num2):
  return num1 + num2

def subtract (num1, num2):
  return num1 - num2

def multiply (num1, num2):
  return num1 * num2

def divide (num1, num2):
  return num1 / num2

def power (num1, num2):
  return num1 ** num2


def calculate ():
  while True:
    print("1. Suma")
    print("2. Resta")
    print("3. multiplicacion")
    print("4. division")
    print("5. potenciacion")
    print("6. salir")
    
    operator = int(input("Elige una operacion: "))
    if operator == 6:
      break
    
    if operator in [1, 2, 3, 4, 5]:
      num1 = float(input("Ingresa el primer valor: "))
      num2 = float(input("Ingresa el segundo valor: "))
      if operator == 1:
        print(num1, "+", num2, "=", add(num1, num2), "\n")
      elif operator == 2:
        print(num1, "-", num2, "=", subtract(num1, num2), "\n")
      elif operator == 3:
        print(num1, "*", num2, "=", multiply(num1, num2), "\n")
      elif operator == 4:
        print(num1, "/", num2, "=", divide(num1, num2), "\n")
      elif operator == 5:
        print(num1, "**", num2, "=", power(num1, num2), "\n")
    else:
      print("Operacion no valida")

calculate()
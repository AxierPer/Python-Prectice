todo = ["Dirigirnos al hotel", "Ir a almorzar", "Visitar un museo", "Volver al Hotel"]

print(todo)

print(todo[0])
print(todo[-1])
print(todo[1:3])
print(todo[:3])
print(todo[3:])

todo.append("Ir al Gym")  # ? Inserta el dato siempre al final de la lista (append())
print(todo)
todo.insert(
    3, "Ir al Gym"
)  # ? Inserta el dato en la posicion donde nosotros le digamos (insert(position, data))
print(todo)
print(todo.index("Ir al Gym"))

numbers = [1, 3, 5, 7, 9, 100, 98.4, 102]
print(numbers)
print(max(numbers))
print(min(numbers))

del numbers[-1]

print(numbers)

del numbers[0:2]

print(numbers)

del numbers

# print(numbers) Nos da un error ya que al haberla eliminado no existe

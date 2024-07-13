 #!--------------------------------------------------------------------------------------------------------------------------------------------------
 #!====================================================================== CADENAS DE TEXTO ==========================================================
 #!--------------------------------------------------------------------------------------------------------------------------------------------------



name = 'Axier Anderzon'
last_name = '-           Perlaza Melendez              -'
clasificador = 'AXIeR PerLAZA ß'
lista = [1,2,3,4,4,4,4,5,5,6,7,8,8,8,8,9,9]
print(name*5) #*El '*5(Se puede cambaira por otro valor)' junto con la variable hace que ese texto se me replique la cantidad de veces que yo quiera
print(name+' '+last_name)
print('Longitud de la cadena de name: ',len(name)) #*La funcion len() me deja ver la cantidad de caracteres de una cadena de texto
print('Longitud de la cadena de last_name:',len(last_name)) #*La funcion len() me deja ver la cantidad de caracteres de una cadena de texto
print(name.lower()) #* Cuando vienen dentro del string no se llaman funciones sino metodos (.lower) y esta pone todo en minusculas
print(name.upper())#* Cuando vienen dentro del string no se llaman funciones sino metodos (.lower) y esta pone todo en mayusculas
print(last_name.strip("- "))#*Este metodo sirve para eliminar todo lo que este dentro de los parentesis dentro de la cadena de texto
print(clasificador.capitalize())#*Retorna una copia de la cadena con el primer carácter en mayúsculas y el resto en minúsculas
print(clasificador.casefold())#*Retorna el texto de la cadena, normalizado a minúsculas. Los textos así normalizados pueden usarse para realizar búsquedas textuales independientes de mayúsculas y minúsculas y es mas agresivo que el lower.
print(lista.count(4)) #*Este metodo me permite contar la cantidad de veces que se repite algo dentro de una lista, cadena de texto, etc...
print("Seprador", "por", "comas", "con", "el", "condicional", "sep", sep=",")



 #!--------------------------------------------------------------------------------------------------------------------------------------------------
 #!====================================================================== TIPOS NUMERICOS ===========================================================
 #!--------------------------------------------------------------------------------------------------------------------------------------------------
 
x = 10
y = 5.6678
is_true = True
is_false = False
#z = 1.2E6
#a = 1.2E-6
# print(z)
# print(a)
print(type(x))
print(type(y))
print(x + x)
print(x + y)
print(y + y)
print(is_true)
print(is_false)

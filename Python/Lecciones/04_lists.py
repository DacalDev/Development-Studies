# Listas

my_list = list()
my_other_list = []

print(len(my_list)) # len en el caso de las listas cuenta el numero de elementos en la lista, comenzando desde 0

my_list = [37, 24, 62, 52, 30, 30, 17, 4]
print(my_list)
print(len(my_list))

my_other_list = [37, 1.77, "Javi", "Dacal"]
print(my_other_list)
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_other_list[-4])
"print(my_other_list[-5])" # Fuera de rango (IndexError)
"print(my_other_list[4])" # Fuera de rango (IndexError)

print(my_other_list.count("Javi")) # .count cuenta el numero de elementos definidos dentro de la lista
print(my_list.count(30))

age, height, name, surname = my_other_list
print(name)

name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3] # Forma rebuscada teniendo que ordenar los elementos
print(height)

print(my_list + my_other_list) # Concatenamos 2 listas
"print(my_list - my_other_list)" # No podemos restar listas
"print(my_list * my_other_list)" # Tampoco multiplicarlas

my_other_list.append("DacalDev") # Con el operador append agregamos un nuevo elemento a la lista, lo agrega la final
print(my_other_list)

my_other_list.insert(1, "Verde") # Con el operador insert agregamos elementos a la lista en la posicion deseada desplazando el resto
print(my_other_list)

my_other_list[1] = "Morado" # Accediendo al elemento de la lista podemos cambiarlo
print(my_other_list)

my_other_list.remove("Morado") # Elimina el elemento de la lista determinado
print(my_other_list)

my_list.remove(30) # Si el elemento estuviera repetido, eleminaria el primer valor encontrado
print(my_list)

print(my_list.pop(2)) # Sirve para remover un elemento determinado
print(my_list)

my_pop_element = my_list.pop(2) # Con pop puedes capturar ese elemento desapilado y guardarlo en otra variable
print(my_list)
print(my_pop_element)

my_other_list.append(my_list.pop(2)) # Podemos desapilar de una lista para insertar el elemento en otra
print(my_other_list)

del my_list[2] # Con del nos cargamos la posicion seleccionada sin mas, elimina por indice
print(my_list)

my_new_list = my_list.copy() # Copiamos una lista en otra

my_list.clear() # Vaciamos la lista
print(my_list)
print(my_new_list)

my_new_list.reverse() # Le damos la vuelta al orden de la lista
print(my_new_list)

my_new_list.sort() # Ordenamos la lista
print(my_new_list)

print(my_new_list[1:3]) # Imprimimos los elementos entre las posiciones

my_list = "Hola Python"
print(my_list)
print(type(my_list)) # Cambia el tipo al machar la variable list por que es un tipado dinamico el que usa Python

# No podemos crear constantes en Python


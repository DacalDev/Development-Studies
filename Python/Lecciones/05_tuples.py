# Tuples

my_tuple = tuple()
my_other_tuple = (37, 24, 62, 52, 30, 30, 17, 4)

my_tuple = (37, 1.76, "Javi", "Dacal", "Javi")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
"print(my_tuple[4])" # Fuera de rango (IndexError)
"print(my_tuple[-6])" # Fuera de rango (IndexError)


print(my_tuple.count("Javi")) # .count cuenta el numero de elementos definidos dentro de la tupla
print(my_tuple.count("DacalDev")) 

print(my_tuple.index("Dacal")) # .index nos devuelve el indice del primer valor encontrado en la tupla
print(my_tuple.index("Javi"))

"my_tuple[1] = 1.80" # Los valores dentro de las tuplas son inmutables, al contrario que en las listas
"my_tuple[5] = 1.80" # Tampoco se pueden ampliar mas haya de lo definido 

my_sum_tuple = my_tuple + my_other_tuple # Concatenamos 2 listas y las guardamos en una nueva tupla
print(my_sum_tuple)

print(my_sum_tuple[3:6]) # Imprimimos los elementos entre las posiciones

my_tuple = list(my_tuple) # Por definición las tuplas son inmutables, si queremos poder modificar una tupla lo que queremos es una lista
print(type(my_tuple))

my_tuple[4] = "DacalDev" # Las listas si son modificables
my_tuple.insert(1, "Verde")
my_tuple = tuple(my_tuple) # Volvemos a definir como tupla para hacerla inmutable
print(my_tuple)
print(type(my_tuple))

"del my_tuple" # Hemos eliminado la variable pese a ser inmutable por que del es una funcion del sistema y esta por encima
"print(my_tuple)" # name 'my_tuple' is not defined
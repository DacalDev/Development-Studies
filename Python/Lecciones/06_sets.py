# Sets

my_set = set()
my_other_set = {} # Inicialmente es un diccionario

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario

my_other_set = {"Javi", "Dacal", 37}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("DacalDev")
print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add("DacalDev") # Un set no admite repetidos

print(my_other_set)

print("Dacal" in my_other_set) # Comprobamos si el dato existe dentro del set
print("Dacol" in my_other_set)

my_other_set.remove("Dacal") # podemos eliminar datos dentro del set pese a no estar ordenados
print(my_other_set)

my_other_set.clear() # Podemos vaciar el set
print(len(my_other_set))

'del my_other_set' # Hemos eliminado la variable, del es una funcion del sistema y esta por encima
'print(my_other_set)' # name 'my_other_set' is not defined

my_set = {"Javi", "Dacal", 37}
my_list = list(my_set) # Al ser set una variable no ordenada al transformar en list en cada ejecución la lista tendra un orden diferente 
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}
my_new_set = my_set.union(my_other_set)
print(my_new_set.union({"JavaScript", "C#"})) # Si el union se ejecuta en el print no se guarda en la variable como ocurre arriba

print(my_new_set.difference(my_set)) # Compara 2 sets y devuelve los elementos diferentes entre ambos
# Dictionaries

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Javi", "Apellido":"Dacal", "Edad":37, 1:"Python"} # El dicionario de se rellena con clave y valor

my_dict = {
    "Nombre":"Javi", 
    "Apellido":"Dacal", 
    "Edad":37, 
    "Lenguajes":{"Python", "Swift", "Kotlin"}, # Esto es una clave con un set como valor
    1:1.76 # Las claves pueden ser int
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict)) # len en este caso cuenta las claves no los valores
print(len(my_dict))

print(my_dict["Lenguajes"]) # Asi podemos llamar diretamente al valor almacenado en la clave
print(my_dict["Nombre"])

my_dict["Nombre"] = "Brais" # Podemos acceder al dicionario y cambiar un valor
print(my_dict["Nombre"])

my_dict["Calle"] = "Calle DacalDev" # Podemos agregar claves / valor al dicionario
print(my_dict)

del my_dict["Calle"] # Para eliminar claves / valor debemos llamar a del he indicarle la clave que queremos eliminar
print(my_dict)

print("Apellido" in my_dict) # Las busquedas en los dicionarios se realizan por clave no por valor
print("Dacal" in my_dict)

print(my_dict.items()) # Retorna el listado de items (claves / valor) del diccionario en formato list
print(my_dict.keys()) # Retorna las claves del dicionario en formato list
print(my_dict.values()) # Retorna los valores del diccionario en formato list

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) # Con fromkeys creamos diccionarios sin valores, solo con claves
print(my_new_dict)

# Otras formas de crear diccionarios solo con claves mas creativas usando list
my_list = ["Nombre", 1, "Piso"]
my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)

# Creamos un nuevo diccionario a partir de otro conservando solo las claves
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

#  Fumada
my_new_dict = dict.fromkeys(my_dict, "DacalDev")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(list(dict.fromkeys(list(my_new_dict.values())).keys()))
print(tuple(my_new_dict))
print(set(my_new_dict))

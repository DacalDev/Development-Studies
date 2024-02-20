# Variables

my_variable = "My string variable"
print(my_variable)

my_int_variable = 5
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

# Print concatena variables separandolas por comas simples, independientemente del tipo
print(my_bool_variable, my_int_variable, my_variable)
#Podemos concatenar de igual manera textos "" con variables
print("Este es el valor de:", my_bool_variable)

my_int_to_str_variable = str(my_int_variable) # Transformamos una variable de entero en string
print(my_int_to_str_variable) # Lo imprimimos
print(type(my_int_to_str_variable)) # Comprobamos que el entero se a transformado en string

print(my_bool_variable, str(my_int_variable), my_variable) # Podemos transformar el entero en string dentro del print

print(type(print(my_bool_variable, str(my_int_variable), my_variable))) # Print al ser una función no tiene tipo, es decir es 'NoneType'

# Algunas funciones del sistema
print(len(my_variable)) # len() cuenta caracteres

# Variables en una sola línea ¡Cuidado con abusar de esta sintaxis!
name, surname, alias, age= "Javi", "Dacal", "DacalDev", 37
print("Mi alias es:", alias, "mi nombre es:", name, surname, "y mi edad es:", age)

# Función input()
name = input('¿Cuál es tu nombre? ')
age = input('¿Cuantos años tienes? ')
print(name, age)

# Cambiamos tipos de las variables sobre la marcha
name = 37
age = "Javi"
print(name, age)

# ¿Forzamos el tipo de la variable?.... no....
address: str = "Mi dirección"
address = 32
address = True
address = 1.2
print(type(address))
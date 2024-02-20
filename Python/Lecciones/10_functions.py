# Functions

# Definición

def my_function():
    print("Esto es una función")

my_function()
my_function()
my_function()

# Función con parámetros de entrada/argumentos

def sum_two_values(first_value, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno

def sum_two_values_with_return(first_value, second_value):
    return first_value + second_value

my_result = sum_two_values(1.4, 5.2) # Retorna none por que la funcion no tiene return
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Dacal", name = "Javi")

def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Javi", "Dacal")
print_name_with_default("Javi", "Dacal", "DacalDev")

# Función con parámetros de entrada/argumentos arbitrarios

def print_texts(*texts): #El asterisco indica que podemos pasar un numero infinito de argumentos del tipo text
    print(type(texts))
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python", "DacalDev")
print_texts("Hola")
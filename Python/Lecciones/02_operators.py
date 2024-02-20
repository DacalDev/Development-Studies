# Operadores

# Aritmeticos
print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3) # Operador de modulo, para saber el resto de la división
print(10 // 3) # Floor división, dividir para que de un entero y no decimales con aproximación
print(2 ** 3) # Exponencial, 2 elevado a 3
print(3 + 2 - 1 / 3 ** 2)

print("Hola " + "Python " + "¿Que tal? ") # Concatena strings

# print("Hola" - "Python") # Restas divisiones... no funcionan
# print("Hola" + 5) # No podemos concatenar tipos distintos

print("Hola " + str(5)) # Si llamamos a la funcion y lo convertimos si funciona
print("Hola " * 5) # Multiplicación si funciona
print("Hola " * (3 + 2 - 1 // 3 ** 2)) # Si el resultado de la operadción es un entero la Multiplicación funciona

# print("Hola " * 2.5) Si es decimal (Float) no funciona
# print("Hola " * (3 + 2 - 1 / 3 ** 2)) Si el resultado de la operación es decimal (Float) tampoco funciona

# Ejemplo de Numeros Complejos
print('Numeros Complejos: ', 1 + 1j)
print('Multiplicando numeros complejos: ',(1 + 1j) * (1 - 1j))

# Comparativos

# Enteros
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)

# Strings, comprueba ordenación alfabética por ASCII
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")

# Strings, con len comprobamos el numero de caracteres
print(len("Hola") > len("Python"))
print(len("Hola") < len("Python"))
print(len("Hola") >= len("Python"))
print(len("Hola") <= len("Python"))
print(len("Hola") == len("Python"))
print(len("Hola") != len("Python"))


# Operadores Lógicos

print(3 > 4 and "Hola" > "Python") # False y False devuelve False
print(3 > 4 or "Hola" > "Python") # False o False devuelve False, si uno de los 2 fuera True devolveria True
print(3 < 4 and "Hola" < "Python") # True y True devuelve True
print(3 < 4 or "Hola" < "Python") # True o True devuelve True, si uno de los 2 fuera False devolveria False
print(3 < 4 or ("Hola" > "Python" and 4 == 4)) # Podemos concatenar operadores logicos y delimitar su resolución con parentesis como en las operaciones matemáticas
print(not(3 > 4 and "Hola" > "Python")) # not niega la condición True o False 
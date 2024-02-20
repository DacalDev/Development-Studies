### Exercises - Day 2 ###

# Exercises: Level 1

'''
1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py
2. Write a python comment saying 'Day 2: 30 Days of python programming'
3. Declare a first name variable and assign a value to it
4. Declare a last name variable and assign a value to it
5. Declare a full name variable and assign a value to it
6. Declare a country variable and assign a value to it
7. Declare a city variable and assign a value to it
8. Declare an age variable and assign a value to it
9. Declare a year variable and assign a value to it
10. Declare a variable is_married and assign a value to it
11. Declare a variable skills and assign a value to it
12. Declare a variable person_info and assign a value to it
13. Declare multiple variable on one line
'''
first_name = input("Nombre: ")
last_name = input("Apellido: ")
full_name = (first_name, last_name)
country = input("Provincia: ")
city = input("Ciudad: ")
age = 37
is_married = True
skills = ['Python', 'HTML', 'CSS', 'JS']
person_info = {
    "Nombre" : first_name,
    'Apellido' : last_name,
    'Provincia' : country,
    'Ciudad' : city
}

print("Nombre: ", first_name)
print("Apellido: ", last_name)
print("Nombre completo: ", full_name)
print("Provincia: ", country)
print("Ciudad: ", city)
print("Edad: ", age)
print("¿Esta casado?", is_married)
print("Skills: ", skills)
print("Informacion personal: ", person_info)

# Exercises: Level 2

'''
1. Check the data type of all your variables using type() built-in function
2. Using the len() built-in function, find the length of your first name
3. Compare the length of your first name and your last name
4. Declare 5 as num_one and 4 as num_two
   Add num_one and num_two and assign the value to a variable total
   Subtract num_two from num_one and assign the value to a variable diff
   Multiply num_two and num_one and assign the value to a variable product
   Divide num_one by num_two and assign the value to a variable division
   Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
   Calculate num_one to the power of num_two and assign the value to a variable exp
   Find floor division of num_one by num_two and assign the value to a variable floor_division
5. The radius of a circle is 30 meters.
   Calculate the area of a circle and assign the value to a variable name of area_of_circle
   Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
   Take radius as user input and calculate the area.
6. Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
7. Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

'''
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_married))
print(type(skills))
print(type(person_info))

print(len(first_name))
print("Nombre tiene", len(first_name),"caracteres, mientras que Apellido tiene", len(last_name), "caracteres")

num_one = 5
num_two = 4
total = (num_one + num_two)
diff = (num_two - num_one)
product = (num_one * num_two)
division = (num_one / num_two)
remainder = (num_one % num_two)
exp = (num_one ** num_two)
floor_division = (num_one // num_two)

radius = input('¿Cual es el radio del circulo? ')
area_of_circle = (3.14 * int(radius) ** 2)
circum_of_circle = (3.14 * (2 * int(radius)))
print("La Circunferencia es de: ", circum_of_circle)
print("El Area es de: ", area_of_circle)

help("keywords")

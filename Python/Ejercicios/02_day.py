### Exercises - Day 3 ###


'''
1. Declare your age as integer variable
2. Declare your height as a float variable
3. Declare a variable that store a complex number
4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
        Enter base: 20
        Enter height: 10
        The area of the triangle is 100
5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
        Enter side a: 5
        Enter side b: 4
        Enter side c: 3
        The perimeter of the triangle is 12
6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
10. Compare the slopes in tasks 8 and 9.
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
14. I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
15. There is no 'on' in both dragon and python
16. Find the length of the text python and convert the value to float and convert it to string
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
        Enter hours: 40
        Enter rate per hour: 28
        Your weekly earning is 1120
22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
        Enter number of years you have lived: 100
        You have lived for 3153600000 seconds.
23. Write a Python script that displays the following table
        1 1 1 1 1
        2 1 2 4 8
        3 1 3 9 27
        4 1 4 16 64
        5 1 5 25 125
'''

age = 37
height = 1.76
complex_number = (1+1j)
triangle_base = input("¿Cuál es la base del triangulo?: ")
triangle_height = input("¿y su altura?: ")
area_of_triangle = (0.5 * float(triangle_base) * float(triangle_height))
print("El area del triangulo es", area_of_triangle)
triangle_side_a = input("¿Cuanto mide el primer lado del triangulo?: ")
triangle_side_b = input("¿el sgundo?: ")
triangle_side_c = input("¿y el tercero?: ")
perimeter_of_triangle = (float(triangle_side_a) + float(triangle_side_b) + float(triangle_side_c))
print("El perimetro del triangulo es", perimeter_of_triangle)
triangle_length = input("¿Cuál es el largo del triangulo?: ")
triangle_width = input("¿y su anchura?: ")
area_of_triangle = (float(triangle_length) * float(triangle_width))
perimeter_of_triangle = (2 * float(triangle_length + triangle_width))
print("El area del triangulo es", area_of_triangle)
print("El perimetro del triangulo es", perimeter_of_triangle)
pi = 3.14
circle_radius = input("¿Cuál es el radio de la circunferencia?: ")
area_of_circle = (pi * float(2 * circle_radius))
circum_of_circle = (2 * pi * float(circle_radius))
print("El area del circulo es", area_of_circle)
print("El perimetro del circulo es", circum_of_circle)

import math
p = [2, 2]
q = [6, 10]
print(math.dist(p, q))


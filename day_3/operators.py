# 1. Declare your age as integer variable
age = 19 

# 2. Delcare your height as a float variable
height = 5.4

# 3. Declare a variable that store a complex number
complex_number = 4 + 4j

# 4. Write a script that prompts the user to enter base and height of the traingle and caclulate an area of this triangle (area = 0.5 x b x h).
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)

# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Caculuate the perimeter of the triangle (perimeter a + b + c).
side_a = float(input("Enter side a of the triangle: "))
side_b = float(input("Enter side b of the triangle: "))
side_c = float(input("Enter side c of the triangle: "))
perimeter = side_a + side_b + side_c
print("The perimeter of the triangle is:", perimeter)

# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is:", area)
print("The perimeter of the rectangle is:", perimeter)

# 7. Get radius of a circle using prompt. Caculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * radius ** 2
circumference = 2 * pi * radius
print("The area of the circle is: ", area)
print("The circumference of the circle is: ", circumference)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x - 2
slope = 2
x_intercept = 1
y_intercept = -2
print("Slope: ", slope)
print("X-intercept: ", x_intercept)
print("Y-intercept: ", y_intercept)

# 9. Slope is m = (y2 - y1) / (x2 - x1). Find the slope between point (2, 2) and point(6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope = (y2 - y1) / (x2 - x1)
print("Slope between points (2, 2) and (6, 10): ", slope)

# 10. Compare the slopes in tasks 8 and 9.
if slope > 2:
    print("The slope between points (2, 2) and (6, 10) is greater than the slope of y = 2x - 2.")
else:
    print("The slope between points (2, 2) and (6, 10) is not greater than the slope of y = 2x - 2.")

# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x = float(input("Enter the value of x: "))
y = x ** 2 + 6 * x + 9
print("The value of y is: ", y)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
Length_python = len("python")
Length_dragon = len("dragon")
print("Length of 'python': ", Length_python)
print("Length of 'dragon': ", Length_dragon)
if Length_python == Length_dragon:
    print("The lengths are equal.")
else:
    print("The lengths are not equal.")

# 13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in 'python' and 'on' in 'dragon':
    print("'on' is found in both 'python' and 'dragon'")

# 14. I hope this course is not full of jargon. Use 'not' operator to check if 'jargon' is not in the sentence.
sentence = "I hope this course is not full of jargon."
if 'jargon' not in sentence:
    print("'jargon' not found in the sentence.")
else:
    print("'jargon' found in the sentence.")

# 15. There is no 'on' in both dragon and python
if 'on' not in 'dragon' and 'on' not in 'python':
    print("'on' is not found in both 'dragon' and 'python'")
else:
    print("'on' is found in either 'dragon' or 'python'")

# 16. Find the length of the text 'python' and convert the value to float and convert it to string
Length_python = len("python")
Length_python_float = float(Length_python)
Length_python_str = str(Length_python_float)
print("Length of 'python' as float: ", Length_python_float)
print("Length of 'python' as string: ", Length_python_str)

# 17. Even numbers are divisble by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(float(input("Enter a number to check if it is even or odd: ")))
if number % 2 == 0:
    print(number, "is an even number.")
else:
    print(number, "is an odd number.")

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
floor_division = 7 // 3
if floor_division == int(2.7):
    print("The floor division of 7 by 3 is equal to the int converted value of 2.7.")
else:
    print("The floor division of 7 by 3 is not equal to the int converted value of 2.7.")

# 19. Check if type of '10' is equal to type of 10
if type('10') == type(10):
    print("Type of '10' is equal to the type of 10.")
else:
    print("Type of '10' is not equal to the type of 10.")

# 20. Check if int('9.8') is equal to type of 10
if int('9.8') == type(10):
    print("int('9.8') is equal to type of 10")
else:
    print("int('9.8') is not equal to type of 10")

# 21. Write a script that prompts the user to enter number of years. Calculate pay of the person?
hours = print(int("Enter hours: "))
rate_per_hour = print(int("Enter rate per hour: "))
weekly_earnings = hours * rate_per_hour 
print("Your weekly earning is " + weekly_earnings)

# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years.
years_lived = print(int("Enter number of years you have lived: "))
number_hours = 365 * years_lived # Converts the number of years to hours
number_days = number_hours * 24 # Converts the number of hours to days
number_minutes = number_days * 60 # Converts the number of days to minutes
number_seconds = number_minutes * 60 # Converts the number of minutes to seconds
print("You have lived for " + number_seconds + " seconds.")

# 23. Write a Python script that displays the following table 
# 1 1 1 1 1 
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125 

for n in range(1, 6):
    print(n, 1, n, n**2, n**3)

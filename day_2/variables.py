# Day 2: 30 Days of python programming

# Exercise: Level 1
# Create a variable named first_name and assign a value to it
first_name = "Kevin"
# Create a variable named last_name and assign a value to it
last_name = "Pham"
# Create a variable named full_name and assign a value to it
full_name = first_name + " " + last_name
# Create a variable named country and assign a value to it
country = "United States"
# Create a variable named city and assign a value to it
city = "Phiadelphia"
# Create a variable named age and assign a value to it
age = 19
# Create a variable named year and assign a value to it
year = 2026
# Create a variable is_married and assigned a value to it
is_married = False
# Create a variable named is_true and assign a value to it
is_true = True
# Create a variable named is_light_on and assign a value to it
is_light_on = True
# Create multiple variable on one line
first_name, last_name, country, age = "Kevin", "Pham", "United States", 19

# Exercise Level 2:

# Check the data type of all your variables using type() built-in function
print(type(first_name)) # string)
# Using the len() built-in function, find the length of your first name
print(len(first_name)) # 5
# Compare the ;ength of your firsdt name and your last name
if len(first_name) > len(last_name):
    print("My first name is longer than my last name.")
# Add the num_one and num_two variables and assign the value to a variable total
num_one = 5
num_two = 4
total = num_one + num_two
print(total) # 9
# Multiply num_one and num_two and assign the value to a variable product
product = num_one * num_two
print(product) # 20
# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two
print(division) # 1.25
# Use the modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one
print(remainder) # 4
# Caclulate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two
print(exp) # 625
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two
print(floor_division) # 1
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius = 30
area_of_circle = 3.14 * radius ** 2
print(area_of_circle) # 2826.0
# Use the built-in function to get first name, last name, country and age from a user and store the value to their corresponding variable names 
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
country = input("Enter your country:")
age = int(input("Enter your age:"))

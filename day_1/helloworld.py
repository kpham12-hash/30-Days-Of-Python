# Day 1 - 30DaysOfPython Challenge

print(3 + 4)             # addition(+)
print(3 - 4)             # subtraction(-)
print(3 * 4)             # multiplication(*)
print(3 / 4)             # division(/)
print(3 ** 4)            # exponential(**)
print(3 % 4)             # modulus(%)
print(3 // 4)            # Floor division operator(//)

print("Kevin Pham")
print("Pham")
print("United States")
print("I am enjoying 30 days of python")

# Checking data types
print(type(10))          # Int
print(type(9.8))        # Float
print(type(3.14))      # Complex number
print(type(4 - 4j))  # Complex number
print(type(['Asabeneh', 'Python', 'Finland']))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type("Pham"))    # String
print(type(("United States")))    # String

print(4) # Int
print(4.1) # Float
print(5.0) # Float
print(5 + 5j) # Complex number
print("Whats up, this is me.") # String
print("This is a list of my favorite things: ", ['Python', 'JavaScript', 'C++']) # List
print("This is a dictionary of my favorite things: ", {'language':'Python', 'framework':'Django', 'database':'PostgreSQL'}) # Dictionary
# Creating a simple tuple
fruits = ("apple", "banana", "cherry")
print(4 == 4)    # True, value comparison
print(4 != 4)    # False, value comparison

# Ecludician distance formula
import math

def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
print(euclidean_distance((2,3), (10, 8))) # Output: 9.433981132056603

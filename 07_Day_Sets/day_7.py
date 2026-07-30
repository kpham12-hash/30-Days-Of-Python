# Excerises: Level 1
#1. Find the length of the set it_companies

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

#2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

#3. Insert multiple IT companies at once to the set it_companies

other_it_companies = ('AMD', 'NVIDIA', 'Samsung', 'Nothing')
it_companies.update(other_it_companies)

print(it_companies)

#4. Remove one of the companies from the set it_companies

it_companies.remove('Nothing')

print(it_companies)

#5. What is the difference between remove and discard

#if item found in Set using remove():
#   It wont raise error
#Else
#   It will raise an error.

fruits = {'Apple', 'Banna', 'Blueberry'}

fruits.remove('Blueberry')

print(fruits)

# fruits.remove("Grape") <--- Crashes program

#The Discard() method wont give or raise any errors. 

fruits.discard('Mango')
print(fruits)

# Exercise 2:

#1. Join A and B

A_and_B = A.union(B)

print(A_and_B)

#2. Find A intersection B

A_intersect_B = A.intersection(B)

print(A_intersect_B)

#3. Is A subset of B?

A_subset = A.issubset(B)

print(A_subset)

#4. Are A and B disjoint sets

B_disjoint = B.isdisjoint(A)

A_disjoint = A.isdisjoint(B)

print(A_disjoint)

print(B_disjoint)

#5. Join A with B and B with A

B_joined = B.union(A)

A_joined = A.union(B)

print(B_joined)

print(A_joined)

#6. What is the symmetric difference between A and B?

A_difference_B = A.symmetric_difference(B) 
B_difference_A = B.symmetric_difference(A)

print(A_difference_B)
print(B_difference_A)
#7. Delete the sets completely

del A

del B

# Exercises: Level 3

#1. Convert the ages to a set and compare the length of the list and the set, which one is bigger?

age = set(age)

print(age)

# 2. Explain the difference between the following data types: string, list, tuple and set

# A string is a data type found in computer programming containing of alphanumeric characters (letters and numbers). 

color = "red"

print(color)

# A list is a data structure used to store multiple items under a single variable name. They can be ordered, index-based or dynamic and mutatable. 

colors_card_set = ['Green Card', 'Red Card', 'Yellow Card', 'Blue Flag']

# A tuple is a collection of different data types whic his ordered and unchangeable (immutable) Written with round brackets. 

names_tuple = ('Jessica', 'Brian', 'Kevin', 'Dennis') 

# A set is a of collection of items. Set is a collection of unordered and un-indexed distinct elements. Written with round brackets. 

cities_set = {'New York', 'Toronto', 'Philadelphia'}

#3. I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.

sentence = "I am a teacher and I love to inspire and teach people."

split_words = sentence.split()

print(len(split_words))

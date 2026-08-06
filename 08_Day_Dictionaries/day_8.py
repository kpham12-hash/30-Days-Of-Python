# Exercises: Day 8

#1. Create an empty dictionary called dog
dog = {}

#2. Add name, color, breed, legs, age to the dog dictionary

dog = {
    'Name': 'Gerry',
    'Breed': 'Chihushua',
    'Legs': 4,
    'Age': 2 }

print(dog)

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary.

student = {
    'first_name': 'Kevin',
    'last_name': 'Pham',
    'gender': 'Male',
    'age': '19',
    'martial_status': 'Single',
    'Skills': ['Organization', 'Coding', 'Pay-attention To Detail', 'Teamwork', 'Communcation Skills', 'Event setup and Support', 'Reliablity'],
    'Country': 'United States',
    'City': 'Havertown',
    'Address': '1519 Melrose Avenue, Havertown, PA, USA'
}

#4. Get the length of the student dictionary.

print(len(student))

#5. Get the value of skills and check the data type, it should be a list.

print(type(student.get('Skills')))

#6. Modify the skills values by adding one or two skills.

student['Skills'].append('Python')
student['Skills'].append('C++')
print(student)

#7. Get the dictionary keys as a list.

keys = student.keys()

print(keys)

#8. Get the dictionary values as a list

values = student.values()

print(values)

#9. Change the dictionary to a list of tuples using items() method

print(student.items())

#10. Delete one of the items in the dictionary.

del student['Address']

print(student)

#11. Delete one of the dictionaries.

del dog

# Exercises: Level 1
# 1. Create an empty tuple

empty_tuple = ()

print(empty_tuple)

#2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine).

siblings_tuple = ("Dennis", "Audrey", "Jessica", "Brian")

print(siblings_tuple)

#3. Join brothers and sisters tuples and assign it to siblings

tpS = ("Audrey", "Jessica")

tpB = ("Dennis", "Brian")

combined_tuple = tpS + tpB

print(combined_tuple)

#4. How many siblings do you have?

print(len(combined_tuple))

#5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

family_members = ("David", "Anh")

Family_whole = family_members + siblings_tuple

print(Family_whole)

#Exercise Level 2:

#1. Unpack siblings and parents from family_members

David, *rest = Family_whole

print(David)
print(rest)

#2. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.

fruit_tuple = ("Banna", "Apple", "Grape", "Blueberry", "Peach", "Orange")
vegatables_tuple = ("Broccoli", "Red Pepper", "Yellow Pepper", "Carrot", "Potatoe", "Cabbage", "Lettuce")
foodproducts_tuple = ("Beef", "Pork", "Chicken", "Greens", "Rice")

food_stuff_tp = fruit_tuple + vegatables_tuple + foodproducts_tuple

print(food_stuff_tp)

#3. Change the about food_stuff_tp tuple to a food_stuff_lt list.

food_stuff_tp = list(food_stuff_tp)

print(food_stuff_tp)

#4. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.

food_stuff_tp = tuple(food_stuff_tp)

adjust_food_stuff_tp = food_stuff_tp[8:10]

print(adjust_food_stuff_tp)

# Another way:

middle = len(food_stuff_tp) // 2

# Takes one item before middle up to the middle item
adjust_food_stuff_tp = food_stuff_tp[middle - 1 : middle + 1]

print(adjust_food_stuff_tp)  # ('Yellow Pepper', 'Carrot')

#5. Slice out the first three items and the last three items from food_stuff_lt list

Sliced_first_three_items = food_stuff_tp[:3]

sliced_last_three_items = food_stuff_tp[15:]

print(Sliced_first_three_items)

print(sliced_last_three_items)

#6. Delete the food_stuff_tp tuple completely
del food_stuff_tp




#7. Check if an item exists in tuple:
#Check if 'Estonia' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country

print('Iceland' in nordic_countries)

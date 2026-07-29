#1. Declare an empty list

lst = list()

#2. Declare a list with more than 5 items.

cars = ['Ford', 'Chevy', 'Buick', 'BYD', 'Mercedes']

#3. Find the length of your list.

print(len(cars))

#4. Get the first item, the middle item and the last item of the list.

cars_first = cars[0]
cars_middle = cars[len(cars) // 2]
cars_last = cars[-1]

print(cars_first)
print(cars_middle)
print(cars_last)

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address).

mix_data_types = ['Kevin', 19, 5.4, 'Single', '1519 Melrose Ave, Havertown, PA']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7. Print the list using print()

print(it_companies)

#8. Print the number of companies in the list

print(len(it_companies))

#9. Print the first, middle and last company

it_companies_first = it_companies[0]
it_companies_middle = it_companies[len(it_companies) // 2]
it_companies_last = it_companies[-1]

print(it_companies_first)
print(it_companies_middle)
print(it_companies_last)

#10. Print the list after modifying one of the companies

last_index = len(it_companies) - 1
it_companies[last_index] = 'Samsung'
print(it_companies)

#11. Add an IT company to it_companies

it_companies.append('Amazon')
print(it_companies)

#12. Insert an IT company in the middle of the companies list

it_companies.insert(3, 'AMD')
print(it_companies)

#13. Change one of the it_companies names to uppercase (IBM excluded!)

upper_Facebook = it_companies[0].upper()
print(upper_Facebook)

#14. Join the it_companies with a string '#;  '
result = '#; '.join(it_companies)
print(result)

#15. Check if a certain company exists in the it_companies list.

does_exist = 'Apple'in it_companies
print(does_exist)

#16. Sort the list using sort() method
it_companies.sort(reverse=True)
print(it_companies)

#17. Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

#18. Slice out the first 3 companies from the list
print(it_companies[0:3])

#19. Slice out the last 3 companies from the list
print(it_companies[6:9])

#20. Slice out the middle IT company or companies from the list.
print(it_companies[4])

#21. Remove the first IT company from the list.
del it_companies[0]
print(it_companies)

#22. Remove the middle IT company or companies from the list
del it_companies[3:5]
print(it_companies)

#23. Remove the last IT company from the list.
del it_companies[5]
print(it_companies)

#24. Remove all IT companies from the list.
del it_companies[0:5]
print(it_companies)

#25. Destroy the IT companies list.
del it_companies

#26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

front_end.extend(back_end)
print('Different ends:', front_end)

#27. After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.

full_stack = front_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

# Exercises: Level 2
# 1. The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age.
ages.sort()
smallest_age = min(ages)
print(smallest_age)

largest_age = max(ages)
print(largest_age)

# Add the min age and the max age again to the list. 
ages.append(19)
ages.append(26)
print(ages)

# Find the median age (one middle item or two middle items divided by two)
n = len(ages)
mid = n // 2

if n % 2 == 0:
    median = (ages[mid - 1] + ages[mid]) / 2
else:
    median = ages[mid]
print(median)

# Find the average age (sum of all items divided by their number )

average = sum(ages) / len(ages)
print(average)

# Find the range of the ages (max minus min)

range = largest_age - smallest_age
print(range)

# Compare the value of (min - average) and (max - average), use abs() method.
print(abs(smallest_age - average))
print(abs(largest_age - average))

# 1. Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
];


first_index = (len(countries) // 2) - 1
second_index = len(countries) // 2

middle_countries = countries[first_index : second_index + 1]

print(middle_countries)

# 2. Divide the countries list into two equal lists if it is even if not one more country for the first half.

if len(countries) % 2 == 0:
    mid = (len(countries) // 2) - 1
else:
    mid = (len(countries) + 1) // 2 

first_half = countries[:mid]
second_half = countries[mid:]

print("The first half: ",len(first_half))
print("The second half: ",len(second_half))

#3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

western_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
China, Russia, USA, *scandic_countries = western_countries

print(China)
print(Russia)
print(USA)
print(scandic_countries)

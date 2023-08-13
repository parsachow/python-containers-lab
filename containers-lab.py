
# Exercise 1
# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

#Ex-1 solution

students = ['Parsa', 'Brent', 'Sofi', "Jorge"]
print(students[1])
print(students[-1])


# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "[food goes here] is a good food".

#Ex-2 solution

foods = ('burger', 'fries', 'ramen', 'dumpling')
for food in foods:
    print(f"{food} is good food")


# Exercise 3
# Using a for loop, print just the last two food strings from foods.
# Hint: Use the slice operator to select the last two foods

#Ex-3 solution

for food in foods[2:]:
    print(food)


# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format:
# "I was born in city, state - population of population"

#Ex-4 solution

home_town = {
    'city': 'Seattle',
    'state': 'Washington',
    'population': '1.5 million'
}
print(f"I was born in {home_town['city']}, {home_town['state']}- population of {home_town['population']}")


# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

#Ex-5 solution

for key, value in home_town.items():
    print(f"{key} = {value}")


# Exercise 6
# Create an empty list named cohort.

# Using a for loop to iterate over the students list.

# Hint: Use the enumerate function to provide both the index & student

# Within the for loop, add a dictionary to the cohort list that combines the student's name and the food in the foods list at the same index. Each dictionary will have this shape:

#  {
#    'student': 'Tina',
#    'fav_food': 'Cheeseburger'
#  }
# Iterate over the cohort list, printing out each item (it's not necessary to format the dictionaries).

#Ex-6 solution

cohort = []
for idx, student in enumerate(students):
    print(idx, student)
    cohort.append({
        'student': student,
        'fav_food': foods[idx]
    })

for student in cohort:
    print(student)


# Exercise 7
# Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over the awesome_students list, printing out each string.

#Ex-7 solution

awesome_students = [student for student in students]
for student in awesome_students:
    print(f"{student} is awesome")


# Exercise 8
# Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.
# Within the for loop, print each food string.

#Ex-8 solution

for food in [food for food in foods if 'a' in food]:
  print(food)
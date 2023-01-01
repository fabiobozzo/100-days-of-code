import random

states_of_america = ["Delaware", "Pensylvania", "New Jersey", "Georgia"]

# print(states_of_america[0])
# print(states_of_america[1])
# print(states_of_america[-1])
# print(states_of_america[-2])

states_of_america[1] = "Pencilvania"
states_of_america.append("Connecticut")
# print(states_of_america)
# print(random.choice(states_of_america))

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
veggies = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

# nested lists
dirty_dozen = [fruits, veggies]
print(dirty_dozen)
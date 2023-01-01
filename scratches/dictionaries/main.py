programming_dictionary = {
    "Bug": "An error in a program that prevents it from running as expected",
    "Function": "A piece of code one can call easily over and over",
    "Loop": "Programming construct to repeat a series of instructions a number of times"
}

# print(programming_dictionary["Function"])
# print(programming_dictionary["something"]) # error!
print(programming_dictionary)

empty_dictionary = {}
empty_dictionary["foo"] = "bar"

# programming_dictionary = {} # wipe out a dictionary content

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

# nesting dictionaries
travel_log = {
    "France": {"cities_visited": ["Paris", "Lyon", "Annecy"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Frankfurt"], "total_visits": 3}
}

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lyon", "Annecy"], 
        "total_visits": 12
    },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Frankfurt"], 
        "total_visits": 3
    }
]

print(travel_log)

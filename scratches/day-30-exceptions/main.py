# FileNotFoundError
# with open("notfound.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent"]

# IndexError
# fruit_list = ["apple", "banana", "pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# Catching exceptions
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    # print(a_dictionary["ciao"])
    print(a_dictionary["key"])
except FileNotFoundError:
    print("there was an error opening the file")
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"the key does not exist: {error_message}")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
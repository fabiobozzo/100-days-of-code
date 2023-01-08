# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# mode="r" -> read-only
# mode="w" -> write
# mode="a" -> append
with open("new_file.txt", mode="w") as file:
    file.write("Hello, my name is Sebastiano.")

with open("new_file.txt", mode="a") as file:
    file.write("\nCiao.")

with open("new_file.txt") as file:
    contents = file.read()
    print(contents)

# absolute paths
with open("/Users/fabio/test.txt") as file:
    contents = file.read()
    print(contents)

# relative paths
with open("../../../../test.txt") as file:
    contents = file.read()
    print(contents)


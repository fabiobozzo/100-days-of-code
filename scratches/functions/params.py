def greet(name): # name is a PARAMETER
    print(f"hello {name}")
    # print("how are you?")
    # print("isn't the weather lovely today?")

greet("fabio") # fabio is an ARGUMENT
greet("sebastiano")
greet(123)

def greet_with(name, location): 
    print(f"hello {name}. how's life in {location}?")

greet_with("fabio", "amsterdam")
greet_with(location="biella", name="sebastiano")
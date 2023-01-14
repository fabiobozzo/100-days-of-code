def add(*args):
    # print(args[0])
    # print(args[0])

    s = 0
    for n in args:
        s += n
    return s


print(add(3, 5, 6))
print(add(1, 7, 4, 3))


def calculate(n, **kwargs):
    print(kwargs)

    if "add" in kwargs:
        n += kwargs["add"]

    if "multiply" in kwargs:
        n *= kwargs["multiply"]

    return n


print(calculate(2, add=3, multiply=5))
print(calculate(2, add=3))


class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.seats = kw.get("seats")  # .get makes it optional


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model, my_car.make)

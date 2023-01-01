print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print(f"Child tickets are ${bill}")
    elif age <= 18:
        bill = 7
        print(f"Youth tickets are ${bill}")
    elif age >= 45 and age <= 55:
        print(f"Please have a free ride.") # mid-life crisis
    else:
        bill = 12
        print(f"Adult tickets are ${bill}")

    wants_photo = input("Do you want your photo taken? (y/n)")
    if wants_photo == "y":
        bill += 3

    print(f"Total: ${bill}")

else:
    print("Sorry. You have to grow taller before you can ride...")


fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit + " Pie")
    print("---")

# for number in range(1,10): # last number is excluded
    # print(number)

for number in range(1,10,3): # step size
    print(number)

total = 0
for number in range(1,101): 
    total += number

print(total)

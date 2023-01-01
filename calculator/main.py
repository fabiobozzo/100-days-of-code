import art

def add(n1, n2):
    """Add two numbers"""
    return n1 + n2

def multiply(n1, n2):
    """Multiply two numbers"""
    return n1 * n2

def subtract(n1, n2):
    """Subtract two numbers: n2 from n1"""
    return n1 - n2

def divide(n1, n2):
    """Divide two numbers: n1 by n2"""
    return n1 / n2

operations = {
    "+": add,
    "*": multiply,
    "-": subtract,
    "/": divide
}

print(art.logo)

def calculator():
    num1 = float(input("What's the first number? "))

    print("\n")
    for symbol in operations:
        print(symbol)

    should_continue = True
    while should_continue:
        operation_symbol = input("\nPick an operation: ")
        calculation_function = operations[operation_symbol]
        num2 = float(input("\nWhat's the next number? "))
        result = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {result}")
        
        if input(f"Type 'y' to continue calculating from {result} or 'n' to start over: ").lower() == "y":
            num1 = result
        else:
            should_continue = False
            print("\n---\n")
            calculator()

calculator()
import data

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_earnings = 0


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: {round(machine_earnings, 2)}$")


def is_choice_available(choice):
    if choice not in data.MENU:
        return False, ""
    for ingredient in data.MENU[choice]["ingredients"]:
        if resources[ingredient] < data.MENU[choice]["ingredients"][ingredient]:
            return False, ingredient
    return True, ""


def prompt_choice():
    valid_choices = ["espresso", "latte", "cappuccino", "off", "report"]
    choice = ""
    while choice not in valid_choices:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino) ").lower()
        if choice not in valid_choices:
            print("Please enter one of the available options.")
    return choice


def insert_coins():
    """Ask the customer to insert coins into the machine, in four different formats."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    value = quarters * data.QUARTER_VALUE + \
            dimes * data.DIME_VALUE + \
            nickels * data.NICKEL_VALUE + \
            pennies * data.PENNY_VALUE
    return round(value, 2)


def pay(choice, value_of_inserted_coins):
    """Use the inserted coins to increase the machine earnings and give back change to the customer, if applicable."""
    global machine_earnings
    machine_earnings += data.MENU[choice]["cost"]
    change = value_of_inserted_coins - data.MENU[choice]["cost"]
    if change > 0:
        print(f"Here is ${round(change, 2)} in change.")


def deliver_order(choice):
    """Prepare the hot drink by deducting the machine's resources that are needed for it."""
    global resources
    for ingredient in data.MENU[choice]["ingredients"]:
        resources[ingredient] -= data.MENU[choice]["ingredients"][ingredient]
    print(f"Here's your {choice}. Enjoy! ☕️")


def run():
    while True:
        choice = prompt_choice()

        match choice:
            case "off":
                print("The coffee machine has been turned off.")
                return
            case "report":
                print_report()
            case _:
                available, missing_ingredient = is_choice_available(choice)
                if available:
                    value_of_inserted_coins = insert_coins()
                    if value_of_inserted_coins >= data.MENU[choice]["cost"]:
                        pay(choice, value_of_inserted_coins)
                        deliver_order(choice)
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    print("Sorry, this choice is not available.")
                    if len(missing_ingredient) > 0:
                        print(f"There is not enough {missing_ingredient}")


if __name__ == "__main__":
    run()

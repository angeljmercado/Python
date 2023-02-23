MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

Penny = 0.01
Nickel = 0.05
Dime = 0.10
Quarter = 0.25

Money = 0


def report(money):
    """Report Resources Left in the Coffee Machine."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def process_coins():
    """Returns the total amount of coins inserted."""
    print("Please Insert Coins.")
    total = int(input("How Many Quarters?: ")) * Quarter
    total += int(input("How Many Dimes: ")) * Dime
    total += int(input("How Many Nickels: ")) * Nickel
    total += int(input("How Many Pennies: ")) * Penny
    return total


def is_resource_sufficient(order_ingredients):
    """Returns True When Order can Be made, and False if insufficient ingredients"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


def is_transaction_successful(money_received, drink_cost):
    """Return true when the payment is accepted, False if the money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 3)
        print(f"Here is ${change} in change.")
        global Money
        Money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for ingredient in order_ingredients:
        resources[ingredient] -= order_ingredients[ingredient]
    print(f"Here's Your {drink_name}.")
    return True


operations = True
while operations:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'report':
        report(Money)
    elif order == 'off':
        operations = False
    else:
        drink = MENU[order]
        if is_resource_sufficient(drink['ingredients']):
            payments = process_coins()
            cost_of_drink = drink['cost']
            if is_transaction_successful(payments, cost_of_drink):
                make_coffee(order, drink['ingredients'])






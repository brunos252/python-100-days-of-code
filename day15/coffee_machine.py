"""
Coffee machine
"""

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

money = 0


def print_report():
    print(f"Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(money))


def check_resources(drink):
    for resource in MENU[drink]["ingredients"]:
        if resources[resource] - MENU[drink]["ingredients"][resource] < 0:
            print(f"Sorry there is not enough {resource}")
            return False
        else:
            resources[resource] -= MENU[drink]["ingredients"][resource]

    return True


while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        break
    if user_input == "report":
        print_report()
        continue
    elif user_input not in MENU:
        print("Sorry, we do not have that.")
        continue
    elif not check_resources(user_input):
        continue

    print("Please insert coins")
    inserted = 0
    inserted += 0.25 * int(input("How many quarters?: "))
    inserted += 0.1 * int(input("How many dimes?: "))
    inserted += 0.05 * int(input("How many nickles?: "))
    inserted += 0.01 * int(input("How many pennies?: "))

    drink_price = MENU[user_input]["cost"]

    if inserted < drink_price:
        print("Sorry that's not enough money. Money refunded.")
        continue

    change = inserted - drink_price
    money += drink_price

    print("Here is $%.2f in change." % change)
    print(f"Here is your {user_input} ☕️. Enjoy!")

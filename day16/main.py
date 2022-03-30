from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        break

    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
        continue

    drink = menu.find_drink(user_input)
    if drink == None:
        continue

    if not coffee_maker.is_resource_sufficient(drink):
        continue

    if money_machine.make_payment(drink.cost):
        coffee_maker.make_coffee(drink)

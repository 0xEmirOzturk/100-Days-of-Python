from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
#menu_item = MenuItem()
coffee = CoffeeMaker()
money_machine = MoneyMachine()



to_cont = True

while to_cont:
    options = menu.get_items()
    choice = input(f"What would you like to offer? ({options}):").lower()
    if choice == "off":
        to_cont = False
    elif choice == "report":
        coffee.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee.make_coffee(drink)

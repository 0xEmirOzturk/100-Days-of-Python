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


def resources_sufficient(x):
    for i in x:
        if x[i] > resources[i]
            print(f"Sorry there is not enough {i} in the machine.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.10
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def transaction_success(x, y):
    if x >= y:
        change = round(x - y , 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += y
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(x, y):
    for i in y:
        resources[i] -= y[i]
    print(f"Here is your {x}. Enjoy!")





profit = 0


to_cont = True
while to_cont:
    ask_user = input("What would you like? (espresso/latte/cappuccino):").lower()
    if ask_user == "off":
        to_cont = False
    elif ask_user == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[ask_user]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_success(payment, drink["cost"]):
                make_coffee(ask_user, drink["ingredients"])




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

profit = 0



def resource_sufficient(x):
    for i in x:
        if x[i] > resources[i]:
            print(f'Sorry there is not enough {i}.')
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickels?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def transaction(money, cost):
    if money >= cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(name, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {name}. Enjoy!")



to_cont = True

while to_cont:
    coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()

    if coffee_type == "off":
        to_cont = False
    elif coffee_type == "report":
        print(f"Water: {resources['water']}")
        print(f"Milk: {resources['milk']}")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        coffee_req = MENU[coffee_type]
        if resource_sufficient(coffee_req["ingredients"]):
            payment = process_coins()
            if  transaction(payment, coffee_req["cost"]):
                make_coffee(coffee_type, coffee_req["ingredients"])

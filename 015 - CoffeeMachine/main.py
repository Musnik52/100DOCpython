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
    },
}
# ☕
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def make_drink(drink, payment):
    change = "${:.2f}".format(payment - MENU[drink]["cost"])
    for recorce in resources:
        resources[recorce] -= MENU[drink]["ingredients"][recorce]
    return f"Enjoy ☕. Your change is ${change}."


def sufficient_resorces(drink, payment):
    for recorce in resources:
        if resources[recorce] < MENU[drink]["ingredients"][recorce]:
            print(f"Insufficient {recorce}.")
            return False
    drink_cost = MENU[drink]["cost"]
    return payment >= drink_cost


def get_money():
    print("Please insert coins.")
    pennies = float(input("How many pennies ($0.01)?: ")) * 0.01
    nickles = float(input("How many nickles ($0.05)?: ")) * 0.05
    dimes = float(input("How many dimes ($0.10)?: ")) * 0.1
    quaters = float(input("How many quaters ($0.25)?: ")) * 0.25
    return pennies + nickles + dimes + quaters


machine_on = True
while machine_on:
    action = input("What would you like? (esspresso/latte/cappuccino): ").lower()

    if action in ["esspresso", "latte", "cappuccino"]:
        payment = get_money()
        if sufficient_resorces(action, payment):
            profit += MENU[action]["cost"]
            print(make_drink(action, payment))
        else:
            print("Transaction canceled.")

    if action == "report":
        money = "${:.2f}".format(profit)
        for recorce in resources:
            print(f"{recorce}: {resources[recorce]}")
        print(f"Money: {money}")

    if action == "off":
        print("Turning off...")
        machine_on = False

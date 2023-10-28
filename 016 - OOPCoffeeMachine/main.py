# import turtle

# timmy = turtle.Turtle()
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.forward(100)
# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# from prettytable import PrettyTable

# table = PrettyTable()
# table.add_column("PokeName", ["Charmander", "Squirtle", "Bulbasaur", "Pikachu"])
# table.add_column("PokeType", ["Fire", "Water", "Grass", "Electric"])
# table.align = "l"
# print(table)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
machine_on = True


while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        money_machine.report()
        coffe_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(
            drink.cost
        ):
            coffe_maker.make_coffee(drink)

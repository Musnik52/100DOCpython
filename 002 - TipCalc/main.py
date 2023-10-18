print("Welcome to the Tip Calc.")
total_cost = int(input("What's the total cost?\n"))
tip_percentage = int(input("How many % for the tip?\n")) / 100
num_of_guests = int(input("How many people?\n"))
tip = total_cost * tip_percentage

cost_individual = "{:.2f}".format(round(total_cost / num_of_guests, 2))
tip_individual = "{:.2f}".format(round(tip / num_of_guests, 2))
pay_idividual = "{:.2f}".format(round((total_cost + tip) / num_of_guests, 2))

print(
    f"Each person pays the following:\nCost: {cost_individual}\nTip: {tip_individual}\nTotal: {pay_idividual}"
)

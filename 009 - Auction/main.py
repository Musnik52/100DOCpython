import logo

print(logo.logo)
biggest_bid = 0
biggest_bidder = ""
bidders = {}
bidding = True

while bidding:
    first_name = input("Name: ").lower()
    while first_name in bidders:
        first_name = input("UNIQUE Name: ")
    bid = float(input("Bid: $"))
    bidders[first_name] = bid
    additional = input("Add another bidder? y/n\n").lower()
    while additional not in ["y", "yes", "n", "no"]:
        additional = input("Add another bidder? y/n\n").lower()
    bidding = True if additional in ["y", "yes"] else False
    
for bidder in bidders:
    if biggest_bid < bidders[bidder]:
        biggest_bid = bidders[bidder]
        biggest_bidder = bidder
print("${:.2f}".format(biggest_bid), "WINNER: ", biggest_bidder.capitalize())

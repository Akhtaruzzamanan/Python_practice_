from replit import clear
from logo import gavel
print(gavel, "\n")

# travel_log = [
#     {
#         "country": "France",
#         "visits": 12,
#         "cities": ["Paris", "Lille", "Dijon"]
#     },
#     {
#         "country": "Germany",
#         "visits": 5,
#         "cities": ["Brelin", "Hamburg", "Stuttgart"]
#     },
# ]

#TODO: Write the function that will work with the flowing line of code Add the entry for Russia to the travel_log
# def add_new_country(country, visit, city):
#     dicon = {}
#     dicon["country"] = country
#     dicon["visits"] = visit
#     dicon["cities"] = city
#     
#     travel_log.append(dicon)
# 
# add_new_country("Russia", 2, ["Moscow", "Saint"])
# print(travel_log)
# 
# for each in travel_log:
#     print(each.keys())
bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #bidding_record = {"zaman": 123, "raihan": 234}
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    
    name = input("What is your name?: ")
    price = input("What is your Bid?: $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes or no'.").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()

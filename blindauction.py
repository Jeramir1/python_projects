# from replit import clear
#HINT: You can call clear() to clear the output in the console.
import os
from blindauctionart import logo
#Definitions
bidders=[]
bids={}
try_again = 'y'
clear = lambda : os.system('clear')
# Function Definitions
def addbid(bidder_name, bid_amount):
    bidders.append ({"name" : bidder_name, "bid amount" : bid_amount})
# Print Logo
print (logo)
# Main Start
while try_again == 'y':
    name = input("What is your name? ")
    bid = input("What is your bid? $")
    addbid(bidder_name = name, bid_amount = bid)
    try_again = input("Are there any more bidders? y/n ").lower()
    # Clear console
    clear()
# Get max bidder
max_bid = max(bidders, key=lambda x:x['bid amount'])
# Print max bidder
print (f"The winner is {max_bid['name']} with a bid of ${max_bid['bid amount']}")
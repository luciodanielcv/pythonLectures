

from art import logo

import os


bid_dictionary={}
os.system("clear")

def add_bid_to_dictionary(the_name, the_bid):
  bid_dictionary[the_name] = the_bid

still_bidding = True
while still_bidding:
  os.system("clear")
  print(logo)
  
  the_name = input("Whats the name of the bidder: ")
  the_bid = int(input("Whats the amount of the bid? $"))
  add_bid_to_dictionary(the_name, the_bid)

  want_to_continue = input("Add more bidders (y/n)? ")
  if want_to_continue.lower() != "y":
    still_bidding = False

the_highest = 0
highest_bidder = ""
for key in bid_dictionary:
  if the_highest < bid_dictionary[key]:
    highest_bidder = key
    the_highest = bid_dictionary[key]

print(f"The highest bidder is: {highest_bidder} with ${bid_dictionary[highest_bidder]}")

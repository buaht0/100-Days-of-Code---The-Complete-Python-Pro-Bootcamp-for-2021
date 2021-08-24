from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")

secret_auction = {}
flag = True

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder

  print(f"The winner is {winner} with a bid of ${highest_bid} ")

while flag == True:
  name = input("What is your name?:")
  bid =  float(input("What's your bid?: $"))
  secret_auction[name] = bid 
  answer = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
  clear()
  if answer == "no":
    flag = False

find_highest_bidder(secret_auction)




# Modules 
from art import logo
from art import vs
from random import choice
from game_data import data 
from replit import clear 

# Display art
print(logo)

# Generate a random account from the game data.
def choice_account(data):
  account = choice(data) 
  return account


# Calculate score 
flag = False
score = 0
def calculation_score():
  return score + 1
  
# Clean screen 
def cleaner():
  clear()
  print(logo)

compare = choice_account(data)

# Make the game repeatable.
while(flag == False):

  print(f"Compare A:{compare['name']}, {compare['description']}, from {compare['country']}.")
  print(vs)
  against = choice_account(data)

  while compare == against:
      against = choice_account(data)
  print(f"Against B:{against['name']}, {against['description']}, from {against['country']}.")
  
  # Ask user for a answer
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  A = compare['follower_count']
  B = against['follower_count']

  if answer == "a" and A > B:
    cleaner()
    score = calculation_score()
    compare = compare
    print(f"You are right! Current score: {score}")
  elif answer == "b" and B > A:
    cleaner()
    score = calculation_score()
    compare = against
    print(f"You are right! Current score: {score}")
    
    
  else: 
    cleaner()
    flag = True
    print(f"Sorry, that's wrong. Final score: {score}")
  
  
    


  



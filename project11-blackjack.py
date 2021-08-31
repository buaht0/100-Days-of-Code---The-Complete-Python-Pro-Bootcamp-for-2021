# Project 11- Blackjack
# Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.

import random
from replit import clear 
from art import logo

def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

 # Create a function called calculate_score() that takes a List of cards as input 
 # and returns the score. 

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)

    return sum(cards)

# Create a function called compare() and pass in the user_score and computer_score.

def compare(user_score,computer_score):
  if computer_score == user_score:
    return "Draw"
  elif computer_score == 0 or user_score > 21:
    return "User loses."
  elif user_score == 0 or computer_score > 21:
    return "Computer loses."
  elif user_score > computer_score:
    return "User win"
  else:
    return "Computer win"

def play_game():

  print(logo)

  #user_cards = []
  #computer_cards = []

  user_cards = []
  computer_cards = []
  is_game_over = False

  for i in range(0,2):
    
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while is_game_over == False:
    print(f"Your cards: {user_cards}, current score: {calculate_score(user_cards)}")
    print(f"Computer's first card: {computer_cards}")

    if calculate_score(user_cards) == 0 or calculate_score(user_cards) > 21 or calculate_score(computer_cards) == 0:
        is_game_over = True
    else:      
      user_answer = input("Type 'y' to get another card, type 'n' to pass:")
      if user_answer == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
        
  while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
    computer_cards.append(deal_card())
  print(f"Your final hand: {user_cards}, final score: {calculate_score(user_cards)}")
  print(f"Computer final hand:{computer_cards}, final score: {calculate_score(computer_cards)}" )
  print(compare(calculate_score(user_cards), calculate_score(computer_cards)))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n':") == "y":
  clear()
  play_game()
  

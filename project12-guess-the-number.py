# Project 12 - Guess The Number
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Function to check user's guess against actual answer.
def check_answer(guess, answer,turns):
  if guess > answer:
    print("Too high.")
    return turns-1

  elif guess < answer:
    print("Too low.")
    return turns-1
  else:
    print(f"You got it! The answer was {answer}.")

# Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard':")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  # Logo 
  from art import logo
  
  print(logo)
  # Choosing a random number between 1 and 100.
  import random
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100")
  answer = random.randint(1,100)
  #print(f"Pssst, the correct answer is {answer}")
  turns = set_difficulty()
  

  # Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    # Let the user guess a number
    guess = int(input("Make a guess:"))

    turns = check_answer(guess, answer, turns)

    if turns == 0:
      print("You've run out of guesses, you lose.")
    elif guess!=answer:
      print("Guess again")
  return 



game()

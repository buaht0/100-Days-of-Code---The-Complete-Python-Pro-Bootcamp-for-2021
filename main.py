rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random 

choices = [rock, paper, scissors]


my_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

if my_choice >= 3 or my_choice < 0:
  print("İnvalid number")
  
else:
  print(f"You: {choices[my_choice]}")
  computer_choice = random.randint(0,2)
  print(f"Computer: {choices[computer_choice]}")


  if my_choice == 0:
    if computer_choice == 0:
      print("Draw")
    elif computer_choice == 1:
      print("Computer win!")
    else:
     print("You win!")
  elif my_choice == 1:
    if computer_choice == 0:
     print("You win!")
    elif computer_choice == 1:
     print("Draw")
    else:
     print("Computer win!")
  else:
    if computer_choice == 0:
      print("Computer win!")
    elif computer_choice == 1:
     print("You win!")
    else:
     print("Draw")



print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

move = input("left or right?: ").lower()

if move == "left":
   move = input("swim or wait: ").lower()
   if move == "wait":
     door_color = input("Which door?: ").lower()
     if door_color == "yellow":
       print("You Win!")
     elif door_color == "red":
       print("Burned by fire. Game Over.")
     elif door_color == "blue":
       print("Eaten by beasts. Game Over.")
     else:
       print("Game Over.")
   else:
     print("Attacked by trout. Game Over.")
else:
  print("Fall into a hole. Game Over.")

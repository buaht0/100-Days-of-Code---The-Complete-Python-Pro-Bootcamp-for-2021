#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

import random


# Letters
selected_letters = []
for letter in range(1,nr_letters+1):
  let_index = random.randint(0,len(letters)-1)
  selected_letters.append(letters[let_index])

print(selected_letters)

# Symbols 
selected_symbols = []
for symbol in range(1,nr_symbols + 1):
  symb_index = random.randint(0, len(symbols)-1)
  selected_symbols.append(symbols[symb_index])

print(selected_symbols)

# Numbers
selected_numbers = []
for number in range(1,nr_numbers + 1):
  num_index = random.randint(0, len(numbers)-1)
  selected_numbers.append(numbers[num_index])
print(selected_numbers)

passwd = []
passwd = selected_letters + selected_numbers + selected_symbols
print(passwd)

# Easy level
print("Easy")
for ps in passwd:
  print(ps, end = "")

# Hard level 
random.shuffle(passwd)

print("\nHard")
for ps in range(0,len(passwd)-1):
  print(passwd[ps], end = "")
print("\n")

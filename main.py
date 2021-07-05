#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12 or 15?")
people_count = input("How many people to split the bill?")

total_tip = (float(total_bill) / 100) * int(percentage_tip)

one_person_tip = total_tip / int(people_count)
one_person_bill = float(total_bill) / int(people_count)

pay = one_person_tip +one_person_bill
pay = round(pay,2)
pay = "{:.2f}".format(pay)
print(f"Each person should pay: ${pay}")

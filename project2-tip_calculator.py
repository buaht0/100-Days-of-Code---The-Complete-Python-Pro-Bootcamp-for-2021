# Project 2 - Tip calculator
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

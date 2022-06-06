print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
tip_percent = input("What percentage tip would you like to give? ")
people_to_split_bill = input("How many people will split the bill? ")
total_bill = float(total_bill)
tip_percent = float(tip_percent)
tip = tip_percent / 100 * total_bill
cost_with_tip = tip + total_bill
people_to_split_bill = float(people_to_split_bill)
cost_for_each_person = cost_with_tip / people_to_split_bill
cost_for_each_person = round(cost_for_each_person, 2)
print(f"Each person should pay: {cost_for_each_person}")
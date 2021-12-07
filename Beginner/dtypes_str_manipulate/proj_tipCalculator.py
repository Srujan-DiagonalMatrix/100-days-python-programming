####################################################
# Input: What is the total bill? $xxx.xx
# What percentage tip would you liek to give? 10, 12, or 15?
# How many people to split the bill?
#
#Output: Each person should pay: $XX.XX with 2 digit decimal only
####################################################

print("Welcome to the tip calculator.")
tot_bill = float(input("What was the total bill?\n"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
split = int(input("How many people to split the bill?\n"))

tip_amount = (tip * tot_bill) / 100
final_split = (tot_bill + tip_amount) / split
final_split = "{:.2f}".format(final_split)

print(f"Each person should pay: ${final_split}")

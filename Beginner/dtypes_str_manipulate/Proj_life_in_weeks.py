"""
Input: age in number
output: You have {} days, {} weeks, and {} months
Formula: 1 year == 365 days, 52 weeks, 12 months


Formula:
for 90 years:
    days: 32850
    weeks: 4680
    months: 1080

convert your age: days, months & weeks.
    days: 365*age
    weeks: 52*age
    months: 12*age

substract
"""

age = input("What is your age? \n")
age = int(age)

#Current age
days = 365*age
weeks = 52*age
months = 12*age

# Left over time
days_left = (32850 - days)
weeks_left = (4680 - weeks)
months_left = (1080 - months)

summary = f"You have {days_left} days, {weeks_left} weeks and {months_left} months left."
print(summary)

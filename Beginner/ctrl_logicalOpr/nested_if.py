height = int(input("What is your height?\n"))

if height <= 119:
    print("Sorry, you can't ride")
else:
    print("You can ride.")
    age = int(input("What is your age?\n"))
    if age < 12:
        print("Please pay $5")
    elif age >= 12 and age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
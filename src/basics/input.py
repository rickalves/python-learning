# input function
name = input("Enter your name:\n")
print("Welcome "+name+"!")
age = input("What is your birth year?\n")
print("You age is:", (2022-int(age)), end="!\n")
print("You have", ((2022-int(age)) * 365), "days of life", end="!\n")

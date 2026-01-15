# main.py
# My First Python Program


# TODO 1: Ask the user for their name
name = input("What is your name? ")


# TODO 2: Ask the user for their age
age_input = input("How old are you? ")
# TODO 3: Check if the age is a number
if age_input.isdigit():
age = int(age_input)


# TODO 4: Print a friendly message
print(f"Hello {name}!")
print(f"Next year, you will be {age + 1} years old.")
else:
# Error message if input is not a number
print("Oops! Please enter your age using numbers only.")

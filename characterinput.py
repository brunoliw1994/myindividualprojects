"""
file name: 
name: Bruno Valente
"""

"""
Exercise 1
Create a program that asks the user to enter 
their name and their age. Print out a message 
addressed to them that tells them the year that 
they will turn 100 years old. Note: for this exercise, 
the expectation is that you explicitly write out the year 
(and therefore be out of date the next year).
"""

# ask the user to enter their name
print()
name = input("What is your name? ")

# ask their age
print()
age = int(input(f"How old are you, {name}? "))

#year calculator
year = 2023 - age + 100

print()
print(f"Name: {name}")
print(f"Age: {age} years old")
print(f"You will turn 100 years old in {year}!")

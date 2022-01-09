# Program for getting the year of birth
# By Aaryan Thobhani
# GitHub:  https://github.com/AaryanThobhani

# Variables
num = input("Insert an integer number:")
num2 = input("Insert a number that is smaller than the first number:")

# Remainder
remainder = int(num) % int(num2)

# Printing the Remainder
print("If you divided {} by {}, your remainder would be {}.".format(int(num), int(num2), remainder))

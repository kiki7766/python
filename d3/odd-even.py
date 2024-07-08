# Which number do you want to check?
number = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
# rewrite a program that works out whether if a given number is an odd or even number.

# Even numbers can be divided by 2 with no remainder. 
# E.g. 86 is even because 86 ÷ 2 = 43
# 3 does not have any decimal places. Therefore the division is clean.# 
# e.g. 59 is odd because 59 ÷ 2 = 29.5 
# 9.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
if (number % 2) == True:
  print("This is an odd number.")
else:
  print("This is an even number.")
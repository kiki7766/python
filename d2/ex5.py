# Project 5 Season 2 xD
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip CALCULATOR!!!")
# We need a float value for the bill total asked from the user
bill = float(input("What was the total bill? $"))
# Well now is the % of the tip of the user would like to add to the total bill.
# Only asking the # of the tip not the % like 10, 12, 15
tip = int(input("How much tip would you like to give 10, 12, or 15? ")) 
# Asking the user how many people we should divide the total bill
people = int(input("Enter total people: "))
# Calculate the total of (bill total divide by total of people) times by the % of the tip entered
total = (bill/people) * (1 + (tip/100))
# we only need 2 decimal places so ...
total = format(total, ".2f")
# round (total, 2) (we could also use this method but I understood better the top one xD)
print (f"Total payment for each people is: ${total}") # Using the method of string with float inside of a sentence I think? xD
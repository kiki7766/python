# 💪 This is a difficult challenge! 💪
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
# 2. Then check for the number of times the letters in the word LOVE occurs.
# 3. Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is *x*, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is *y*, you are alright together."
# Otherwise, the message will just be their score. e.g.:

# "Your score is *z*."
# e.g.
# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5
# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3
# Love Score = 53
# Print: "Your score is 53."

print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
word1 ="true"
word2 = "love"
total_true = 0
total_love = 0
# letter_true1 = {t: name1.upper().count(t) for t in word1}
# letter_love1 = {l: name1.upper().count(l) for l in word2}

for t in word1:
    letter_true1 = name1.lower().count(t)
    letter_true2 = name2.lower().count(t)
    count_true = letter_true1 + letter_true2
    # print(f"{t} occurs {count_true} times")
    total_true += count_true
    # if 
    
for l in word2:
    letter_love1 = name1.lower().count(l)
    letter_love2 = name2.lower().count(l)
    count_love = letter_love1 + letter_love2
    # print(f"{l} occurs {count_love} times")
    total_love += count_love
    
total = str(total_true) + str(total_love)
total = int(total)
    
if (total< 10 or total> 90):
    print(f"Your score is {total}, you go together like coke and mentos.")
elif (total>= 40 and total<=50):
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

# print(f"true: {total_true}\nlove: {total_love} \n total {total}")
# letter_love2 = {}
# print(f"true: {letter_true1} \n love: {letter_love1}")
# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

# Warning. Do not change the code on line 1. Your program should work for different inputs. e.g. any two-digit number.

# The last line of your program should print the result.

# Example 1 Input
# 39

# Example 1 Output
# 12

two_digit_number = input()
# 🚨 Don't change the code above 👆
####################################
# Write your code below this line 👇
# change = str(two_digit_number)

# Since the input is type string (check pls)
# print(type(two_digit_number))
# what I tried to do is to convert the string into integer type in which I took the same variable
# two_digit_number and convert it into integer by using int(two_digit_number)
# okay so to understand why using the array ... so we need the very first value/character of the string 
# which would be location [0] so using int(two_digit_number[0]) we will get the first character of the input
# now we needed to do a similar stuff with the second digit after all of that we need to sum/add them together
# so by doing int(two_digit_number[0]) + int(two_digit_number[1]) we would get the add/sum of them
# so we finally would need the result print out right? so why not print them
# print(int(two_digit_number[0]) + int(two_digit_number[1]))
# we could also put it in a more elegibable way but would take a couple of more lines...
print(int(two_digit_number[0]) + int(two_digit_number[1]))


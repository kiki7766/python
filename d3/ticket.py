height = int(input("What's your height in cm: "))
age = int(input("What's your age? "))
photo = input("Want any photos? Y/N: ")
ticket = 0
if (height >= 120):
    # print("You will ride the rollcoaster!")
    if (age < 12 ):
        ticket = 5
    elif (age >= 12 and age <= 18):
        ticket = 7
    elif (age >= 45 and age <= 55):
        ticket = 0
    else:
        ticket = 12

else:
    print("You cannot ride the rollcoaster, sorry!")
    
        
if photo == "Y":
    ticket +=3
    
print (f"Your ticket is ${ticket}")
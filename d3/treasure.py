print("****************************************************")
print("****************************************************")
print("******************** HI Human **********************")
print("****************************************************")
print("****************************************************")

path = input("Where do you wanna go? (left or right): ")

if (path == "left"):
    print("Welcome to hell!!!!🔥🔥") 
    exit
elif (path == "right"):
    print("Great choice! Welcome to Heaven!")
    move = input("What do you prefer to do \"walk\" or \"scooter\"? ")
    if (move == "walk"):
        print("Perfect! You must be in shape!")
        color = input("Select a color: green, blue or orange? ")
        if (color == "orange"):
            print("Seems like you are hungry! xD")
            exit
        elif (color == "blue"):
            print("Well the sky is blue lately!")
        elif (color == "green"):
            print("FINALLY! You won!")
        else:
            print("Man, wrong input!")
            exit
    elif (move == "scooter"):
        print("I'll do the same btw hahaha!")
        exit
    else:
        print("Wrong input! :)")
        exit
else:
    print("Wrong input :)!")
    exit

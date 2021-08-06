#To write functions to simulate playing one game.
#The basic approach is to generate a random number representing the door behind which the real prize sits, and another random number representing the door that the contestant initially selects.
#Monty opens the remaining door.
#Then, have the contestant switch doors (or not switch doors), and see if the contestant winds up with the door behind which the prize sits.



from random import randint

def montyalways(): #Function for the case when the contestant always switches
    prize = randint(1,3) #The variable prize is the prize behind the door
                                #choosing the door with the prize
    choice1 = randint(1,3) #The variable choice1 is the number the contestant chooses
                                 #And the function randint is to make the contestant choose


    while True:
        door_no = randint(1,3) #The variable door_no is the door numbers

        if door_no == prize or door_no==choice1:
            continue

        else:
            break



    while True:
        choice2 = randint(1,3) #The variable choice2 is the number the contestant chooses after the first one

        if choice2==choice1 or choice2 == door_no:
            continue
        else:
            break

    if choice2 == prize:
        choice2 = True
    else:
        choice2 =  False

    return choice2 #Checking if the prize is behind the second door or not

def montynever(): #Function for the case when the contestant never switches

    prize = randint(1,3)
    choice1 = randint(1,3)
    if choice1 == prize:
        choice1 = True
    else:
        choice1 = False
    return choice1

montyalways()#To call function where contestant always switches

montynever()#To call function where contestant never switches

#Now we will simulate a large number of games.
#To ask the user for the number of games to be played.
#To play one set of games for the contestant always changing the door and another set for the contestant never changing the door.
#To print the resulting fraction of times that the contestant wins, and the number of games won.


from random import randint


games= input("Number of games to play:") #Takes input from the user i.e.,the number of games to be played


winning_prob=0 #Initialising the winning probability to 0

try:
    games=int(games) #Input has to be integer

    if games < 0: #To see that it is a positive integer

        print("Enter a positive number")

except:
    print("Enter a positive number")


else:

    print("Out of",games,"games:")

    def montyalways(): #The case where the contestant always switches
        win=0
        for line in range(0,games):#The variable prize is the prize behind the door
            prize=randint(1,3) #choosing the door with the prize
            contestant_choice=randint(1,3)#The variable contestant_choice is the number the contestant chooses
                                          #And the function randint is to make the contestant choose

            while True:#The variable door_no is the door number
                door_no=randint(1,3) #Choosing the door that monty hall opens

                if door_no==prize or door_no==contestant_choice: #Without the door with the prize and contestants choice
                    continue
                else:
                    break

            while True:
                next_choice= randint(1,3) #Door switched

                if next_choice==contestant_choice or next_choice==door_no: #New door should not be the old door or the door opened by Monty Hall
                    continue
                else:
                    break
            #print(next_choice,prize)
            if next_choice==prize: #To check if contestant has won

                win=win+1 #incrementing everytime he/she wins

        winning_prob=win/games #Probability of winning

        print("Always switching wins:",winning_prob,"(",win,"games)")


    def montynever(): #The case where the contestant does not switch

        win=0 #Intialising the variable win to 0
        for line in range(0,games):

            prize=randint(1,3) #Choosing the door with the prize
            contestant_choice=randint(1,3) #And the function randint is to make the contestant choose

            if contestant_choice==prize: #To check if the contestant won

                win=win+1 #Increments by 1 everytime he/she wins

            winning_prob=win/games #To find the probability of winning

        print("Never switching wins:",winning_prob,"(",win,"games)")

    montyalways() #To call function where contestant always switches

    montynever() #To call function where contestant never switches

#To add a graphical output to visualize the results
#To draw a histogram, with the bars being the relative sizes of the numbers

from random import randint

import turtle

games= input("Number of games to play:") #Takes input from the user i.e.,the number of games to be played


try:
    games=int(games) #Input has to be integer

    if games < 0: #To see that it is a positive integer

        print("Enter a positive number")

except:
    print("Enter a positive number")


else:

    print("Out of",games,"games:")

    def montyalways(): #The case where the contestant always switches
        global winning_prob1
        winning_prob1=0
        win=0
        for line in range(0,games): #The variable prize is the prize behind the door
            prize=randint(1,3) #choosing the door with the prize
            contestant_choice=randint(1,3) #The variable contestant_choice is the number the contestant chooses
                                           #And the function randint is to make the contestant choose

            while True: #The variable door_no is the door number
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

        winning_prob1=win/games #Probability of winning

        print("Always switching wins:",winning_prob1,"(",win,"games)")


    def montynever(): #The case where the contestant does not switch
        global winning_prob2
        winning_prob2=0

        win=0 #Intialising the variable win to 0
        for line in range(0,games):

            prize=randint(1,3) #Choosing the door with the prize
            contestant_choice=randint(1,3) #And the function randint is to make the contestant choose

            if contestant_choice==prize: #To check if the contestant won

                win=win+1 #Increments by 1 everytime he/she wins

            winning_prob2=win/games #To find the probability of winning

        print("Never switching wins:",winning_prob2,"(",win,"games)")




def subtitles(x,y,subtitle,s): #function to draw function
    s.penup()
    s.setx(x)
    s.sety(y)
    s.pendown()
    s.write(str(subtitle),False,"center", font=("Arial",10,"normal"))


def histogram(z,height,title): #Function to draw function
            z.begin_fill()

            z.left(90)

            z.forward(height)

            z.right(90)

            z.forward(20)

            z.write(str(title),False,"center",font=("Ariel",10,"normal"))

            z.forward(20)

            z.right(90)

            z.forward(height)

            z.right(90)

            z.forward(40)

            z.right(180)

            z.forward(40)

            z.end_fill()



def main():
    montyalways()

    montynever()

    apercent = int(winning_prob1*100)#% wins when it is always changing

    npercent = int(winning_prob2*100)#% wins when it is never changing

    border = 0.1

    windows = turtle.Screen()#To draw the window for the picture

    windows.bgcolor("White")

    windows.setworldcoordinates(0,-50,126,100)

    hist = turtle.Turtle()#create a turtle,called "rect_hist"

    hist.shape("turtle")#pen is a turtle

    hist.color("black")

    hist.fillcolor("black")#histogram bars are black in color

    hist.forward(10)

    histogram(hist,apercent,winning_prob1)

    hist.forward(25)

    histogram(hist,npercent,winning_prob2)

    hist.forward(10)

    subtitles(30,-8,"Always",hist)

    subtitles(95,-8,"Never",hist)

    subtitles(63,-15,"The Monty Hall Problem:"+str(games)+" games",hist)

    subtitles(63,-18,"Percentage of games if you switch always or never",hist)

    hist.hideturtle()#To hide the loop



    windows.mainloop()



main()

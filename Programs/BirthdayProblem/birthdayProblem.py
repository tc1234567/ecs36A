#The birthday problem asks how many people must be in a room so that the probability of two of them having the same birthday is 0.5

import random

def hasduplicates(l):#Defining a function hasduplicates to check for duplicate elements
    if len(l)!= len(set(l)):#Boolean value True is returned if the list contains duplicate elements length of the list is not
                            #equal to the length of the list with unique elements
                            #Boolean value False is returned if the list does not contain a duplicate element length of the list
                            #equal to the length of the list with unique elments

        return True
    else:
        return False

def onetest(count):#Function to get a list of random numbers between 1 and 365 (including 1 and 365)
                   #True is returned if the list has a duplicate element and False if it does not
    rand_list =[]
    for i in range (0,count):
        rand_list.append(random.randint(1,365))
    return hasduplicates(rand_list)


def probab(count, no):#Function to run no tests of count people
                      #Also to count the number of tests with duplicates
    nduplicates=0 #Initializing the duplicates to 0
    for i in range(0,no): #For loop to look at the range over no and keep a count of the number of tests with duplicates
        z = onetest(count)
        if z == True:
            nduplicates = nduplicates + 1 #Counting the number of duplicates (hasduplicates returns True) and incrementing

    bday_probability = nduplicates/no
    return bday_probability

 #Function that starts with a list of 2 elements and increases the number of elements in the list until the simulation shows a probability of 0.9
def main():

    NumberOfPeople =2
    no = 5000
    bday_probability=0
    while bday_probability < 0.9: #While loop to find the probablity as the number of people increases
        bday_probability=probab(NumberOfPeople, no)
        print("For" ,NumberOfPeople, "people, the probability of 2 birthdays is", bday_probability)
        NumberOfPeople = NumberOfPeople +1

main()

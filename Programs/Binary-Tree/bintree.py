#Program to implement a binary tree to count and sort the words in a file
#creating a root node
#This code defines Node Data Structure of a Tree
#This code opens a file and creates a binary tree

class Node: #creating the node class

    def __init__(self, data, count=1):#Function init_

        self.left = None #To initialise left node
        self.right = None #To initialise right node
        self.data = data #To initialise data
        self.count = count #no of times data is repeated

    def __str__(self):
        return str(self.data)+'('+str(self.count)+')' #Formatting of each component of the binary tree

def Tree_create(u, v): #To create the tree, with u and v as arguements

    if u.data < v: #Condition if the present node is lesser than the next one
        if u.right is None: #When there is no node on its right
            u.right = Node(v) #Printing of the 2nd node
        else:
            Tree_create(u.right, v) #If there is something on the right from before, recursion takes place
    elif u.data > v: #Just like the last one but on the left
        if u.left is None:#When there is no node on the left
            u.left = Node(v)
        else:
            Tree_create(u.left, v)#If there is something on the left from before, recursion takes place
    else:
        u.count += 1 #Its count increments by 1 everytime the word comes up


try:
    openFile=input("Enter the file name:") 
    file=open(openFile,"r") 
except: #Checking if the user enters a file which is not in the same directory
    print("This file is not there in the folder.")#To print this statement if the except block is run
    exit()

#file = open("alice.txt","r")
s = file.read() 

from string import punctuation #To remove special characters
character = list(punctuation) 
character.remove("_") 
character.append(" ") 
character.append("\n")

def List_tree(s, list1): #creates a list of the tree
    global z #Defining a as a global variable, so that it can be used outside this function as well
    l = [s]#Defining list1 
    for j in list1: #Starting another for loop
        list2 = []
        for item in l:#Another for loop inside this for loop
            list2.extend(item.split(j))#Splitting the variable j and to appending list2 
        l = list2
    return l 
z = List_tree(s,character)
while "" in z:
    z.remove("")#Removing "" in all places

def Tree_make(node, whitespaces): #To print the list created as a tree
    if node is not None: #Condition for when there is a node
        Tree_make(node.left, whitespaces+1) #Modifying the arguments of the final tree  
        print("  "*whitespaces + str(node))        Tree_make(node.right, whitespaces+1)



fNode = Node(z[0])
for i in range(1,len(z)): 
    Tree_create(fNode, z[i]) #creates the tree

Tree_make(fNode, 0) 

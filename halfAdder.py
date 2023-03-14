# Event: LCCS National Workshop 4
# Date: 2023
# Author: Professional Development Service for Teachers
# eMail: computerscience@pdst.ie
# Half-Adder in Python

#defining a function called halfAdder
def halfAdder(x,y):  #function takes in two parameters
    if x!=y:    #checks if x is not equal to y
        s = 1   #s assigned value of 1 if x is not equal to y
    else:
        s = 0   #if x equals y then s is assigned the value 0
    c = x & y     #& is AND operation 
    print("Inputs", x, "and", y, ": \t Sum=", s,"\t Carry=", c)

halfAdder(0,0)
halfAdder(0,1)
halfAdder(1,0)
halfAdder(1,1)  

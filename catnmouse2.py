# Event: LCCS National Workshop 4
# Date: 2023
# Author: Professional Development Service for Teachers
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate a simple cat and mouse model
# This is a variation on the catnmouse1.py program. Here ther is just have 1 room
# and the model is used to simulate and visualise multiple different scenarios.

import random
import matplotlib.pyplot as plt

#cat_gender = random.choice(["M", "F"])
cat_gender = input("Enter cat's gender 'M' or 'F': ")

mice_pop = [] # a list to keep track of the mice population
start = 0
x = [0, 1,2,3,4,5] # x-axis values

for i in range(1,10): # 9 simulations
    
    mice = 50 # set the initial population of mice
    mice_pop.append(mice)
    
    # randomise the escape rate
    mice_escape_rate = round(random.randint(1,20)/10, 1)
    
    # iterate 5 times for each mouse
    for j in range(5): # attacks
        # The mouse population is changed on every iteration
        mice = int(mice * mice_escape_rate)
        
        if cat_gender == "M":
            cat_aggression = random.randint(0,4)
        else: # Female cats tend to be better mousers than males
            cat_aggression = random.randint(5,9)
        cat_aggression = round(cat_aggression*0.1,1)
        mice -= int(mice * cat_aggression)
        
        mice_pop.append(mice)

    # plot the data for this simulation
    lbl_txt = "G:{} A:{} E:{}".format(cat_gender, cat_aggression, mice_escape_rate)
    plt.plot(x, mice_pop[start:start+6], label = lbl_txt)
    start+=6
    
print(mice_pop) # display the populations for every simulation

# Show the data in a graph
plt.xlabel('Iteration')
plt.ylabel('Mouse Population')
title_txt = "G=Gender; A=Aggression; E=Escape Rate"
plt.title(title_txt)
plt.legend()
plt.show()

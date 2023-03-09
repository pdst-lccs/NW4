# Event: LCCS National Workshop 4
# Date: 2023
# Author: Professional Development Service for Teachers
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate a simple cat and mouse model

import random
import matplotlib.pyplot as plt

# mice is used to hold the current population of mice in rooms 1 and 2
mice =  [100, 100] # these initial values could be random

# mice1 is a list used to store the populations in room 1 as the model is run
mice1 = [mice[0]] # initial population of mice in room 1

# mice2 is a list used to store the populations in room 2 as the model is run
mice2 = [mice[1]] # initial population of mice in room 2

# The behaviour of the model will depend on the aggression of the cat
# Female cats tend to be better mousers (i.e. more aggressive) than males
cat_aggression = 0.2 # default cat aggression(assume the cat is male)
cat_gender = input("Enter cat's gender 'M' or 'F': ")
print("Cat's gender:", cat_gender)
if cat_gender == "F":
    cat_aggression = 0.8

# Let the user decide how many mice will escape on each iteration
mice_escape_rate = int(input("Enter percentage mice escape rate [0-100] "))
mice_escape_rate = float(mice_escape_rate/100)

# Now run the model in 10 steps
for _ in range(10):

    # Randomly choose a room for the cat
    cat_in_room = random.choice(["R1", "R2"])
    #print(cat_in_room)

    # The mouse population is changed on every iteration (regardless of where the cat is)
    mice[0] = int(mice[0] * mice_escape_rate)
    mice[1] = int(mice[1] * mice_escape_rate)

    # reduce the mouse population in the room where the cat is
    if (cat_in_room == "R1"):
        mice[0] -= int(mice[0] * cat_aggression)
    elif (cat_in_room == "R2"):
        mice[1] -= int(mice[1] * cat_aggression)
        
    # Keep a record of the populations in both rooms
    mice1.append(mice[0])
    mice2.append(mice[1])

# Now plot the data
x = [i for i in range(len(mice1))] # this is our x-axis e.g. 1-10

fig, ax = plt.subplots()
ax.plot(x, mice1, label = "Mice Room 1")
ax.plot(x, mice2, label = "Mice Room 2")

ax.set_xlabel('Iteration')
ax.set_ylabel('Mouse Population')
title = "Cat Gender {}, Cat Aggression {}, Mice Escape Rate {}".format(cat_gender, cat_aggression, mice_escape_rate)
ax.set_title(title)

plt.legend()
plt.show()

# CONSIDER THE FOLLOWING QUESTIONS
# What could we use this model for?
# ... to explore the effect of cat gender (aggression) on mice populations
# ... to explore the effect of escape rates on mice populations

# Challenge
# Mofify the model so that the cat is unable to secure a definitive victory over the mouse, who,
# despite not being able to defeat the cat, is able to avoid capture

# How could we improve the model?
# In the current model the mouse population is decreased on every iteration
# regardless of which room the cat is in. This may be a bit unfair on the mice!
# We could modify the model to allow the mouse population to (sometimes) increase
# For example if the cat doesn't appear in the same room on two consecutive iterations
# we could increase the mouse population in that room by X%.
# (When the cat's away the mice will play!!)

# How could we extend the model?
# Prompt the user for the initial mouse population
# Add more rooms / ask the user how many rooms they want to model
# Just have 1 room and use the model to simulate multiple different scenarios. Graph the outcomes
# Add a second cat
# Introduce a dog!
# In the current model the moouse population decreases in every room on each iteration ...
# ... we could modify the model so that the population only decreases in rooms where the cat is
# ... i.e. make the model so that the outcomes vary from room to room
# We could introduce additional variables ... see below
# ... Cat-urine (can make mice harder to catch)
# The mere whiff of cat urine and litter is often enough to scare the mice away.
# According to research, mice are conditioned to turn in the opposite direction when they smell cat urine.
# ... The cat parasite Toxoplasma gondii is known to cause infected rodents to lose their
# fear of feline predators, which makes the mice much easier prey to catch.

# Lesson. By modelling a problem we are learning more about the real world
# (CT is looking at a problem through the prism of CS)

# See also ...
# Game of Cat and Mouse - Numberphile:
# https://www.youtube.com/watch?v=vF_-ob9vseM
# https://www.wired.com/story/the-best-way-for-a-mouse-to-escape-a-cat-according-to-math/

# https://www.geeksforgeeks.org/puzzle-cat-mice-and-4-boxes/
# https://www.microsoft.com/en-us/p/cat-vs-dog/9wzdncrfj0vw#activetab=pivot:overviewtab
# https://towardsdatascience.com/a-very-easy-tutorial-to-learn-python-objected-oriented-programming-through-ms-game-cat-vs-dog-967e229bd81e


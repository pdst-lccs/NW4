# Event: LCCS National Workshop 4
# Date: 2023
# Author: Adapted by Professional Development Service for Teachers
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate the use of simulation as a tool to ..
# .. investigate stay-switch strategies for the Monty Hall problem

import random

# The overal aim is to compute (and compare) these ...
stay_wins = 0 
switch_wins = 0

for _ in range(100000):
    doors = [0,0,0]
    prize_door = random.randint(0, 2)
    doors[prize_door] = 1
    #print("Prize behind door", prize_door)

    # Player picks a door - any door
    players_door = random.randint(0, 2)
    #print("Players door", players_door)

    # Host picks a door
    door_to_show = random.randint(0, 2)
    #print("Door to show", door_to_show)

    # Keep looping so that the host's door is neither the players door nor the prize door
    while door_to_show == players_door or door_to_show == prize_door: 
        door_to_show = random.randint(0, 2)
        #print("Door to show", door_to_show)

    if doors[players_door] == 1:
        stay_wins += 1

    # This is the clever bit!!
    switched_door = 3 - players_door - door_to_show # Explain!
    #print("Switched door", switched_door)
    if doors[switched_door] == 1:
        switch_wins += 1


print("Stay wins:", stay_wins)
print("Switch wins:", switch_wins)

# Possible challenges ...
# Give the user an option at the start to choose a strategy - stay or switch
# Plot the stay-switch results in a bar chart
# Implement the Monty Hall Game

# Event: LCCS National Workshop 4
# Date: 2023
# Author: Adapted from NCCA by Professional Development Service for Teachers
# eMail: computerscience@pdst.ie
# Purpose: A program to demonstrate a simple population
# This project aligns with population growth topic for Leaving Certificate Geography.
# The user will be asked to enter the ...
# ... population,start year, mortality rate, birth rate, migration rate, ...
# ...how much these rates change every year (currently as a constant rate of change) and ...
# ...how many years you want to model
# The program then generates a list of projected population estimates for each year.
# Fianlly a graph is generated to visualise the model output.

import matplotlib.pyplot as plt

print("This program models population growth.")
print("You will be asked to enter the 'current' population, start year, mortality rate, birth rate, migration rate, how much these rates change every year (currently as a constant rate of change) and how many years you want to model.")
print("The program then generates a list of projected population estimates for each year and graphs it for you to interpret.")

current_pop = int(input("what is the current population (thousands)? "))
start_year = int(input("what is the starting year? "))
current_death_rate =  float(input("what is the current death rate (per 1000 people)? "))
current_birth_rate =  float(input("what is the current birth rate (per 1000 people)? "))
current_migration_rate =  float(input("what is the net migration rate (per 1000 people)? "))

current_change_death_rate =  float(input("what is the projected change in death rate per year? "))
current_change_birth_rate =  float(input("what is the projected change in birth rate per year? "))
current_change_net_migration =  float(input("what is the projected change in migration rate per year? "))

num_years =  int(input("how many years do you want to model? "))

pop_list = [current_pop] # create list to collect each years projected population, for graphing later
year_list = [start_year] # create list to list each year, for graphing later

for x in range(0, num_years):
    # Model Calculation
    pop_list.append(pop_list[x] - (pop_list[x]*(current_death_rate/1000)) + \
                    (pop_list[x]*(current_birth_rate/1000)) + \
                    (pop_list[x]*(current_migration_rate/1000)))
    
    current_death_rate = current_death_rate + current_change_death_rate
    current_birth_rate = current_birth_rate + current_change_birth_rate
    current_migration_rate = current_migration_rate + current_change_net_migration
    year_list.append(year_list[x]+1)
    
    # Put it all togther for the user to read and generate outputted list
    print ("in the year " + str(year_list[x]) + \
           " the population will be " +  \
           str(pop_list[x]) + "000") 

# Now plot the data
x = [i for i in range(num_years)] # this is our x-axis e.g. 1-10

fig, ax = plt.subplots()
ax.plot(year_list, pop_list)
ax.set_xlabel('Year')
ax.set_ylabel('Population')
ax.set_title("Population Model")

plt.show()


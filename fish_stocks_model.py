import matplotlib.pyplot as pyplot
 
# A simple population model
initial_population = int(input("Enter the starting population: ")) # e.g. 4000000
years = int(input("Enter the number of years: ")) # e.g. 10 or 100
growth_rate = int(input("Enter the percentage growth rate: ")) # e.g. 8
growth_rate = growth_rate/100 
harvest = int(input("Enter the maximum annual harvest allowed: ")) # e.g. 1500

print("Year \t Population")
print("==== \t ==========")
population = initial_population
population_list = [ ]
population_list.append(initial_population)
for year in range(years):
    population = (1+growth_rate) * population - harvest
    population_list.append(population)
    print(year + 1, "\t", int(population))

print('The final population is %.2f' %population)

# Display the results graphically
pyplot.plot(range(years + 1), population_list)
pyplot.xlabel('Year')
pyplot.ylabel('Population')
pyplot.show()

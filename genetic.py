import random

def randomBits(bits):
    s = ""
    for i in range(bits):
        s += str(int(random.random()*2))
    return s

def generateInitialPopulation(no_of_pop, bits):
    pop = [randomBits(bits) for i in range(no_of_pop)]
    fit = [int(pop[i],2) for i in range(no_of_pop)]

    return pop, fit

def selection(pop, fit):
    mini = fit.index(min(fit))
    maxi = fit.index(max(fit))
    pop[mini] = pop[maxi]
    fit[mini] = fit[maxi]

    return pop, fit

def crossover(pop, fit, bits):
    crossPoint = int(bits/2)

    x = len(pop)
    if len(pop)%2:
        x = len(pop)-1

    for i in range(0, x, 2):
        temp = pop[i][:crossPoint] + pop[i+1][crossPoint:]
        pop[i+1] = pop[i+1][:crossPoint] + pop[i][crossPoint:]
        pop[i] = temp
        fit[i] = int(pop[i],2)
        fit[i+1] = int(pop[i],2)

    return pop, fit

def mutation(pop, fit, bits):
    for i in range(len(pop)):
        pop[i] = pop[i].replace('0', '1', 1)

    return pop, fit

####################################################################################################33

no_of_pop = int(input("Enter size of initial population: "))
bits = int(input("Enter size of bits: "))

# Initial population creation
pop, fitness = generateInitialPopulation(no_of_pop, bits)

print("\nInitial population:")
print(pop)
print(fitness)

# Stopping condition
maxPop = pow(2, bits)-1
generation = 0

if(maxPop == max(fitness)):
    print("Condition fullfilled!")
else:
    while(maxPop != max(fitness)):
        print("__________________________________________")
        
        # Perform selection
        pop, fitness = selection(pop, fitness)
        print("\nSelection:")
        print(pop)
        print(fitness)

        # Perform Crossover
        pop, fitness = crossover(pop, fitness, bits)
        print("\nCrossover:")
        print(pop)
        print(fitness)

        # Perform Mutation
        pop, fitness = mutation(pop, fitness, bits)
        print("\nMutation:")
        print(pop)
        print(fitness)

        print("Max fitness of generation (", generation, ") is ", max(fitness))
        generation += 1
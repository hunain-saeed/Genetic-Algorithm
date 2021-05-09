import random

def randomBits(bits):
    s = ""
    for i in range(bits):
        s += str(int(random.random()*2))
    return s

def generateInitialPopulation(no_of_pop, bits):
    pArr = [randomBits(bits) for i in range(no_of_pop)]
    fit = [int(pArr[i],2) for i in range(no_of_pop)]

    return pArr, fit

def selection(pop, fit):
    mini = fit.index(min(fit))
    maxi = fit.index(max(fit))
    pop[mini] = pop[maxi]
    fit[mini] = fit[maxi]

    return pop, fit

no_of_pop = int(input("Enter size of initial population: "))
bits = int(input("Enter size of bits: "))

# Initial population creation
pop, fitness = generateInitialPopulation(no_of_pop, bits)

print("Initial population: ", pop)
print("Fitness: ", fitness)

# Stopping condition
maxPop = pow(2, bits)-1
generation = 0

if(maxPop == max(fitness)):
    print("Condition fullfilled!")
else:
    while(maxPop != max(fitness)):
        # Perform selection
        pop, fitness = selection(pop, fitness)
        print(pop)
        print(fitness)


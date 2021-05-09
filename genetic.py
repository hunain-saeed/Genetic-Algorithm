import random

def randomBits(bits):
    s = ""
    for i in range(bits):
        s += str(int(random.random()*2))
    return s


def generateInitialPopulation(no_of_pop, bits):
    pArr = [randomBits(bits) for i in range(no_of_pop)]
    fit = [int(pArr[i],2) for i in range(no_of_pop)]
    
    print(pArr)
    print(fit)

    return pArr, fit




no_of_pop = int(input("Enter size of initial population: "))
bits = int(input("Enter size of bits: "))

pop, fitness = generateInitialPopulation(no_of_pop, bits)
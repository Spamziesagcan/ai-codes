import random

# Define multiple fitness functions
def fitness1(c):
    return int(c, 2) ** 2

def fitness2(c):
    return int(c, 2) * 3

# Dictionary for user to choose fitness function
fitness_functions = {
    "1": fitness1,
    "2": fitness2
}

# Modified to accept fitness as argument
def select(pop, fitness):
    return max(random.sample(pop, 2), key=fitness)

def crossover(p1, p2):
    pt = random.randint(1, len(p1)-1)
    return p1[:pt] + p2[pt:]

def mutate(c, rate):
    if random.random() < rate:
        i = random.randint(0, len(c)-1)
        c = list(c)
        c[i] = '1' if c[i] == '0' else '0'
        return ''.join(c)
    return c

def run_ga():
    print("Choose fitness function:")
    print("1: f(x) = x^2")
    print("2: f(x) = 3 * x")
    choice = input("Enter choice (1/2): ")

    fitness = fitness_functions.get(choice, fitness1)

    pop_size = int(input("Enter population size: "))
    gens = int(input("Generations: "))
    rate = float(input("Mutation rate (0-1): "))
    pop = [''.join(random.choice('01') for _ in range(5)) for _ in range(pop_size)]
    
    for g in range(gens):
        pop.sort(key=fitness, reverse=True)
        print(f"Gen {g+1}: Best = {pop[0]} (x = {int(pop[0], 2)}, f = {fitness(pop[0])})")
        new_pop = [pop[0]]
        
        while len(new_pop) < pop_size:
            c = crossover(select(pop, fitness), select(pop, fitness))
            c = mutate(c, rate)
            if c not in new_pop: 
                new_pop.append(c)

        pop = new_pop

# Run the genetic algorithm
run_ga()
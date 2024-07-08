

import random
import math

with open('input.txt') as f:
    lines = f.readlines()

n = int(lines[0])  
cities = []

for i in range(1, min(n+1, len(lines))):
    x, y, z = map(float, lines[i].split())
    cities.append((x, y, z))

  
POP_SIZE = 80
MAX_GENS = 500
ELITE_SIZE = 10
MUTATION_RATE = 0.2

def create_individual(cities):
    return random.sample(cities, len(cities))

def population_init(pop_size):
    population = []
    for i in range(pop_size):
        individual = create_individual(cities)
        population.append(individual)
    return population

def fitness(individual):
    distance = 0
    for i in range(len(individual)):
        city1 = individual[i]
        city2 = individual[(i+1) % len(individual)]
        dist = math.sqrt((city1[0] - city2[0])**2 + 
                         (city1[1] - city2[1])**2 +
                         (city1[2] - city2[2])**2)
        distance += dist
    fitness = 1/distance
    return fitness

def rank_population(population):
    fitnesses = []
    for individual in population:
        fitnesses.append(fitness(individual))
        
    ranked_pop = [x for _, x in sorted(zip(fitnesses, population), reverse=True)] 
    return ranked_pop

def selection(population):
    ranked_pop = rank_population(population)  
    p1, p2 = random.sample(ranked_pop[:50], 2)
    return p1, p2

def crossover(p1, p2):
    child1 = [] 
    child2 = []
    
    if len(p1) > 1: 
        pt1 = random.randint(0, len(p1)-2)
        pt2 = random.randint(pt1+1, len(p1)-1)
        
        child1 += p1[pt1:pt2]
        child2 += p2[pt1:pt2]

    p1_remaining = [gene for gene in p1 if gene not in child1]
    p2_remaining = [gene for gene in p2 if gene not in child2]

    child1 += p1_remaining 
    child2 += p2_remaining
    
    return child1, child2

def mutate(individual):
    i, j = random.sample(range(len(individual)), 2)
    individual[i], individual[j] = individual[j], individual[i]
    return individual

def elitism(population, offspring):
    combined_pop = population + offspring
    ranked_combined = rank_population(combined_pop)
    elite = ranked_combined[:ELITE_SIZE]
    return elite

def genetic_algorithm():
    population = population_init(POP_SIZE)
    best = None
    
    for gen in range(MAX_GENS):
        offspring = []
        for i in range(POP_SIZE//2):
            p1, p2 = selection(population)
            o1, o2 = crossover(p1, p2)
            o1 = mutate(o1)
            o2 = mutate(o2)
            offspring += [o1, o2]
        
        population = elitism(population, offspring)
        
        fitnesses = [fitness(i) for i in population]
        if best is None or fitnesses[0] > fitness(best):
            best = population[0]
            
    return best

best = genetic_algorithm()

# Print output
print(1/fitness(best))

for city in best:
    print(city[0], city[1], city[2])
    
print(best[0][0], best[0][1], best[0][2])


with open('output.txt', 'w') as f:

    f.write(str(1/fitness(best))+'\n')
    
    for city in best:
        f.write(str(int(city[0]))+' '+str(int(city[1]))+' '+str(int(city[2]))+'\n')

    f.write(str(int(best[0][0]))+' '+str(int(best[0][1]))+' '+str(int(best[0][2])))





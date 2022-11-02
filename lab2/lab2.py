import numpy as np
import random
from copy import copy
from time import time
from collections import namedtuple

PROBLEM_SIZE = 500 #problem size corresponds to N
POPULATION_SIZE = 100
OFFSPRING_SIZE = 20
SEED = 42
N_MAX_ITERATIONS = 10000


Individual = namedtuple("Individual", ["genome", "fitness"])
#each individual is a tuple in the form (genome, (number of coverd elements from 0 to N-1, -sum of elements in the lists))

def problem(PROBLEM_SIZE, seed=None):
    """Creates an instance of the problem without duplicate elements"""
    random.seed(seed)
    return list(sorted({
        tuple(set(random.randint(0, PROBLEM_SIZE - 1) for n in range(random.randint(PROBLEM_SIZE // 5, PROBLEM_SIZE // 2))))
        for n in range(random.randint(PROBLEM_SIZE, PROBLEM_SIZE* 5))
    }))

ALL_LISTS = problem(PROBLEM_SIZE, SEED) #list of tuples 
LIST_LEN = len(ALL_LISTS)

def fitness_function(genome: tuple):
    '''Returns a tuple (number_of_covered_elements, -weigth)'''
    num_covered_elements = set()
    weigth = 0
    for (i, list_) in enumerate(ALL_LISTS):
        if genome[i]:
            num_covered_elements.update(list_)
            weigth += len(list_)
    return len(num_covered_elements), -weigth

def select_parent(population, tournament_size = 2):
    '''tournaments are performed and the individual with the highest fitness is chosen'''
    return max(random.choices(population, k = tournament_size), key = lambda individual: individual.fitness) 

def single_mutation(genome: tuple):
    '''Fist mutation function: flips a single element'''
    index = random.randint(0, LIST_LEN-1)
    return genome[:index] + (not genome[index],) + genome[index+1:]

def multiple_mutations(genome: tuple):
    '''Second mutation function: flips a randomic number of elements'''
    n_mutations = np.random.poisson(lam= 2)
    for _ in range(n_mutations):
        genome = single_mutation(genome)
    return genome

def crossover(genome1: tuple, genome2: tuple):
    '''First crossover function: splits the parents in two and then combine first slice of one parent with the second slice of the other parent.
    randomly chooses also which parent to put first'''
    cut = random.randint(0, LIST_LEN-1)
    first_genome = random.randint(0,2) #chooses which parent to put first 
    
    if first_genome: #first_parent = 1
        return genome1[:cut] + genome2[cut:]
    else: #first_parent = 0
        return genome2[:cut] + genome1[cut:]   
    
def crossover_version2(genome1: tuple, genome2: tuple):
    '''Created a mask of size PROBLEM_SIZE and if the i-th element is True then we choose the i-th element of parent1 otherwise of parent2'''
    '''Aims at mixing the parents elements'''
    mask = [random.choice([True, False]) for _ in range(LIST_LEN)]
    genome = [genome1[index] if m else genome2[index] for index, m in enumerate(mask)]
    return tuple(genome)

def generate_population():
    '''Generation of the individuals'''
    population = list()
    random.seed(SEED)
    for genome in [tuple([random.choice([True, False]) for _ in range(len(ALL_LISTS))]) for __ in range(POPULATION_SIZE)]:
        population.append(Individual(genome, fitness_function(genome)))

    #sorting the population according first to the number of covered elements, then according to the weight 
    population = sorted(population, key = lambda individual: individual.fitness, reverse = True)
    fittest_individual = copy(population[0]) 
    return population, fittest_individual


def set_covering(crossover_type: callable, mutation_type: callable, mutation_rate = .5):
    '''Performs set_covering'''
    population, fittest_individual = generate_population()
    print(f"Initial fittest individual has fitness = {fittest_individual.fitness}")
    
    start = time()
    for number_iteration in range(N_MAX_ITERATIONS):
        offspring = list()
        for i in range(OFFSPRING_SIZE):

            parent1 = select_parent(population, tournament_size = 15)
            parent2 = select_parent(population, tournament_size = 15)
            new_individual = crossover_type(parent1.genome, parent2.genome) 
            
            if np.random.uniform() >= mutation_rate:
                new_individual = multiple_mutations(new_individual) #eventually applies mutation
                '''if random.uniform returns a value higher than mutation_rate, applies mutation.'''
                '''The lower mutation rate, the higher is the probability that the mutation is applied'''
                '''Higher mutation rates imply higher exploitation in the single_mutation case, whereas it implies higher exploration 
                in the multiple_mutation case'''

            new_individual = Individual(new_individual, fitness_function(new_individual))

            if fittest_individual.fitness < new_individual.fitness: #keeps track of the best found solution till now
                fittest_individual = copy(new_individual)
                #print(fittest_individual.fitness)

            offspring.append(new_individual)

        population += offspring
        population = sorted(population, key=lambda individual: individual.fitness, reverse=True)[:POPULATION_SIZE]
    
    end = time()
    print(f"Fittest individual in the population has fitness = {fittest_individual.fitness}, rate at which mutation if performed {(1-mutation_rate)*100}%")
    print(f"Time required = {end-start} ms")
    return population, fittest_individual
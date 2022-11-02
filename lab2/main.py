from lab2 import *
random.seed(SEED)

'''First tested function is the single mutation + half genome crossover'''
population, fittest_individual = set_covering(crossover_type = crossover, mutation_type= single_mutation)

'''Second tested versione is the multiple mutations + half genome crossover '''
population, fittest_individual = set_covering(crossover_type = crossover, mutation_type= multiple_mutations)

'''Third tested version is the single mutation + crossover performed with a mask'''
population, fittest_individual = set_covering(crossover_type = crossover_version2, mutation_type= single_mutation)

'''Fourth tested version is the multiple mutations + crossover performed with a mask '''
population, fittest_individual = set_covering(crossover_type = crossover, mutation_type= multiple_mutations)

'''Check for the mutation rate impact'''
mutation_rates = np.arange(.1, 1, .1)
for mr in mutation_rates:
    break

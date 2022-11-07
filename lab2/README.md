
# Lab2
The proposed solution for Lab2 is [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/lab2/lab2.ipynb)

## Expected results with SEED=42
Given the known issues the problem has been runned multiple times returning the following weights for the following parameters: 
- Population size = 50
- Offspring size = 20
- Max number of iterations = 3000
- Rate at which a mutation is performed = .5
- Rate at which the negation mutation is performed = .25
- Rate at which a single flip mutation is performed = .25

| PROBLEM_SIZE = 5  | PROBLEM_SIZE = 10 |  PROBLEM_SIZE = 100 | PROBLEM_SIZE = 500 | PROBLEM_SIZE = 1000 |
|:-------|:-------|:--------|:--------|:---------|
| 5      | 12     | 255     | 1732    | 3885     |

## Known issues
- For high values of the population_size, the computation starts to be expensive, maybe another problem representation is more efficient. 
- Multiple mutations instead than a single one might have a higher performance, but too computationally expensive.
- I did not only look for a population with distinct elements. 

## Collaboration
Collaboration with students:
- s302294
- s280117

## Yanking
- one-max.ipynb Professor Squillero [here](https://github.com/squillero/computational-intelligence/blob/master/2022-23/one-max.ipynb)

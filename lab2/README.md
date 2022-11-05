
# Lab2
The proposed solution for Lab2 is [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/lab2)

## Expected results with SEED=42
Given the known issues the problem has been runned multiple times returning the following weights for the following parameters: 
- Population size = 50
- Offspring size = 20
- Max number of iterations = 3000
- Rate at which a mutation is performed = .5
- Rate at which the negation mutation is performed = .25
- Rate at which a single flip mutation is performed = .25

| N = 5  | N = 10 |  N = 100 | N = 500 | N = 1000 |
|:-------|:-------|:--------|:--------|:---------|
| 5      | 12     | 255     | 1732    | 3885     |

## Known issues
For high values of the population_size, the computation starts to be expensive, maybe another problem representation is more efficient. 

## Collaboration
Collaboration with students:
- s302294
- s280117

## Yanking
- one-max.ipynb Professor Squillero [here](https://github.com/squillero/computational-intelligence/blob/master/2022-23/one-max.ipynb)

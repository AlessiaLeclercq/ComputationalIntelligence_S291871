
# Lab1
The proposed solution for Lab2 is divided in:
- Set of functions to be used [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/lab2/lab2.py)
- A main file to run for output [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/lab2/main.py)
Two crossover functions have been tested: 
- The first function randomply chooses a splitting index and an initial parent. Then, it constructs the new genome by combining the first part of the first parent with the second part of the second parent.
- The second function creates a mask over all possible sets and takes the elements of parent1 when the i-th element of the mask is True, otherwise it takes the element of the second parent. 
Also two mutation functions have been tested:
- The firast mutation function flips a randomly chosen element
- The second mutation function randomly chooses n flips to be performed and also randomly chooses for each of the N flips whether to change the element value or not

## Expected results with SEED=42
- N =

- N = 10

- N = 20

- N = 100

- N = 500

-N = 1000

## Known issues
Even though a seed has been imposed for reproducibility purposes, the exploration results are not always the same. Therefore, the one previously reported are the results of the last run and the output screenshot has been published [here]()

## Collaboration
Collaboration with students:
- s302294
- s280117

## Yanking
- one-max.ipynb Professor Squillero [here](https://github.com/squillero/computational-intelligence/blob/master/2022-23/one-max.ipynb)

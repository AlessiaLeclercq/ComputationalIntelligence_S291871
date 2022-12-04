Implementation of NIM using EA can be found [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/lab3/lab3.py). 
The algorithm uses three basic rules:
- Only a single heap $i$ presents at least two values, then with probability = 1: if the number of heaps is even, then it takes all objects but one from $i$; otherwise it takes the whole heap 
- With $P > threshold$ it tries to put/keep the number of non empty heaps to an even value
- With $P \leq threshold$ it tries to put all heaps $=$ 1
 
The $threshold$ is learned through 1000 iterations according to an (1,lambda) EA strategy with population size lambda = 20.

The algorithm has been trained against some adversaries:
- *random_player* which randomly chooses one row and a number of objects to delete from it
- *basic_player* which takes only one object from the largest row
- *nim_sum* implementation of a slightly modificed nim_sum strategy, which correctly performs nim_sum 70% of the times and the remaining 30% it behaves like the basic player
- *human_player* that enables the user to play against the game

Here the percentage of times it won against an adversary:

| ADVERSARY  | WINNING PERCENTAGE| STARTING THRESHOLD | LEARNED THRESHOLD |
|:-----------|:------------------|:-------------------|:------------------|
| random_player | 1.  |  .37 | .43 
| basic_player  | 1.  |  .37 | .37 
| nim_sum  30%  | .46 |  .37 | .20 

# YANKING 
Squillero rastrigin [here](https://github.com/squillero/computational-intelligence/blob/master/2021-22/rastrigin.ipynb) and nim [here](https://github.com/squillero/computational-intelligence/blob/master/2022-23/lab3_nim.ipynb)

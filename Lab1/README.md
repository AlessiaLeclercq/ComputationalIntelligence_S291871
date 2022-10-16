
# Lab1
The proposed solution for Lab1 is divided in:
- Set of functions to be used [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/Lab1/lab1.py)
- A main file to run for output [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/Lab1/main.py)

## Expected results with SEED=42
- N = 5
  > Breadth First total visited states 247, solution found in 3 steps
  > 
  > Depth First total visited states 53, solution found in 8 steps
  > 
  > Greedy total visited states 28, solution found in 3 steps
  > 
  > A* total visited states 151, solution found in 3 steps 

- N = 10
  > Breadth First total visited states 31579, solution found in 3 steps
  > 
  > Depth First total visited states 553, solution found in 16 steps
  > 
  > Greedy total visited states 124, solution found in 3 steps
  > 
  > A* total visited states 2197, solution found in 4 steps 

- N = 20
  > Breadth First total visited states 65649, solution found in 4 steps
  >
  > Depth First total visited states 568, solution found in 27 steps
  > 
  > Greedy total visited states 131, solution found in 4 steps
  > 
  > A* total visited states 54077, solution found in 5 steps

- N = 100 
  > Greedy total visited states 2126, solution found in 5 steps

## Known issues
From N = 100 too many states are visited and added to the frontier and any output is generated in acceptable time. 

## Collaboration with
- s302294
- s280117

## Yanking
- 8-puzzle.ipynb Professor Squillero [here](https://github.com/squillero/computational-intelligence/blob/master/2022-23/8-puzzle.ipynb)
- gx_utils.py Professor Squillero [here](https://github.com/squillero/computational-intelligence/blob/master/2022-23/gx_utils.py)

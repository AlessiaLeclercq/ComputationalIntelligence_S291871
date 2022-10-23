
# Lab1
The proposed solution for Lab1 is divided in:
- Set of functions to be used [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/lab1/lab1.py)
- A main file to run for output [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/lab1/main.py)

*NOTE: only those two files must be checked for the peer_review, see Update section for further explanatons*

## Expected results with SEED=42
- N = 5
  > Breadth First total visited states 247, solution found in 3 steps, cost = 5
  > 
  > Depth First total visited states 53, solution found in 8 steps, cost = 12
  > 
  > Greedy total visited states 28, solution found in 3 steps, cost = 6
  > 
  > A* total visited states 151, solution found in 3 steps, cost = 5 

- N = 10
  > Breadth First total visited states 31579, solution found in 3 steps, cost = 12
  > 
  > Depth First total visited states 553, solution found in 16 steps, cost = 47
  > 
  > Greedy total visited states 124, solution found in 3 steps, cost = 13
  > 
  > A* total visited states 2197, solution found in 4 steps, cost = 10

- N = 20
  > Breadth First total visited states 65649, solution found in 4 steps, cost = 31
  >
  > Depth First total visited states 568, solution found in 27 steps, cost = 147
  > 
  > Greedy total visited states 131, solution found in 4 steps, cost = 29
  > 
  > A* total visited states 54077, solution found in 5 steps, cost = 23

- N = 100 
  > Greedy total visited states 2126, solution found in 5 steps, cost = 188

## Known issues
From N = 100 too many states are visited and added to the frontier and any output is generated in acceptable time. 

## Collaboration
Collaboration with students:
- s302294
- s280117

## Yanking
- 8-puzzle.ipynb Professor Squillero [here](https://github.com/squillero/computational-intelligence/blob/master/2022-23/8-puzzle.ipynb)
- gx_utils.py Professor Squillero [here](https://github.com/squillero/computational-intelligence/blob/master/2022-23/gx_utils.py)

## Updates after the deadline (17/10/2022)
Loaded two new files with updates that have been made after the deadline. 
- Set of functions to be used [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/lab1/lab1_afterdeadline.py)
- A main file to run for output [here](https://github.com/AlessiaLeclercq/ComputationalIntelligence_S291871/blob/main/lab1/main_afterdeadline.py)

Updates have been made:
- Use of the original and not modifed problem function 
- Added two functions to transform the original list of lists into a frozenset of HashableArrays
- The frozen set is now sorted only once (at its creation) and not every time the possible_action function is called
- ALL_STATES has been renamed in ALL_ACTIONS according to peer review (23/10/2022)
- Use of np.arrays instead of sets to store values within an HashableArray. When I was using sets and running the code wit N>200 the following error message was displayed (solved with numpy arrays): 
> Traceback (most recent call last):
File "main.py", line 7, in <module>
  ALL_STATES = problem(N, SEED)
File "/home/aleclercq/Documents/Python/Computational_Intelligence/lab1.py", line 11, in problem
  return frozenset(HashableArray(set(
File "/home/aleclercq/Documents/Python/Computational_Intelligence/lab1.py", line 51, in hash
  return hash(bytes(self._data))
ValueError: bytes must be in range(0, 256)

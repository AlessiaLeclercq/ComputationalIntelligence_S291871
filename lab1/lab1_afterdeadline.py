import numpy as np
import random
import heapq
import logging

from typing import Callable

def problem(N, seed=None):
    random.seed(seed)
    return [
        list(set(random.randint(0, N - 1) for n in range(random.randint(N // 5, N // 2))))
        for n in range(random.randint(N, N * 5))
    ]

def transform(a):
	return(HashableArray(np.array(a)))

def transform_set(all_sets):
#function that given a list of lists returns a frozenset (immutable, hence hashable)
#of elements of type HashableArray (hash function is implemented)	
#lists are turned into np.arrays and stored in HashableArray._data
#sorted is required for reproducibility purposes, especially in the possible_actions function 	
	return sorted(frozenset(map(transform , all_sets)))

class PriorityQueue:
#priority queue implementation taken from prof. Squillero gx_utils.py
#for the frontier   
    def __init__(self):
        self._data_heap = list()
        self._data_set = set()

    def __bool__(self):
        return bool(self._data_set)

    def __contains__(self, item):
        return item in self._data_set

    def push(self, item, p=None):
        assert item not in self, f"Duplicated element"
        if p is None:
            p = len(self._data_set)
        self._data_set.add(item)
        heapq.heappush(self._data_heap, (p, item))

    def pop(self):
        p, item = heapq.heappop(self._data_heap)
        self._data_set.remove(item)
        return item


class HashableArray:
#Class used to represent a single set within the stat and overcome the unhashability problem of lists
#and np.ndarrays. 
#Same implementation of State class from 8-puzzle.ipynb prof. Squillero

    def __init__(self, data: np.array):
        self._data = data.copy()

    def __hash__(self):
        return hash(bytes(self._data))

    def __eq__(self, other):
        return bytes(self._data) == bytes(other._data)

    def __lt__(self, other):
        return bytes(self._data) < bytes(other._data)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self._data)

    def __len__(self): #not implemented in prof. Squillero's State function
        return len(self._data)

    @property
    def data(self):
        return self._data

    def copy_data(self):
        return self._data.copy()


def goal_test(state: frozenset, N):
#reads the data and adds the Hashablearrays values in the goal_set
#then checks whether the goal_set has lenght N (all values have been added)
	goal_set = set()
	for list_ in state:
		goal_set.update(list_._data)  
	return len(goal_set) == N


def is_valid(state: frozenset, action: HashableArray):
#is_valid returns True if the action is not already in the state, otherwise False
    return action not in state

def possible_actions(state: frozenset, ALL_ACTIONS: frozenset): 
#possible_actions returns all actions that are not already present in the State    
    return (action for action in ALL_ACTIONS if is_valid(state, action))

def result(state: frozenset, action: HashableArray):
#result returns a new state in which the action is added 
	return state.union(frozenset([action]))

def h(state: frozenset, N):
#heuristic function returns how many elements are missing to reach the solution
#work as goal_test except for the returned result
	element_set = set()
	for array_ in state:
		element_set.update(array_._data)
	return N-len(element_set)

#search function from 8-puzzle.ipynb professor Squillero with added parameters (ALL_STATES, N)
def search(
    initial_state: frozenset,
    ALL_ACTIONS : frozenset,
    N : int, 
    goal_test: Callable,
    parent_state: dict,
    state_cost: dict,
    priority_function: Callable,
    unit_cost: Callable,
):
    frontier = PriorityQueue()
    parent_state.clear()
    state_cost.clear()

    state = initial_state
    parent_state[state] = None
    state_cost[state] = 0

    while state is not None and not goal_test(state, N):
        for a in possible_actions(state, ALL_ACTIONS):
            new_state = result(state, a)
            cost = unit_cost(a)
            if new_state not in state_cost and new_state not in frontier:
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                frontier.push(new_state, p=priority_function(new_state))
                logging.debug(f"Added new node to frontier (cost={state_cost[new_state]})")
            elif new_state in frontier and state_cost[new_state] > state_cost[state] + cost:
                old_cost = state_cost[new_state]
                parent_state[new_state] = state
                state_cost[new_state] = state_cost[state] + cost
                logging.debug(f"Updated node cost in frontier: {old_cost} -> {state_cost[new_state]}")
        if frontier:
            state = frontier.pop()
        else:
            state = None

    path = list()
    s = state
    while s:
        path.append(s.copy())
        s = parent_state[s]
    print(f"Solution N = {N} found in {len(path)} steps; visited {len(state_cost)} states, cost = {state_cost[state]}")
    return list(reversed(path))

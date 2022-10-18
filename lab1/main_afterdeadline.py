from lab1 import * 

N = 100
SEED = 42
random.seed(SEED)

ALL_STATES = transform_set(problem(N, SEED))
INITIAL_STATE = frozenset()

parent_state = dict()
state_cost = dict()

#BREADTH FIRST
print("Breadth First")
final = search(
    INITIAL_STATE,
    ALL_STATES,
    N,
    goal_test=goal_test,
    parent_state=parent_state,
    state_cost=state_cost,
    priority_function=lambda s: len(state_cost),
    unit_cost=lambda a: len(a),
)

#DEPTH FIRST 
print("Depth First")
final = search(
    INITIAL_STATE,
    ALL_STATES,
    N, 
    goal_test=goal_test,
    parent_state=parent_state,
    state_cost=state_cost,
    priority_function=lambda s: -len(state_cost),
    unit_cost=lambda a: len(a)
)


#GREEDY
print("Greedy")
final = search(
    INITIAL_STATE,
    ALL_STATES,
    N,
    goal_test=goal_test,
    parent_state=parent_state,
    state_cost=state_cost,
    priority_function=lambda s: h(s, N),
    unit_cost=lambda a: len(a)
)


#A*
print("A*")
final = search(
    INITIAL_STATE,
    ALL_STATES,
    N,
    goal_test=goal_test,
    parent_state=parent_state,
    state_cost=state_cost,
    priority_function=lambda s: state_cost[s] + h(s, N),
    unit_cost=lambda a: len(a),
)



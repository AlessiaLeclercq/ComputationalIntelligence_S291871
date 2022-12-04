import numpy as np
import random

from operator import xor
from functools import reduce
from collections import namedtuple 

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

Nimy = namedtuple("Nimy", ['row', 'value'])
Individual = namedtuple("Individual", ['percentage', 'threshold'])


class Nim:
	def __init__(self, n_rows):
		self._board = [Nimy(i, i*2+1) for i in range(n_rows)] 
		self._largest = self._board[-1]
		self._smallest = self._board[0]

	def update(self):
		'''updates its content variables'''
		self._board = [heap for heap in self._board if heap.value > 0]
		if self._board:
			self._largest = max(self._board, key = lambda heap: heap.value)
			self._smallest = min(self._board, key = lambda heap: heap.value)

	def nim_print(self):
		'''prints the board'''
		for heap in self._board:
			print (heap.row, heap.value)
		print("\n")

	def get_heap(self, row: int):
		'''gets the heap location and returns the heap'''
		for heap in self._board:
			if heap.row == row:
				return heap
		return ()

	def nimming(self, move: Nimy):
		'''performs the change'''
		heap = self.get_heap(move.row)
		assert heap.value >= move.value
		self._board[self._board.index(heap)] = Nimy(heap.row, heap.value - move.value)


#ADVERSARIES FUNCTIONS
def compute_nim_sum(board : list):
	'''performs bitwise xor'''
	return reduce(xor, [heap.value for heap in board])

def nim_sum(nim: Nim):
	'''Implementation of nim sum'''
	x = compute_nim_sum(nim._board)
	if random.random() > 0.3:
		if x > 0:
			for heap in nim._board:
				bit_xor = x^heap.value
				if bit_xor < heap.value:
					nim.nimming(Nimy(heap.row, heap.value - bit_xor))
					return nim

	nim.nimming(Nimy(nim._largest.row, 1))
	return nim 


def human_player(nim):
	'''mimics the human player (input is <row> <how many elements to remove>)'''
	move = input()
	row, value = (int(move.split(" ")[0]), int(move.split(" ")[1]))
	nim.nimming(Nimy(row, value))
	return nim

def random_player(nim):
	'''pure random strategy'''
	heap = random.choice(nim._board)
	num_objects = random.randint(1, heap.value)
	nim.nimming(Nimy(heap.row, num_objects))
	return nim

def basic_player(nim):
	'''player which only takes len - one from largest row'''
	nim.nimming(Nimy(nim._largest.row, nim._largest.value - 1))	
	return nim

#RULE FOR EVOLUTIONARY ALGORITHM 
def rule_tested(nim: Nim, thresh: float):
	'''Rule chosen to be evolved'''
	non_ones = [heap for heap in nim._board if heap.value > 1]

	if len(non_ones) == 1:
		if len(nim._board) % 2 == 0:
			nim.nimming(Nimy(non_ones[0].row, non_ones[0].value-1))
		else: 
			nim.nimming(Nimy(non_ones[0].row,  non_ones[0].value))
		return nim

	if non_ones and random.random() > thresh:
		#tries to put to one all values
		smallest_heap = min(non_ones, key = lambda heap: heap.value)
		nim.nimming(Nimy(smallest_heap.row, smallest_heap.value-1))

	else: 
		#if number of rows is even, takes a random value from the largest row
		if len(nim._board)%2==0:
			value = max(1, random.choice(range(nim._largest.value)))
			nim.nimming(Nimy(nim._largest.row, value))
		#if number of rows is odd, takes everything from the lowest row
		else:
			nim.nimming(Nimy(nim._smallest.row, nim._smallest.value))

	return nim 


def play_game(games, n_games, thresh, p=0):
	'''performs n_games between my function and the adversarial one and return the number of time my function wins. p parameter only to say whether to printo or not the board when playing''' 
	
	player = random.choice([0,1])
	count = 0

	for game_iteration in range(n_games):
		nim = Nim(5)

		#games is always games[0] = adversary function, games[1] = function to be tested
		while(nim._board):
			#printing instruction
			if p:
				nim.nim_print()
			#perform move according to current player	
			if player:
				nim = games[player](nim, thresh)
			else: 
				nim = games[player](nim)
			#update internal parameters
			nim.update()
			#update the turn
			player = 1-player

		#if player 1 (test function) wins
		if 1-player == 1:
			count += 1
			if(p==1):
				print("Algorithm Wins")


	return count/n_games

if __name__ == "__main__":
	#idea is to tweak the threshold
	size_population = 20

	#initial value for sigma
	current_thr = np.random.random()
	print(f"starting = {current_thr:.2f}")
	tweak_value = .05
	n_games = 100
	n_updates = 1000

	games = [basic_player, rule_tested]
	history = []

	#set intial best performing
	result = play_game(games, n_games, current_thr)
	best = Individual(result, current_thr)
	overall_best = Individual(result, current_thr)

	for update in range(n_updates):
		#generate tweaks for the threshold:
		threshold_values = np.random.uniform(low = max(0, current_thr - tweak_value), high = min(1, current_thr + tweak_value), size = (size_population,))
		
		population = []

		#compute for every threshold value the percentage of times my function wins
		for thr in threshold_values:
			population.append(Individual(play_game(games, n_games, thr), thr))		

		#1,lambda strategy 	
		best = max(population)
		current_thr = best.threshold
		history.append(best)

		#allow for exploration 
		if update>0 and update%100==0:
			if max(history[-20:]).percentage - min(history[-20:]).percentage < 0.1:
				current_thr = np.random.choice([current_thr*0.1, current_thr + 0.5, current_thr + 0.8])


		#store global max
		if best.percentage > overall_best.percentage:
			overall_best = best


	print(history)
	print(f"Played against random, fitness: {overall_best.percentage:.2f} threshold = {overall_best.threshold:.2f} ")
	
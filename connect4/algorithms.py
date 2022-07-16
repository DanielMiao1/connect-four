# -*- coding: utf-8 -*-
import math
import random


class MonteCarlo:
	def __init__(self):
		self.outcomes = {}
		self.visits = {}
		self.tree = {}

	@staticmethod
	def make_legal_moves(board):
		if board.terminal:
			return set()
		return {board.make_move(board, i) for i in board.legal_moves(board)}

	@staticmethod
	def make_random_move(board):
		if board.terminal:
			return None
		return board.make_move(board, random.choice(board.legal_moves(board)))

	@staticmethod
	def evaluate(board):
		if board.turn is (not board.winner):
			return 0
		return 0.5

	def choose(self, node):
		if node not in self.tree:
			return MonteCarlo.make_random_move(node)

		def score(n):
			if self.visits[n] == 0:
				return float("-inf")
			return self.outcomes[n] / self.visits[n]

		return max(self.tree[node], key=score)

	def rollout(self, node):  # TEMP node is __init__/Game object (not main/Game)
		path = self.select(node)
		leaf = path[-1]
		self.expand(leaf)
		outcome = self.simulate(leaf)
		self.backpropagate(path, outcome)

	def select(self, node, path=None):  # TEMP node is __init__/Game object (not main/Game)
		"""TEMP
		Selection algorithm for MCTS:
		on first run (when tree is empty), should return (path variable) a single-element array with the root node provided to begin expansion, which makes all possible moves of depth=1; this allows for later runs of select to select, based on the UCT algorithm, the best move of depth=2 for further expansion.
		"""
		# TEMP recursive function, path is used to track path array
		if path is None:
			path = []  # TEMP initialize path
		path.append(node)  # TEMP add current move to path
		if node not in self.tree or not self.tree[node]:  # TEMP if the node is a leaf (is not in tree or does not have any children)
			return path
		unexplored = self.tree[node] - self.tree.keys()
		if unexplored:
			path.append(unexplored.pop())
			return path
		return self.select(self.uct(node), path)  # TEMP select next node for recursion using UCT

	def expand(self, node):
		"""TEMP
		Expansion algorithm for MCTS:
		should add all children of the given node to the tree, if not already done
		[this is literally two lines that can be shortened into 1 line which can be shorted into 0 by using function header/body on the same line: `def expand(self, node): return [((self.tree[node] := MonteCarlo.make_legal_moves(node)) if node not in self.tree else None), None][1]' (this will probably not work as walruses on dictionary values probably dont exist)]
		"""
		if node not in self.tree:
			self.tree[node] = MonteCarlo.make_legal_moves(node)

	@staticmethod
	def simulate(node, invert=True):
		"""TEMP
		Simulation algorithm for MCTS:
		should simulate a random playout of the game, starting at `node' to a terminal node
		an `invert' variable keeps track of whether the current player is favorable (if the currently playing player is actually the opponent. If so, invert the outcome if necessary)
		"""
		if node.terminal:  # TEMP if the current node is a terminal node (if the current game state indicates that the game has concluded)
			outcome = MonteCarlo.evaluate(node)   # TEMP retrieve outcome of the game using a simple evaluation function defined in algorithms.py, returning 0.5 for ties, or 0 for losses. The evaluation function does not account for wins, as the invert parameter of the current function does that
			# TEMP return the outcome, inverting the result if necessary
			if invert:
				return 1 - outcome
			return outcome
		return MonteCarlo.simulate(MonteCarlo.make_random_move(node), not invert)  # TEMP if the current node is not a terminal/leaf, continue the simulation on a random next-move and toggle the invert variable as it is now the opponent's turn

	def backpropagate(self, path, outcome):
		"""TEMP
		Backpropagation:
		using the PATH of the SELECTION algorithm and the OUTCOME of the SIMULATION, update every node in the path to reflect the outcome
		this is completed using the `self.visits' dictionary (defined in the MonteCarlo.__init__ constructor function) and the `self.outcomes' dictionary, which keep track of the number of visits for each game state, and the outcome of each game state, respectively
		the two dictionary should have identical keys that point to a specific game state stored in memory (which is why over 500MB memory is used on move 7)
		the for loop in this function initializes each key-value pair in the dictionaries if it is not already, and puts the correct value there
		both dictionaries are cumulative (see choose function for how that works, which is basically dividing the outcome by the visits to obtain the average value. HOWEVER, this divisive approach certainly has some flaws, as low visit counts can bias the result, which could be addressed by adding a slight visits variable to the final result for each game-state so the engine slightly prefers moves that have been explored more thoroughly)
		"""
		for node in path[::-1]:  # TEMP iterate through each node of the path, in reverse order (for inverse operations (line with `outcome = 1 - outcome') to be effective)
			# TEMP append value to `visits' dictionary
			if node in self.visits:  # TEMP if the value has already been initialized in the dictionary, simply increment the existing value by 1
				self.visits[node] += 1
			else:  # TEMP otherwise, create a new key-value pair in the dictionary (notice the key is `node', a variable representing the game state) with the value set to 1 to represent that the node only has one visit
				self.visits[node] = 1
			# TEMP append value to `outcomes' dictionary
			if node in self.outcomes:  # TEMP same as appending value to the `self.visits' dictionary. Note the cumulative quality that also exists in the `self.outcomes' dictionary, and the key (`node') that is the same with the `self.visits' dictionary
				self.outcomes[node] += outcome
			else:
				self.outcomes[node] = outcome
			outcome = 1 - outcome  # TEMP invert the outcome to compensate for the opponent's (or the other player's) turn

	def uct(self, node):
		"""TEMP
		UCT selection algorithm
		[just search it up]
		"""
		log = math.log(self.visits[node])
		return max(self.tree[node], key=lambda n: (self.outcomes[n] / self.visits[n]) + (2 * math.sqrt(log / self.visits[n])))
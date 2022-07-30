# -*- coding: utf-8 -*-
import math
import random

class Node:
	def __init__(self, board=None, value=0, visits=1):	
		self.board = board
		self.children = []
		self.visits = visits
		self.value = value

class MonteCarlo:
	def __init__(self):
		self.tree = Node()

	def mcts(self, node, simulation_count):
		"""
		`simuation_count' iteration(s) of MCTS
		"""
		for _ in range(simulation_count):
			path = self.select(node)
			leaf = path[-1]
			self.expand(leaf)
			outcome = self.simulate(leaf)
			self.backpropagate(path, outcome)

	@staticmethod
	def evaluate(board):
		if bool(board.turn - 1) == board.winner:
			return 0
		return 0.5

	def choose(self, node):
		# if node not in self.tree:
		# 	return MonteCarlo.make_random_move(node)

		def score(n):
			if n.visits == 0:
				return float("-inf")
			return (n.outcome / n.visits)

		return max(node.children, key=score)

	def select(self, node):
		'''Return the path from initial position to leaf node based on UCT'''
		path = [node]
		
		while node.children:
			node = self.uct(node)
			path.append(node)

		return path
	
  # node.child.add(new_node)
	def expand(self, leaf_node):
		'''Expand the tree by a single node'''
		new_node = Node(MonteCarlo.make_random_move(node), 0, 0)
		leaf_node.children.append(new_node)

	@staticmethod
	def simulate(node, invert=True):
		if node.board.terminal:
			outcome = MonteCarlo.evaluate(node.board)
			if invert:
				return 1 - outcome
			return outcome
		return MonteCarlo.simulate(MonteCarlo.make_random_move(node.board), not invert)

	def backpropagate(self, path, outcome):
		for node in path[::-1]:
			node.visits += 1
			node.outcome += outcome
			outcome = 1 - outcome

	def uct(self, node):
		log = math.log(self.visits[node])
		return max(node, key=lambda n: (n.outcomes / n.visits) + (2 * math.sqrt(log / n.visits)))

	@staticmethod
	def make_random_move(board):
		if board.terminal:
			return None
		return board.make_move(board, random.choice(board.legal_moves(board)))
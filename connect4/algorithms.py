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
			return node.make_random_move()

		def score(n):
			if self.visits[n] == 0:
				return float("-inf")
			return self.outcomes[n] / self.visits[n]

		return max(self.tree[node], key=score)

	def rollout(self, node):
		path = self.select(node)
		leaf = path[-1]
		self.expand(leaf)
		outcome = self.simulate(leaf)
		self.backpropagate(path, outcome)

	def select(self, node, path=None):
		if path is None:
			path = []
		path.append(node)
		if node not in self.tree or not self.tree[node]:
			return path
		unexplored = self.tree[node] - self.tree.keys()
		if unexplored:
			path.append(unexplored.pop())
			return path
		return self.select(self.uct(node), path)

	def expand(self, node):
		if node not in self.tree:
			self.tree[node] = MonteCarlo.make_legal_moves(node)

	@staticmethod
	def simulate(node, invert=True):
		if node.terminal:
			outcome = MonteCarlo.evaluate(node)
			if invert:
				return 1 - outcome
			return outcome
		return MonteCarlo.simulate(MonteCarlo.make_random_move(node), not invert)

	def backpropagate(self, path, outcome):
		for node in path[::-1]:
			if node in self.visits:
				self.visits[node] += 1
			else:
				self.visits[node] = 1
			if node in self.outcomes:
				self.outcomes[node] += outcome
			else:
				self.outcomes[node] = outcome
			outcome = 1 - outcome

	def uct(self, node):
		log = math.log(self.visits[node])
		return max(self.tree[node], key=lambda n: (self.outcomes[n] / self.visits[n]) + (2 * math.sqrt(log / self.visits[n])))
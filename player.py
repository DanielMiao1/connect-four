# -*- coding: utf-8 -*-

import random


class Player:
	def __init__(self, color, board):
		self.color = color
		self.board = board

	def get_player_move(self):
		while True:
			try:
				column = int(input())
			except ValueError:
				print("Invalid input")
				continue
			if self.board.board.is_column_valid(column):
				break
			print("Invalid input")
		return column


class HumanPlayer(Player):
	pass
	

class AIPlayer(Player):
	def get_player_move(self):
		return self.minimax()

	def minimax(self, *_):
		return random.choice(self.board.moves())  # (temporary)

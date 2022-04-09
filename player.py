# -*- coding: utf-8 -*-

import random

from typing import *

from board import Board


class Player:
	def __init__(self, color: int, board: Board) -> None:
		self.color = color
		self.board = board

	def get_player_move(self, invalid: bool = False) -> Union[int, Literal["u"]]:
		try:
			column = input(f"[%s] > " % ("\033[91mInvalid input\033[0m" if invalid else "Enter your move"))
			if column.lower() in ["u", "undo"]:
				return "u"
			column = int(column)
		except ValueError:
			print("\033[91mInvalid input\033[0m")
			return False
		if self.board.is_column_valid(column):
			return column
		print("\033[91mInvalid input\033[0m")
		return False


class HumanPlayer(Player):
	pass
	

class AIPlayer(Player):
	def get_player_move(self):
		result = self.minimax(2, self.color)[0]
		if result is None:
			return random.choice(self.board.legal_moves()) + 1
		return result
	
	def minimax(self, depth, player, maximizing=True):
		move = None

		if depth == 0:
			return move, self.board.evaluate()
		elif self.board.is_game_over():
			return move, self.board.evaluate()
		
		base = -2 if maximizing else 2
		for i in self.board.legal_moves():
			self.board.place_move(i + 1)
			_, evaluation = self.minimax(depth - 1, player, not maximizing)
			self.board.undo()
			if (maximizing and base < evaluation) or (not maximizing and base > evaluation):
				base = evaluation
				move = i + 1
		return move, base


# empty spaces

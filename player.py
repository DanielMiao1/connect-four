# -*- coding: utf-8 -*-

import random

import time

from typing import *

from board import Board


class Player:
	def __init__(self, color: int, board: Board) -> None:
		self.color = color
		self.board = board

	def get_player_move(self, invalid: bool = False) -> Union[int, Literal["u"]]:
		try:
			column = input(f"[%s] > " % ("\033[91mInvalid input\033[0m" if invalid else "Enter your move"))
			if column.lower().startswith("row"):
				# row player_number n
				print(self.board.get_n_in_a_row(int(column.split()[1]), int(column.split()[2])))
				time.sleep(3)
				return False
			if column.startswith("e"):
				print(self.board.evaluate())
				time.sleep(1.5)
				return False
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
		result = self.minimax(3, self.color)[0]
		if result is None:
			return random.choice(self.board.legal_moves()) + 1
		return result
	
	def minimax(self, depth: int, player: int, maximizing: bool=True) -> tuple:
		move = None

		if depth == 0:
			return move, self.board.evaluate()
		elif self.board.is_game_over():
			return move, self.board.evaluate()
		
		base = float("-inf") if maximizing else float("inf")
		for i in self.board.legal_moves():
			self.board.place_move(i + 1)
			_, evaluation = self.minimax(depth - 1, player, not maximizing)
			self.board.undo()
			if (maximizing and base < evaluation) or (not maximizing and base > evaluation):
				base = evaluation
				move = i + 1
		return move, base



	# inf if red won, negative inf if yellow won

	# 3 * (# of 3 red in a row) 2 * (# of 2 red in a row) - [3 * (# of 3 yellow in a row) 2 * (# of 2 yellow in a row)]

# empty spaces
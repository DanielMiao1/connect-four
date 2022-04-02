# -*- coding: utf-8 -*-

import time
import random
from typing import *


class Player:
	def __init__(self, color: int, board: object) -> None:
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
	# everything here is temporary
	def get_player_move(self):
		time.sleep(2 + random.uniform(0, 1))
		return self.minimax()

	def minimax(self, *_: Any):
		return random.choice(self.board.moves())

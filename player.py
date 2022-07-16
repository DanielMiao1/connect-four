# -*- coding: utf-8 -*-
import random

import time



class Player:
	def __init__(self, color, board) -> None:
		self.color = color
		self.board = board

	def get_player_move(self, invalid: bool = False):
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
		if column in self.board.legal_moves():
			return column
		print("\033[91mInvalid input\033[0m")
		return False


class HumanPlayer(Player):
	pass
	

class AIPlayer(Player):
	def get_player_move(self):
<<<<<<< HEAD
		result = self.board.minimax_algorithm(4, self.color)[0]
		if result is None:
			return random.choice(self.board.legal_moves())
		return result
=======
		for _ in range(5000):
			self.board.tree.rollout(self.board.board)
		return self.board.tree.choose(self.board.board)
>>>>>>> parent of 689b4ed (patched monte carlo tree search algorithm)

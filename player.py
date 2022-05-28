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
		if column in self.board.legal_moves():
			return column
		print("\033[91mInvalid input\033[0m")
		return False


class HumanPlayer(Player):
	pass
	

class AIPlayer(Player):
	def get_player_move(self):
		start = time.time()
		result = self.board.minimax_algorithm(4, self.color)[0]
		print(time.time() - start)
		print(result)
		# 4.55299186706543 4.525663375854492 4.262247323989868 4.2896504402160645
		time.sleep(3)
		if result is None:
			return random.choice(self.board.legal_moves())
		return result

	
	'''
	def minimax(self, depth: int, player: int, maximizing: bool=True, alpha: Union[float, int] = float("-inf"), beta: Union[float, int] = float("inf")) -> tuple:
		"""
		The Minimax Algorithm
		:param depth: the depth of the search tree
		"""
		move = None

		# reached terminal node or cut off search
		if depth == 0:
			return move, self.board.evaluate()
		elif self.board.is_game_over():
			return move, self.board.evaluate()

		# set base evaluation
		base = float("-inf") if maximizing else float("inf")

		# iterate through legal moves
		for i in self.board.legal_moves():
			# get evaluation of move
			self.board.place_move(i + 1)
			_, evaluation = self.minimax(depth - 1, player, not maximizing, alpha, beta)
			self.board.undo()

			# update the evaluation and best move if needed
			if (maximizing and base < evaluation) or (not maximizing and base > evaluation):
				base = evaluation
				move = i + 1

			# maximizing player
			# if maximizing:
			# 	if evaluation > beta:
			# 		continue
			# 	alpha = max(evaluation, alpha)
				
			# # minimizing player
			# else:
			# 	if evaluation < alpha:
			# 		continue
			# 	beta = min(evaluation, beta)

		return move, base
	00000111111222222333333444444555555666666
00000111111222222333333444444555555666666
00000111111222222333333444444555555666666
00000111111222222333333444444555555666666
00000111111222222333333444444555555666666
10000011111222222333333444444555555666666
10000011111222222333333444444555555666666
10000011111222222333333444444555555666666
10000011111222222333333444444555555666666
10000011111222222333333444444555555666666
10000011111222222333333444444555555666666
20000011111122222333333444444555555666666
20000011111122222333333444444555555666666
20000011111122222333333444444555555666666
20000011111122222333333444444555555666666
20000011111122222333333444444555555666666
20000011111122222333333444444555555666666
30000011111122222233333444444555555666666
30000011111122222233333444444555555666666
30000011111122222233333444444555555666666
30000011111122222233333444444555555666666
30000011111122222233333444444555555666666
30000011111122222233333444444555555666666
40000011111122222233333344444555555666666
40000011111122222233333344444555555666666
40000011111122222233333344444555555666666
40000011111122222233333344444555555666666
40000011111122222233333344444555555666666
40000011111122222233333344444555555666666
50000011111122222233333344444455555666666
50000011111122222233333344444455555666666
50000011111122222233333344444455555666666
50000011111122222233333344444455555666666
50000011111122222233333344444455555666666
50000011111122222233333344444455555666666
60000011111122222233333344444455555566666
60000011111122222233333344444455555566666
60000011111122222233333344444455555566666
60000011111122222233333344444455555566666
60000011111122222233333344444455555566666
60000011111122222233333344444455555566666
	'''
	# def minimax(self, depth: int, player: int, maximizing: bool=True) -> tuple:
	# 	move = None

	# 	if depth == 0:
	# 		return move, self.board.evaluate()
	# 	elif self.board.is_game_over():
	# 		return move, self.board.evaluate()
		
	# 	base = float("-inf") if maximizing else float("inf")
	# 	for i in self.board.legal_moves():
	# 		# 
	# 		print(i, end="")
	# 		self.board.place_move(i)
	# 		_, evaluation = self.minimax(depth - 1, player, not maximizing)
	# 		self.board.undo()
	# 		if (maximizing and base < evaluation) or (not maximizing and base > evaluation):
	# 			base = evaluation
	# 			move = i
	# 	print()
	# 	return move, base

# if it's the maximizing player's turn, then out possible choices for minimizing player,
# if current move for minimizing player > beta, then don't consider that move
# if it's the minimizing player's turn, then out possible choices for maximizing player,
# if current move for maximizing player < alpha, then don't consider that move
# 

# for each of the possible moves:
# maximizing player:
# set alpha variable to highest scoring move so far

# minimizing player:
# set beta variable to lowest scoring move so far

		
	# inf if red won, negative inf if yellow won

	# 3 * (# of 3 red in a row) 2 * (# of 2 red in a row) - [3 * (# of 3 yellow in a row) 2 * (# of 2 yellow in a row)]

# empty spaces

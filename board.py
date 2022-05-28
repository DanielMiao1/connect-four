# -*- coding: utf-8 -*-

import typing


VALUES = ["    ", "\033[31m ◉  \033[0m", "\033[93m ◉  \033[0m"]


class Board:
	"""The grid."""
	def __init__(self, size: typing.List[int], connect_size: int):
		self.board = [[0 for _ in range(size[0])] for _ in range(size[1])]  # Possible values in board: 0 (empty), 1 (red), or 2 (yellow)
		self.moves = []  # List of moves made
		# self.board = [[random.randint(0, 2) for _ in range(size[1])] for _ in range(size[0])]  # Populate the board with random values
		self.size = size
		self.turn = 1  # 1 for red, 2 for yellow
		self.connect_size = connect_size
		
	def visualize_board(self):
		"""Returns a formatted string representing the board."""
		board_rows = [[] for _ in range(self.size[0])]
		for col in range(len(self.board)):
			for square in range(len(self.board[col])):
				board_rows[square].append(self.board[col][square])
		numbers_y, numbers_x = list(reversed(list(map(lambda x: x + 1, range(self.size[0]))))), list(reversed(list(map(lambda x: x + 1, range(self.size[1])))))
		max_length_y, max_length_x = len(str(numbers_y[0])), len(str(numbers_x[0]))
		# The top border (e.g. ┌———┬————┬————┬————┬————┐)
		result = "┌——" + ("—" * max_length_y)
		for _ in range(len(numbers_x)):
			result += "┬————"
		result += "┐\n"
		# Each rank, from top to bottom except the bottommost rank
		for index in range(len(numbers_y) - 1):
			result += f"│ {numbers_y[index]}{' ' * (max_length_y - len(str(numbers_y[index])))} │"  # The rank number
			# Add the square cells
			for square in board_rows[index]:
				result += VALUES[square] + "│"
			result += "\n"
			# Add the horizontal separator
			result += f"┝ {' ' * max_length_y} ┽"
			for _ in range(len(board_rows[index]) - 1):
				result += "————┼"
			result += "————┤\n"
		# Add the final rank with a special character
		result += f"│ 1{' ' * (max_length_y - 1)} │"
		for square in board_rows[-1]:
			result += VALUES[square] + "│"
		result += "\n"
		result += f"├——{'—' * max_length_y}┼"
		for _ in range(len(board_rows[index]) - 1):
			result += "————╁"
		result += "————┤\n"
		# Add the file numbers
		result += f"│  {' ' * max_length_y}│"
		for number in numbers_x[::-1]:
			result += f" {' ' * (max_length_x - len(str(number)))}{number} {' ' if number != numbers_x[0] else ''}{' ' if max_length_x == 1 else ''}"  # Append the file number with the correct spacing (on the last number, remove a space at the end for the border)
		result += f"│\n└—{'—' * max_length_y}—┴"
		for _ in range(len(numbers_x) - 1):
			result += "————┸"
		result += "————┘"
		return result

	def has_player_won(self):
		"""Returns True if the player has won, False otherwise."""
		return any([self.get_n_in_a_row(player_number, self.connect_size) for player_number in [1, 2]])
		# # Check vertical lines
		# for column in self.board:
		# 	for square in range(len(column) - self.connect_size + 1):
		# 		if len(set(column[square:square + self.connect_size])) == 1 and column[square] != 0:
		# 			return True
		# # Check horizontal lines
		# for row in range(len(self.board) - self.connect_size + 1):
		# 	for square in range(len(self.board[row])):
		# 		if len(set(self.board[row + x][square] for x in range(self.connect_size))) == 1 and self.board[row][square] != 0:
		# 			return True
		# # Check diagonal lines
		# for row in range(len(self.board) - self.connect_size + 1):
		# 	for square in range(len(self.board[row]) - self.connect_size + 1):
		# 		if len(set(self.board[row + x][square + x] for x in range(self.connect_size))) == 1 and self.board[row][square] != 0:
		# 			return True
		# 	for square in range(self.connect_size - 1, len(self.board[row])):
		# 		if len(set(self.board[row + x][square - x] for x in range(self.connect_size))) == 1 and self.board[row][square] != 0:
		# 			return True
		
		# return False

	def is_game_over(self):
		"""Returns True if the game is over, False otherwise."""
		if self.has_player_won():
			return True
		return self.is_tie()
	
	def is_tie(self):
		"""Returns True if the game is tied, False otherwise."""
		for column in self.board:
			for square in column:
				if not square:
					return False
		return True

	def legal_moves(self):
		"""Returns a list of all possible moves in the current position."""
		moves = []
		for column_index in range(len(self.board)):
			for square in self.board[column_index]:
				if not square:
					moves.append(column_index + 1)
		return moves
	
	def undo(self):
		if not self.moves:
			return
		for square_index in range(len(self.board[self.moves[-1]])):
			if self.board[self.moves[-1]][square_index]:
				self.board[self.moves[-1]][square_index] = 0
				break
		self.turn = 3 - self.turn
		self.moves.pop()
	
	def place_move(self, col):
		"""Finds the first empty square in the column and places the move there."""
		for i in range(len(self.board[col - 1]))[::-1]:
			if not self.board[col - 1][i]:
				self.board[col - 1][i] = self.turn
				self.turn = 3 - self.turn
				self.moves.append(col - 1)
				break	

	def evaluate(self):
		"""Returns the evaluation of the position
		Positive values indicate advantage for player 1, negative values favor player 2
		"""
		return 0
		# if player 1 won, return inf, if player 2 won, return -inf
		if self.has_player_won():
			return -1 * ((-1) ** self.turn) * float("inf")
		if self.is_tie():
			return 0
		result = 0
		for i in range(2, self.connect_size):
			result += i * self.get_n_in_a_row(1, i)
			result -= i * self.get_n_in_a_row(2, i)
		return result

	def get_n_in_a_row(self, player, n):
		"""Returns the number of n-in-a-rows for the given player."""
		result = 0
		# Check vertical lines
		for column in self.board:	
			for square in range(len(column) - n + 1):
				if len(set(column[square:square + n])) == 1 and column[square] == player:
					result += 1

		# Check horizontal lines
		for row in range(len(self.board) - n + 1):
			for square in range(len(self.board[row])):
				if len(set(self.board[row + x][square] for x in range(n))) == 1 and self.board[row][square] == player:
					result += 1
					
		# Check diagonal lines
		for row in range(len(self.board) - n + 1):
			for square in range(len(self.board[row]) - n + 1):
				if len(set(self.board[row + x][square + x] for x in range(n))) == 1 and self.board[row][square] == player:
					result += 1
			for square in range(n - 1, len(self.board[row])):
				if len(set(self.board[row + x][square - x] for x in range(n))) == 1 and self.board[row][square] == player:
					result += 1
		
		return result

# -*- coding: utf-8 -*-

import typing


VALUES = ["    ", "\033[31m ◉  \033[0m", "\033[93m ◉  \033[0m"]


class Board:
	def __init__(self, size: typing.List[int], connect_size: int):
		self.board = [[0 for _ in range(size[1])] for _ in range(size[0])]  # Possible values in board: 0 (empty), 1 (red), or 2 (yellow)
		# self.board = [[random.randint(0, 2) for _ in range(size[1])] for _ in range(size[0])]  # Populate the board with random values
		self.size = size
		
	def visualize_board(self):
		# return "┌———┬————┬————┬————┬————┬————┬————┬————┐\n│" + f"│\n┝  {' ' * (len(str(self.size[0])) - 1)} ┽————┼————┼————┼————┼————┼————┼————┤\n│".join([f" {len(self.board) - x}{' ' * (len(str(self.size[0])) - len(str(x - 1)))} │" + "│".join([VALUES[y] for y in self.board[x]]) for x in range(len(self.board))]) + f"│\n├——{'—' * (len(str(self.size[0])) - 1)}—┼————╁————╁————╁————╁————╁————╁————┤\n│  {' ' * (len(str(self.size[0])) - 1)} │  {'    '.join(list(map(lambda x: str(x + 1), range(self.size[1]))))} │\n└——{'—' * (len(str(self.size[0])) - 1)}—┴————┸————┸————┸————┸————┸————┸————┘"
		numbers_y, numbers_x = list(reversed(list(map(lambda x: x + 1, range(self.size[0]))))), list(reversed(list(map(lambda x: x + 1, range(self.size[1])))))
		max_length_y, max_length_x = len(str(numbers_y[0])), len(str(numbers_x[0]))
		# The top border (e.g. ┌———┬————┬————┬————┬————┐)
		result = "┌——" + ("—" * max_length_y)
		for _ in range(len(numbers_x)):
			result += "┬————"
		result += "┐\n"
		# Each rank, from top to bottom except the bottomost rank
		for index in range(len(numbers_y) - 1):
			result += f"│ {numbers_y[index]}{' ' * (max_length_y - len(str(numbers_y[index])))} │"  # The rank number
			# Add the square cells
			for square in self.board[index]:
				result += VALUES[square] + "│"
			result += "\n"
			# Add the horizontal separator
			result += f"┝ {' ' * max_length_y} ┽"
			for _ in range(len(self.board[index]) - 1):
				result += "————┼"
			result += "————┤\n"
		# Add the final rank with a special character
		result += f"│ 1{' ' * (max_length_y - 1)} │"
		for square in self.board[-1]:
			result += VALUES[square] + "│"
		result += "\n"
		result += f"├——{'—' * max_length_y}┼"
		for _ in range(len(self.board[index]) - 1):
			result += "————╁"
		result += "————┤\n"
		# Add the file numbers
		result += f"│  {' ' * max_length_y}│"
		for number in numbers_x:
			result += f" {' ' * (max_length_x - len(str(number)))}{number} {' ' if number != 1 else ''}{' ' if max_length_x == 1 else ''}"  # Append the file number with the correct spacing (on the last number, remove a space at the end for the border)
		result += f"│\n└—{'—' * max_length_y}—┴"
		for _ in range(len(numbers_x) - 1):
			result += "————┸"
		result += "————┘"
		return result

	def is_game_over(self):
		pass

	def is_column_valid(self, col):
		return True
	
	def place_move(self, col):
		pass

	def moves(self):
		moves = []
		for column_index in range(len(self.board)):
			for square in self.board[column]:
				if not square:
					moves.append(column_index)
		return moves

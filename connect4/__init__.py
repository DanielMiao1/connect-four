VALUES = {None: "    ", 1: "\033[31m ◉  \033[0m", 2: "\033[93m ◉  \033[0m"}


class Game:
	def __init__(self, size=(6, 7), connect_size=4, position=None, turn=True, winner=None, terminal=False):
		if position is None:
			self.position = (((None,) * size[0],) * size[1])
		else:
			self.position = position
		self.turn, self.winner, self.terminal = turn, winner, terminal
		self.size, self.connect_size = size, connect_size

	@staticmethod
	def visualize_board(board):
		board_rows = [[] for _ in range(board.size[0])]
		for col in range(len(board.position)):
			for square in range(len(board.position[col])):
				board_rows[square].append(board.position[col][square])
		numbers_y, numbers_x = list(reversed(list(map(lambda x: x + 1, range(board.size[0]))))), list(reversed(list(map(lambda x: x + 1, range(board.size[1])))))
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

	@staticmethod
	def has_player_won(position):
		for color in [1, 2]:
			if position.get_n_in_a_row(position, color, position.connect_size):
				return color
		return None

	@staticmethod
	def is_tie(board):
		"""Returns True if the game is tied, False otherwise."""
		for column in board.position:
			if column[0] is None:
				return False
		return True

	@staticmethod
	def make_move(board, index):
		position = board.position
		for i in range(len(board.position[index - 1]))[::-1]:
			if not board.position[index - 1][i]:
				position = position[:index - 1] + (position[index - 1][:i] + (board.turn,) + position[index - 1][i + 1:],) + position[index:]
				turn = 3 - board.turn
				# winner/is_terminal variables: re-write functions here
				winner = Game.has_player_won(Game(position=position))
				terminal = (winner is not None) or Game.is_tie(Game(position=position))
				break
		return Game(position=position, turn=turn, winner=winner, terminal=terminal)

	@staticmethod
	def get_n_in_a_row(board, player, n):
		"""Returns the number of n-in-a-rows for the given player."""
		# TODO: (maybe) add a variable for occupied columns
		result = 0
		# Check vertical lines
		for column in board.position:
			for square in range(0, board.size[0] - n + 1):  # step parameter of range function should be (n - 1) (optimization)?
				for i in column[square:square + n]:
					if i != player:
						break
				else:
					result += 1

		# Check horizontal lines
		for col_index in range(board.size[1] - n + 1):
			for square_index in range(board.size[0]):
				for i in board.position[col_index:col_index + n]:
					if i[square_index] != player:
						break
				else:
					result += 1

		# Check diagonal lines
		for column_index in range(board.size[1] - n + 1):
			for row_index in range(board.size[0] - n + 1):
				for x in range(n):
					if board.position[column_index + x][row_index + x] != player:
						break
				else:
					result += 1

			for row_index in range(n - 1, board.size[0]):
				for x in range(n):
					if board.position[column_index + x][row_index - x] != player:
						break
				else:
					result += 1
		return result

	@staticmethod
	def legal_moves(board):
		moves = []
		for column_index in range(len(board.position)):
			if not board.position[column_index][0]:
				moves.append(column_index + 1)
		return moves

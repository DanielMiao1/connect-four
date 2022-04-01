# -*- coding: utf-8 -*-

"""
Connect Four Game
Supports any board configuration within the range 2x2-99x99. However, larger boards may not fit on the screen, and replit xterm unicode rendering errors may occur more frequently on larger boards.
"""

from board import Board
from player import HumanPlayer, AIPlayer

from typing import *

from os import system


class PLAYER:
	Computer, Human = range(2)


class Game:
	def __init__(self, size: List[int]=(6, 7), connect_size: int=4):
		self.board: Board = Board(size, connect_size)
		self.players: List[Union[HumanPlayer, AIPlayer]] = [HumanPlayer(1, self.board)]
		self.size: List[int] = size
		self.connect_size: int = connect_size

	def start(self):
		def prompt_mode(invalid=False):
			system("clear")
			print("""\033[96m_________                                    _____     __________
\033[34m__  ____/______ _______ _______ _____ _________  /_    ___  ____/______ ____  __________
\033[96m_  /     _  __ \__  __ \__  __ \_  _ \_  ___/_  __/    __  /_    _  __ \_  / / /__  ___/
\033[34m/ /___   / /_/ /_  / / /_  / / //  __// /__  / /_      _  __/    / /_/ // /_/ / _  /
\033[96m\____/   \____/ /_/ /_/ /_/ /_/ \___/ \___/  \__/      /_/       \____/ \____/  /_/\033[0m""")  # speed
			
			result = input(f"\nEnter the mode, or 'h' for the help menu\n\033[91m{'[Invalid input] ' if invalid else ''}\033[0m> ")
			if result.lower() in ["c", "computer"]:
				return PLAYER.Computer
			elif result.lower() in ["f", "friend"]:
				return PLAYER.Human
			elif result.lower() in ["h", "help"]:
				return
			else:
				return prompt_mode(True)

		mode = prompt_mode()
		if mode == PLAYER.Computer:
			self.players.append(AIPlayer(2, self.board))
		elif mode == PLAYER.Human:
			self.players.append(HumanPlayer(2, self.board))
		else:
			system("clear")
			print("""\033[96m______  __      ______                ______  ___
\033[34m___  / / /_____ ___  /________        ___   |/  /_____ _______ ____  __
\033[96m__  /_/ / _  _ \__  / ___  __ \       __  /|_/ / _  _ \__  __ \_  / / /
\033[34m_  __  /  /  __/_  /  __  /_/ /       _  /  / /  /  __/_  / / // /_/ /
\033[96m/_/ /_/   \___/ /_/   _  ____/        /_/  /_/   \___/ /_/ /_/ \____/
\033[34m                      /_/\033[0m

\033[94mIntroduction\033[0m
Connect Four is a game where two players, one yellow and one red, take turns dropping their colored pieces into one of the grid's columns.
Upon dropping, the piece is automatically placed in the last empty space in the column, from top to bottom.
When four of either player's own discs form a horizontal, vertical, or diagonal line, that player wins.
""")
			if input("[Press Enter to continue, or 'q' to quit] > ").lower() in ["q", "quit"]:
				return self.start()
			system("clear")
			print("""\033[96m______  __      ______                ______  ___
\033[34m___  / / /_____ ___  /________        ___   |/  /_____ _______ ____  __
\033[96m__  /_/ / _  _ \__  / ___  __ \       __  /|_/ / _  _ \__  __ \_  / / /
\033[34m_  __  /  /  __/_  /  __  /_/ /       _  /  / /  /  __/_  / / // /_/ /
\033[96m/_/ /_/   \___/ /_/   _  ____/        /_/  /_/   \___/ /_/ /_/ \____/
\033[34m                      /_/\033[0m

\033[94mHow to start playing\033[0m
To start playing, you must first select a mode.
On the main screen, enter 'c' to play against the computer, or 'f' to play against a friend.
After selecting a mode, the game will automatically start, and the starting board will be printed.
""")
			if input("[Press Enter to continue, or 'q' to quit] > ").lower() in ["q", "quit"]:
				return self.start()
			system("clear")
			print("""\033[96m______  __      ______                ______  ___
\033[34m___  / / /_____ ___  /________        ___   |/  /_____ _______ ____  __
\033[96m__  /_/ / _  _ \__  / ___  __ \       __  /|_/ / _  _ \__  __ \_  / / /
\033[34m_  __  /  /  __/_  /  __  /_/ /       _  /  / /  /  __/_  / / // /_/ /
\033[96m/_/ /_/   \___/ /_/   _  ____/        /_/  /_/   \___/ /_/ /_/ \____/
\033[34m                      /_/\033[0m

\033[94mMaking a move\033[0m
To make a move, type in the column number (shown on the board) you wish to drop your piece in.
After pressing enter, the your piece will be automatically placed in the given column.

To undo a move, enter 'u' on your opponent's turn.
If the game has ended, you cannot undo any moves.
""")
			if input("[Press Enter to continue, or 'q' to quit] > ").lower() in ["q", "quit"]:
				return self.start()
			system("clear")
			print("""\033[96m______  __      ______                ______  ___
\033[34m___  / / /_____ ___  /________        ___   |/  /_____ _______ ____  __
\033[96m__  /_/ / _  _ \__  / ___  __ \       __  /|_/ / _  _ \__  __ \_  / / /
\033[34m_  __  /  /  __/_  /  __  /_/ /       _  /  / /  /  __/_  / / // /_/ /
\033[96m/_/ /_/   \___/ /_/   _  ____/        /_/  /_/   \___/ /_/ /_/ \____/
\033[34m                      /_/\033[0m

\033[94mCustomizing the board\033[0m
To change the size of the board and the number of discs that must be connected to win, enter 's' for the settings menu on the main screen.
Then, enter the setting ('s' for size of board, and 'n' ofr number of discs to win) you wish to change, and enter the new value for the setting.
For changing the size of the board, the new value should by in the format 'axb', where 'a' and 'b' are integers within the inclusive range of 2-99.
For changing the number of discs to win, the new value should be an integer larger or equal to 2, but smaller or equal to the board \033[1mwidth\033[0m.
""")
			input("[Press Enter for the main menu] > ")
			return self.start()

		while True:
			system("clear")
			print(self.board.visualize_board())
			input()
			pass


game = Game()
game.start()


# size of the board, connect n

# either player can be AI or human


"""
  0 1 2 3 4 5 6 7
0 0 -1
1.1 0 -1
2.  1 0 -1
3     1
4
5
6
7


  0 1 2 3 4 5 6 7
0             6 7
1             7
2           7
3         7
4
5
6
7
"""

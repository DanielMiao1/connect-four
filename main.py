# -*- coding: utf-8 -*-

"""
Connect Four Game
Supports any board configuration within the range 2x2-99x99. However, larger boards may not fit on the screen.
"""
import re

from board import Board
from player import HumanPlayer, AIPlayer
from settings import board_size, connect_length, settings_menu

import help_menu

from typing import *

from os import system


class PLAYER:
	Computer, Human = range(2)


class Game:
	def __init__(self, size: List[int]=board_size, connect_size: int=connect_length):
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
				return "h"
			elif result.lower() in ["s", "settings"]:
				return "s"
			else:
				return prompt_mode(True)

		mode = prompt_mode()
		print(mode)
		if mode == PLAYER.Computer:
			self.players.append(AIPlayer(2, self.board))
		elif mode == PLAYER.Human:
			self.players.append(HumanPlayer(2, self.board))
		elif mode == "h":
			help_menu.help_menu()
			return self.start()
		else:
			settings_menu()
			return self.start()

		while not self.board.is_game_over():
			system("clear")
			print(self.board.visualize_board())
			print(f"It is player {self.board.turn} (%s{('Red', 'Yellow')[self.board.turn - 1]}%s)'s turn to move" % (("\033[31m", "\033[93m")[self.board.turn - 1], "\033[0m"))
			move = self.players[self.board.turn - 1].get_player_move()
			while not move:
				system("clear")
				print(self.board.visualize_board())
				print(f"It is player {self.board.turn} (%s{('Red', 'Yellow')[self.board.turn - 1]}%s)'s turn to move" % (("\033[31m", "\033[93m")[self.board.turn - 1], "\033[0m"))
				move = self.players[self.board.turn - 1].get_player_move(True)
			if move == "u":
				self.board.undo()
				continue
			self.board.place_move(move)
		system("clear")
		print(self.board.visualize_board())
		print(f"{('Yellow', 'Red')[self.board.turn - 1]} wins")


try:
	game = Game()
	game.start()
except KeyboardInterrupt:
	exit("")


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

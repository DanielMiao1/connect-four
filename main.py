# -*- coding: utf-8 -*-

"""
Connect Four Game
Supports any board configuration within the range 2x2-99x99. However, larger boards may not fit on the screen.
"""

from connect4 import Game as Connect4
from player import HumanPlayer, AIPlayer
from settings import board_size, connect_length, settings_menu

import help_menu

from typing import List, Union

from os import system


class PLAYER:
	Computer, Human = range(2)


class Game:
	def __init__(self, size: List[int]=board_size, connect_size: int=connect_length):
		self.board: Connect4 = Connect4(size, connect_size)
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
			
			result = input(f"\nEnter the mode ('f' to play with a friend, or 'c' to play against the computer), or 'h' for the help menu\n\033[91m{'[Invalid input] ' if invalid else ''}\033[0m> ")
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
		if mode == PLAYER.Computer:
			self.players.append(AIPlayer(2, self.board))
		elif mode == PLAYER.Human:
			self.players.append(HumanPlayer(2, self.board))
		elif mode == "h":
			help_menu.help_menu()
			return self.start()
		else:
			result = settings_menu()
			if result:
				if result[0] == "s":
					global board_size
					board_size = (int(result[1].split("x")[0]), int(result[1].split("x")[1]))
				elif result[0] == "c":
					global connect_length
					connect_length = int(result[1])
				self.board: Connect4 = Connect4(board_size, connect_length)
				self.players: List[Union[HumanPlayer, AIPlayer]] = [HumanPlayer(1, self.board)]
				self.size: List[int] = board_size
				self.connect_size: int = connect_length
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
		if self.board.is_tie():
			print("The game is tied")
		else:
			print(f"{('Yellow', 'Red')[self.board.turn - 1]} wins")


try:
	game = Game()
	game.start()
except KeyboardInterrupt:
	exit("")

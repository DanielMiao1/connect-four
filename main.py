# -*- coding: utf-8 -*-

"""
Connect Four Game
Supports any board configuration within the range 2x2-99x99. However, larger boards may not fit on the screen, and replit xterm unicode rendering errors may occur more frequently on larger boards.
"""

from board import Board
from player import HumanPlayer, AIPlayer

import typing
import curses
import _thread

from os import system


y = 0


def print(screen, string, add_line=True, color=None):
	global y
	if color is None:
		screen.addstr(y, 0, string)
	else:
		screen.addstr(y, 0, string, color)
	screen.refresh()
	
	if add_line:
		y += len(string.splitlines())


def get_input(screen, prompt):
	global y
	curses.echo()
	screen.addstr(y, 0, prompt)
	screen.refresh()
	y += 3
	return screen.getstr(y + 1, 0, 1)


class PLAYER:
	Computer, Human = range(2)


class Game:
	def __init__(self, size: typing.List[int]=(6, 7), connect_size: int=4):
		self.board = Board(size, connect_size)
		self.players = [HumanPlayer(1, self.board)]
		self.size = size
		self.connect_size = connect_size

	def start(self, screen):

		def prompt_mode(clear=True):
			print(screen, "_________                                    _____     __________", color=curses.color_pair(1))
			print(screen, "__  ____/______ _______ _______ _____ _________  /_    ___  ____/______ ____  __________", color=curses.color_pair(1) | curses.A_DIM)
			print(screen, "_  /     _  __ \__  __ \__  __ \_  _ \_  ___/_  __/    __  /_    _  __ \_  / / /__  ___/", color=curses.color_pair(1))
			print(screen, "/ /___   / /_/ /_  / / /_  / / //  __// /__  / /_      _  __/    / /_/ // /_/ / _  /", color=curses.color_pair(1) | curses.A_DIM)
			print(screen, "\____/   \____/ /_/ /_/ /_/ /_/ \___/ \___/  \__/      /_/       \____/ \____/  /_/", color=curses.color_pair(1))
			
			mode = get_input(screen, "Enter the mode, or 'h' for the help menu")
			print(screen, str(mode.lower() == "h"))
			if mode.lower() in ["c", "computer"]:
				return PLAYER.Computer
			elif mode.lower() in ["f", "friend"]:
				return PLAYER.Human
			elif mode.lower() in ["h", "help"]:
				return help
			else:
				return prompt_mode()

		mode = prompt_mode(False)
		if mode == PLAYER.Computer:
			self.players.append(AIPlayer(2, self.board))
		elif mode == PLAYER.Human:
			self.players.append(HumanPlayer(2, self.board))
		else:
			screen.clear()
			print(screen, "HELP MENU")
			input()
			return self.start(screen)
		while True:
			system("clear")
			print(self.board.visualize_board())
			input()
			pass


def main(screen):
	curses.curs_set(0)
	curses.mousemask(1)

	curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)

	def listen(screen):
		while True:
			screen.refresh()
			key = screen.getch()
			if key == curses.KEY_MOUSE:
				_, x, y, _, _ = curses.getmouse()
				# print(screen, f"{x} {y}")
				print(screen, "ahsdbh")
				# screen.addstr(1, 0, get_input(screen, 1, 0, "HI:"))
	
	game = Game()
	_thread.start_new_thread(listen, (screen,))
	game.start(screen)


curses.wrapper(main)


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

# -*- coding: utf-8 -*-
from os import system


def help_menu():
	system("clear")
	print("""\033[96m    __  __          __                    __  ___
\033[34m   / / / /  ___    / /    ____           /  |/  /  ___    ____   __  __
\033[96m  / /_/ /  / _ \  / /    / __ \         / /|_/ /  / _ \  / __ \ / / / /
\033[34m / __  /  /  __/ / /    / /_/ /        / /  / /  /  __/ / / / // /_/ /
\033[96m/_/ /_/   \___/ /_/    / ____/        /_/  /_/   \___/ /_/ /_/ \____/
\033[34m                      /_/\033[0m

\033[94mIntroduction\033[0m
Connect Four is a game where two players, one yellow and one red, take turns dropping their colored pieces into one of the grid's columns.
Upon dropping, the piece is automatically placed in the last empty space in the column, from top to bottom.
When four of either player's own discs form a horizontal, vertical, or diagonal line, that player wins.
""")
	if input("[Press Enter to continue, or 'q' to quit] > ").lower() in ["q", "quit"]:
		return
	system("clear")
	print("""\033[96m    __  __          __                    __  ___
\033[34m   / / / /  ___    / /    ____           /  |/  /  ___    ____   __  __
\033[96m  / /_/ /  / _ \  / /    / __ \         / /|_/ /  / _ \  / __ \ / / / /
\033[34m / __  /  /  __/ / /    / /_/ /        / /  / /  /  __/ / / / // /_/ /
\033[96m/_/ /_/   \___/ /_/    / ____/        /_/  /_/   \___/ /_/ /_/ \____/
\033[34m                      /_/\033[0m

\033[94mHow to start playing\033[0m
To start playing, you must first select a mode.
On the main screen, enter 'c' to play against the computer, or 'f' to play against a friend.
After selecting a mode, the game will automatically start, and the starting board will be printed.
""")
	if input("[Press Enter to continue, or 'q' to quit] > ").lower() in ["q", "quit"]:
		return
	system("clear")
	print("""\033[96m    __  __          __                    __  ___
\033[34m   / / / /  ___    / /    ____           /  |/  /  ___    ____   __  __
\033[96m  / /_/ /  / _ \  / /    / __ \         / /|_/ /  / _ \  / __ \ / / / /
\033[34m / __  /  /  __/ / /    / /_/ /        / /  / /  /  __/ / / / // /_/ /
\033[96m/_/ /_/   \___/ /_/    / ____/        /_/  /_/   \___/ /_/ /_/ \____/
\033[34m                      /_/\033[0m

\033[94mMaking a move\033[0m
To make a move, type in the column number (shown on the board) you wish to drop your piece in.
After pressing enter, the your piece will be automatically placed in the given column.

To undo a move, enter 'u' on your opponent's turn.
If the game has ended, you cannot undo any moves.
""")
	if input("[Press Enter to continue, or 'q' to quit] > ").lower() in ["q", "quit"]:
		return
	system("clear")
	print("""\033[96m    __  __          __                    __  ___
\033[34m   / / / /  ___    / /    ____           /  |/  /  ___    ____   __  __
\033[96m  / /_/ /  / _ \  / /    / __ \         / /|_/ /  / _ \  / __ \ / / / /
\033[34m / __  /  /  __/ / /    / /_/ /        / /  / /  /  __/ / / / // /_/ /
\033[96m/_/ /_/   \___/ /_/    / ____/        /_/  /_/   \___/ /_/ /_/ \____/
\033[34m                      /_/\033[0m

\033[94mCustomizing the board\033[0m
To change the size of the board and the number of discs that must be connected to win, enter 's' for the settings menu on the main screen.
Then, enter the setting ('s' for size of board, and 'n' for number of discs to win) you wish to change, and enter the new value for the setting.
For changing the size of the board, the new value should by in the format 'axb', where 'a' and 'b' are integers within the inclusive range of 2-99.
For changing the number of discs to win, the new value should be an integer larger or equal to 2, but smaller or equal to the board \033[1mwidth\033[0m.
""")
	input("[Press Enter for the main menu] > ")
	return

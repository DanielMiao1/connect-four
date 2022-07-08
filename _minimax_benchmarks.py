# -*- coding: utf-8 -*-
import os
import re
import time
import json
import random
import asyncio
import connect4


os.system("clear")


def get_amount(text, invalid=False, print_title=True, pattern=r"^\d+$"):
	if print_title:
		print("""\033[96m    ____                          __                                  __
\033[36m   / __ )  ___    ____   _____   / /_    ____ ___   ____ _   _____   / /__   _____
\033[96m  / __  | / _ \  / __ \ / ___/  / __ \  / __  __ \ / __  /  / ___/  / //_/  / ___/
\033[36m / /_/ / /  __/ / / / // /__   / / / / / / / / / // /_/ /  / /     / ,<    (__  )
\033[96m/_____/  \___/ /_/ /_/ \___/  /_/ /_/ /_/ /_/ /_/ \____/  /_/     /_/|_|  /____/\033[0m
""")
	amount = input(f"\033[91m{'[Invalid input] ' if invalid else ''}\033[92m{text}: \033[0m")
	if re.match(pattern, amount):
		return amount
	os.system("clear")
	return get_amount(text, True, pattern=pattern)


minimax_test = int(get_amount("Enter the amount of benchmarks to take for the minimax-vs-minimax test"))
random_test = int(get_amount("Enter the amount of benchmarks to take for the minimax-vs-random test", print_title=False))
minimax_level = int(get_amount("Enter the strength (depth) of the minimax engine", print_title=False, pattern=r"^[1-9]$"))
threads = int(get_amount("Enter the number of asynchronous threads allowed", print_title=False, pattern=r"^([1-9]|[1-9]([0-9]+))$"))

spawned_threads = 0
completed_tests = 0

minimax_wins = minimax_losses = minimax_ties = 0
minimax_games = []


async def minimax_test_case():
	global spawned_threads, completed_tests, minimax_wins, minimax_losses, minimax_ties
	game = connect4.Game()
	while not game.is_game_over():
		result = game.minimax_algorithm(minimax_level, game.turn)[0]
		if result is None:
			result = random.choice(game.legal_moves())
		game.place_move(result)
	minimax_games.append(game.moves)
	completed_tests += 1
	spawned_threads -= 1
	os.system("clear")
	print(f"""\033[96m    ____                          __                                  __
\033[36m   / __ )  ___    ____   _____   / /_    ____ ___   ____ _   _____   / /__   _____
\033[96m  / __  | / _ \  / __ \ / ___/  / __ \  / __  __ \ / __  /  / ___/  / //_/  / ___/
\033[36m / /_/ / /  __/ / / / // /__   / / / / / / / / / // /_/ /  / /     / ,<    (__  )
\033[96m/_____/  \___/ /_/ /_/ \___/  /_/ /_/ /_/ /_/ /_/ \____/  /_/     /_/|_|  /____/\033[0m

\033[94mRunning {minimax_test} minimax-vs-minimax test{'s' if minimax_test > 1 else ''}\033[0m

\033[93mCompleted tests: {completed_tests}/{minimax_test}\033[0m
""")
	if game.is_tie():
		minimax_ties += 1
	else:
		if game.turn == 1:
			minimax_losses += 1
		else:
			minimax_wins += 1


os.system("clear")
print(f"""\033[96m    ____                          __                                  __
\033[36m   / __ )  ___    ____   _____   / /_    ____ ___   ____ _   _____   / /__   _____
\033[96m  / __  | / _ \  / __ \ / ___/  / __ \  / __  __ \ / __  /  / ___/  / //_/  / ___/
\033[36m / /_/ / /  __/ / / / // /__   / / / / / / / / / // /_/ /  / /     / ,<    (__  )
\033[96m/_____/  \___/ /_/ /_/ \___/  /_/ /_/ /_/ /_/ /_/ \____/  /_/     /_/|_|  /____/\033[0m

\033[94mRunning {minimax_test} minimax-vs-minimax test{'s' if minimax_test > 1 else ''}\033[0m

\033[93mCompleted: 0/{minimax_test}
""")

for i in range(minimax_test):
	while spawned_threads >= threads:
		pass
	spawned_threads += 1
	asyncio.run(minimax_test_case())


while spawned_threads:
	time.sleep(0.1)

print(f"""\033[93mResults:
\033[92m\tWins: {minimax_wins}
\033[93m\tTies: {minimax_ties}
\033[91m\tLosses: {minimax_losses}""")

input("\033[92mPress any key to continue: \033[0m")

os.system("clear")
print(f"""\033[96m    ____                          __                                  __
\033[36m   / __ )  ___    ____   _____   / /_    ____ ___   ____ _   _____   / /__   _____
\033[96m  / __  | / _ \  / __ \ / ___/  / __ \  / __  __ \ / __  /  / ___/  / //_/  / ___/
\033[36m / /_/ / /  __/ / / / // /__   / / / / / / / / / // /_/ /  / /     / ,<    (__  )
\033[96m/_____/  \___/ /_/ /_/ \___/  /_/ /_/ /_/ /_/ /_/ \____/  /_/     /_/|_|  /____/\033[0m

\033[94mRunning {random_test} minimax-vs-random test{'s' if random_test > 1 else ''}\033[0m

\033[93mCompleted: 0/{random_test}
""")

spawned_threads = 0
completed_tests = 0

random_wins = random_losses = random_ties = 0
random_games = []


async def random_test_case():
	global spawned_threads, completed_tests, random_wins, random_losses, random_ties
	game = connect4.Game()
	while not game.is_game_over():
		if game.turn == 1:
			result = game.minimax_algorithm(minimax_level, game.turn)[0]
			if result is None:
				result = random.choice(game.legal_moves())
		else:
			result = random.choice(game.legal_moves())
		game.place_move(result)
	random_games.append(game.moves)
	completed_tests += 1
	spawned_threads -= 1
	os.system("clear")
	print(f"""\033[96m    ____                          __                                  __
\033[36m   / __ )  ___    ____   _____   / /_    ____ ___   ____ _   _____   / /__   _____
\033[96m  / __  | / _ \  / __ \ / ___/  / __ \  / __  __ \ / __  /  / ___/  / //_/  / ___/
\033[36m / /_/ / /  __/ / / / // /__   / / / / / / / / / // /_/ /  / /     / ,<    (__  )
\033[96m/_____/  \___/ /_/ /_/ \___/  /_/ /_/ /_/ /_/ /_/ \____/  /_/     /_/|_|  /____/\033[0m

\033[94mRunning {random_test} minimax-vs-random test{'s' if random_test > 1 else ''}\033[0m

\033[93mCompleted tests: {completed_tests}/{random_test}\033[0m
""")
	if game.is_tie():
		random_ties += 1
	else:
		if game.turn == 0:
			random_losses += 1
		else:
			random_wins += 1

for i in range(random_test):
	while spawned_threads >= threads:
		pass
	spawned_threads += 1
	asyncio.run(random_test_case())


while spawned_threads:
	time.sleep(0.1)

print(f"""\033[93mResults:
\033[92m\tWins: {random_wins}
\033[93m\tTies: {random_ties}
\033[91m\tLosses: {random_losses}""")

filename = input("\033[92mEnter the filename (case-sensitive, will overwrite any existing content) to export the results in JSON format, or ^C to exit: \033[0m")
if filename.lower() == "^C":
	exit()
else:
	with open(filename, "w") as file:
		result = {"minimax-vs-minimax": {"games": [i for i in minimax_games], "wins": minimax_wins, "losses": minimax_losses, "ties": minimax_ties}, "minimax-vs-random": {"games": [i for i in random_games], "wins": random_wins, "losses": random_losses, "ties": random_ties}}
		json.dump(result, file)

exit()

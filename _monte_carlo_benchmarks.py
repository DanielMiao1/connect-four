# -*- coding: utf-8 -*-
import os
import re
import time
import json
import random
import asyncio
import connect4
import connect4.algorithms


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


algorithm_test = int(get_amount("Enter the amount of benchmarks to take for the montecarlo-vs-montecarlo test"))
minimax_test = int(get_amount("Enter the amount of benchmarks to take for the montecarlo-vs-minimax test", print_title=False))
random_test = int(get_amount("Enter the amount of benchmarks to take for the montecarlo-vs-random test", print_title=False))
level = int(get_amount("Enter the rollout count of the monte carlo algorithm", print_title=False, pattern=r"^([1-9]|[0-9]\d+)$"))
threads = int(get_amount("Enter the number of asynchronous threads allowed", print_title=False, pattern=r"^([1-9]|[0-9]\d+)$"))

spawned_threads = 0
completed_tests = 0

algorithm_wins = algorithm_ties = algorithm_losses = 0
montecarlo_games = []


async def montecarlo_test_case():
	global spawned_threads, completed_tests, algorithm_wins, algorithm_ties, algorithm_losses
	game = connect4.Game()
	tree = connect4.algorithms.MonteCarlo()
	moves = []
	while not game.has_player_won(game) and not game.is_tie(game):
		for _ in range(level):
			tree.rollout(game)
		move = tree.choose(game)
		moves.append(move.moves[-1])
		game = move
	montecarlo_games.append(moves)
	completed_tests += 1
	spawned_threads -= 1
	os.system("clear")
	print(f"""\033[96m    ____                          __                                  __
\033[36m   / __ )  ___    ____   _____   / /_    ____ ___   ____ _   _____   / /__   _____
\033[96m  / __  | / _ \  / __ \ / ___/  / __ \  / __  __ \ / __  /  / ___/  / //_/  / ___/
\033[36m / /_/ / /  __/ / / / // /__   / / / / / / / / / // /_/ /  / /     / ,<    (__  )
\033[96m/_____/  \___/ /_/ /_/ \___/  /_/ /_/ /_/ /_/ /_/ \____/  /_/     /_/|_|  /____/\033[0m
\033[94mRunning {algorithm_test} montecarlo-vs-montecarlo test{'s' if algorithm_test > 1 else ''}\033[0m
\033[93mCompleted tests: {completed_tests}/{algorithm_test}\033[0m
""")
	if game.is_tie(game):
		algorithm_ties += 1
	else:
		if game.turn:
			algorithm_losses += 1
		else:
			algorithm_wins += 1


os.system("clear")
print(f"""\033[96m    ____                          __                                  __
\033[36m   / __ )  ___    ____   _____   / /_    ____ ___   ____ _   _____   / /__   _____
\033[96m  / __  | / _ \  / __ \ / ___/  / __ \  / __  __ \ / __  /  / ___/  / //_/  / ___/
\033[36m / /_/ / /  __/ / / / // /__   / / / / / / / / / // /_/ /  / /     / ,<    (__  )
\033[96m/_____/  \___/ /_/ /_/ \___/  /_/ /_/ /_/ /_/ /_/ \____/  /_/     /_/|_|  /____/\033[0m
\033[94mRunning {algorithm_test} montecarlo-vs-montecarlo test{'s' if algorithm_test > 1 else ''}\033[0m
\033[93mCompleted: 0/{algorithm_test}
""")

for i in range(algorithm_test):
	while spawned_threads >= threads:
		pass
	spawned_threads += 1
	asyncio.run(montecarlo_test_case())


while spawned_threads:
	time.sleep(0.1)

print(f"""\033[93mResults:
\033[92m\tWins: {algorithm_wins}
\033[93m\tTies: {algorithm_ties}
\033[91m\tLosses: {algorithm_losses}""")

input("\033[92mPress any key to continue: \033[0m")

os.system("clear")
print(f"""\033[96m    ____                          __                                  __
\033[36m   / __ )  ___    ____   _____   / /_    ____ ___   ____ _   _____   / /__   _____
\033[96m  / __  | / _ \  / __ \ / ___/  / __ \  / __  __ \ / __  /  / ___/  / //_/  / ___/
\033[36m / /_/ / /  __/ / / / // /__   / / / / / / / / / // /_/ /  / /     / ,<    (__  )
\033[96m/_____/  \___/ /_/ /_/ \___/  /_/ /_/ /_/ /_/ /_/ \____/  /_/     /_/|_|  /____/\033[0m
\033[94mRunning {random_test} montecarlo-vs-random test{'s' if random_test > 1 else ''}\033[0m
\033[93mCompleted: 0/{random_test}
""")

spawned_threads = 0
completed_tests = 0

random_wins = random_losses = random_ties = 0
random_games = []


async def random_test_case():
	global spawned_threads, completed_tests, random_wins, random_losses, random_ties
	game = connect4.Game()
	tree = connect4.algorithms.MonteCarlo()
	moves = []
	while not game.has_player_won(game) and not game.is_tie(game):
		for _ in range(level):
			tree.rollout(game)
		move = tree.choose(game)
		moves.append(move.moves[-1])
		game = move
		if game.has_player_won(game) or game.is_tie(game):
			break
		move = game.make_move(game, random.choice(game.legal_moves(game)))
		moves.append(move.moves[-1])
		game = move
	random_games.append(moves)
	completed_tests += 1
	spawned_threads -= 1
	os.system("clear")
	print(f"""\033[96m    ____                          __                                  __
\033[36m   / __ )  ___    ____   _____   / /_    ____ ___   ____ _   _____   / /__   _____
\033[96m  / __  | / _ \  / __ \ / ___/  / __ \  / __  __ \ / __  /  / ___/  / //_/  / ___/
\033[36m / /_/ / /  __/ / / / // /__   / / / / / / / / / // /_/ /  / /     / ,<    (__  )
\033[96m/_____/  \___/ /_/ /_/ \___/  /_/ /_/ /_/ /_/ /_/ \____/  /_/     /_/|_|  /____/\033[0m
\033[94mRunning {random_test} montecarlo-vs-random test{'s' if random_test > 1 else ''}\033[0m
\033[93mCompleted tests: {completed_tests}/{random_test}\033[0m
""")
	if game.is_tie(game):
		random_ties += 1
	else:
		if game.turn:
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
		result = {"montecarlo-vs-montecarlo": {"games": [i for i in montecarlo_games], "wins": algorithm_wins, "losses": algorithm_losses, "ties": algorithm_ties}, "montecarlo-vs-random": {"games": [i for i in random_games], "wins": random_wins, "losses": random_losses, "ties": random_ties}}
		json.dump(result, file)

exit()
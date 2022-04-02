# -*- coding: utf-8 -*-
from os import system

import re
import time

board_size = (6, 7)
connect_length = 4


def settings_menu():
	def prompt_setting(invalid: bool=False):
		system("clear")
		print(f"""\033[96m   _____         __    __
\033[34m  / ___/  ___   / /_  / /_   ( )   ____    ____ _   _____
\033[96m  \__ \  / _ \ / __/ / __/  / /   / __ \  / __  /  / ___/
\033[34m ___/ / /  __// /_  / /_   / /   / / / / / /_/ /  (__  )
\033[96m/____/  \___/ \__/  \__/  /_/   /_/ /_/  \__  /  /____/
\033[34m                                        /____/\033[0m

Board size: {board_size[0]}x{board_size[1]}
Connect length: {connect_length}

Enter the setting you wish to change, or 'q' to quit:""")  # slant
		prompt = input(f"\033[91m{'[Invalid input] ' if invalid else ''}\033[0m> ")
		if prompt.lower() in ["q", "quit"]:
			return "q"
		elif prompt.lower() in ["s", "size"]:
			return "s"
		elif prompt.lower() in ["n", "number"]:
			return "n"
		else:
			return prompt_setting(True)
	
	setting = prompt_setting()
	if setting == "q":
		return

	def prompt_setting_value(invalid: bool=False):
		system("clear")
		print("""\033[96m   _____         __    __
\033[34m  / ___/  ___   / /_  / /_   ( )   ____    ____ _   _____
\033[96m  \__ \  / _ \ / __/ / __/  / /   / __ \  / __  /  / ___/
\033[34m ___/ / /  __// /_  / /_   / /   / / / / / /_/ /  (__  )
\033[96m/____/  \___/ \__/  \__/  /_/   /_/ /_/  \__  /  /____/
\033[34m                                        /____/\033[0m

Enter the new value for the setting, or 'q' to quit:""")
		prompt = input(f"{'[Invalid input] ' if invalid else ''}> ")
		if prompt.lower() in ["q", "quit"]:
			return "q"
		elif setting == "s":
			if re.match(r"^([2-9]|[1-9]{2})x([2-9]|[1-9]{2})$", prompt) is not None:
				global board_size
				board_size = (int(prompt.split("x")[0]), int(prompt.split("x")[1]))
				print(f"\033[92mBoard size is now set to {board_size[0]}x{board_size[1]}\033[0m\nReturning to main menu in 1500ms")
				time.sleep(1.5)
				return prompt
			else:
				return prompt_setting_value(True)
		elif setting == "n":
			if re.match(rf"^[2-{board_size[0]}]$", prompt) is not None:
				global connect_length
				connect_length = int(prompt)
				print(f"\033[92mConnect length is now set to {connect_length}\033[0m\nReturning to main menu in 1500ms")
				time.sleep(1.5)
				return prompt
			else:
				return prompt_setting_value(True)
		else:
			return prompt_setting_value(True)
	
	value = prompt_setting_value()
	return

from enemies import Enemy


def choose_target_menu(enemy_list: list[Enemy]):
	print('=' * 20)
	print('Choose target: ')
	for i, enemy in enumerate(enemy_list, start=1):
		print(f'{i}. {enemy.name} | {enemy.hp}HP')
	print('=' * 20)

	inp = input_index('', len(enemy_list))
	return enemy_list[inp]


def input_index(prompt, max_n) -> int:
	while True:
		try:
			x = input(prompt)
			if x.lower().strip() == 'e':
				raise SystemExit
			x = int(x)
			if x < 1 or x > max_n:
				raise ValueError
			return x - 1
		except ValueError:
			print("Invalid choice")
			continue
	return -1

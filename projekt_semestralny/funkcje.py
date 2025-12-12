import random

from statystyki import *


def game_over():
	print('\n' * 5)
	print(line)
	print('GAME OVER')
	print(line)


def game_win():
	print('\n' * 20)
	print(line)
	print('WYGRALES')
	print(line)
	exit()


def use_item(item):
	if item in inv:
		if item == mikstura_heal:
			gracz[HP] += mikstura_heal[ITEM_STAT]
			if gracz[HP] > gracz[MAX_HP]:
				gracz[HP] = gracz[MAX_HP]
			inv.remove(mikstura_heal)
			print(f'{line}\nMasz {gracz[HP]}HP.\n{line}')
		elif item == mikstura_maxhp:
			if mikstura_maxhp[3] <= 2:
				gracz[MAX_HP] += mikstura_maxhp[ITEM_STAT]
				gracz[HP] = gracz[MAX_HP]
				mikstura_maxhp[3] += 1
				print(f'{line}\nMasz teraz {gracz[MAX_HP]} max. HP i {gracz[HP]} HP.')
			else:
				print(f'{line}\nUżyłeś już maksymalną ilość tej mikstury. Brak efektu')
			inv.remove(mikstura_maxhp)


def inventory():
	if len(inv) == 0:
		print('Ekwipunek jest pusty')
	else:
		n = 1
		print(f'{line}\nEKWIPUNEK')
		for i in inv:
			print(f'{n}) {i[0]}')
			n += 1
		inp = input('a) wróć\n')
		if inp == 'a'.lower():
			# return True
			pass
		else:
			inp = int(inp)
			if inp - 1 >= len(inv):
				print('Nieistniejaca opcja')
			# return True
			else:
				use_item(inv[inp - 1])


def namegen(wrog):
	name = []
	name.append(random.choice(prefix1))
	name.append(random.choice(prefix2))
	name.append(wrog[IMIE])
	if random.random() > 0.85:
		name.append(random.choice(suffix))
	return ' '.join(name)


def walka(wrog, imie_wroga):
	global quest_wykonane
	global quest_progress
	while gracz[HP] > 0 or wrog[HP] > 0:
		inp = input(
			"WALKA\n"
			"1) atak\n"
			"2) przedmioty\n"
			"3) ucieczka (70% sukces, 30% na stracenie tury)\n")
		if inp == '1':
			if random.random() > wrog[DODGE_CHANCE]:
				print(f'{line}\n{imie_wroga} unika ataku!\n{line}')
			else:
				wrog[HP] -= gracz[ATAK]
				print(f'{line}\nAtakujesz {imie_wroga} za {gracz[ATAK]}HP.\n	{imie_wroga} ma {wrog[HP]}HP.\n{line}')
			if gracz[HP] <= 0 or wrog[HP] <= 0:
				break
			if random.random() > gracz[DODGE_CHANCE]:
				print(f'Unikasz ataku!\n{line}')
			else:
				gracz[HP] -= wrog[ATAK] // gracz[ARMOR]
				print(f'{imie_wroga} atakuje cie za {wrog[ATAK] // gracz[ARMOR]}HP.\n	Masz {gracz[HP]}HP.\n{line}')
			if gracz[HP] <= 0 or wrog[HP] <= 0:
				break
		elif inp == '2':
			inventory()
		elif inp == '3':
			if not wrog[IMIE] == 'DAWID':
				if random.random() >= .7:
					print(line)
					print('Udało ci się uciec.')
					swiat_1()
				else:
					print(line)
					print('Nie udało ci się uciec.')
					print(line)
					if random.random() > gracz[DODGE_CHANCE]:
						print(f'Unikasz ataku!\n{line}')
					else:
						gracz[HP] -= wrog[ATAK] // gracz[ARMOR]
						print(
							f'{imie_wroga} atakuje cie za {wrog[ATAK] // gracz[ARMOR]}HP.\n	Masz {gracz[HP]}HP.\n{line}')
					if gracz[HP] <= 0 or wrog[HP] <= 0:
						break
			else:
				print(line)
				print('Od Dawida nie ma ucieczki.')
				print(line)

		else:
			print("Nieistniejaca opcja")
			continue

	if gracz[HP] > 0:
		if wrog[IMIE] == 'DAWID':
			game_win()
		else:
			print('GRACZ wygrywa!')
			drop = random.randint(wrog[2], wrog[3])
			gracz[CEBULION] += drop
			print(f'{wrog[4]} upuścił {drop}x cebulion!')


	elif gracz[HP] <= 0:
		game_over()
		exit()


def swiat_1():
	global quest_wykonane
	global quest_progress
	while swiat == 1:
		print(line)
		inp = input(
			"1) eksploracja\n"
			"2) sklep\n"
			"3) ekwipunek\n"
			"4) wejdz to tajemniczej jaskini. (oplaca sie przygotowac)\n\n"
			f"Masz {gracz[HP]} HP, {gracz[ATAK]} ataku, {gracz[ARMOR]} obrony i {gracz[CEBULION]}x cebulion.\n")
		if inp == '1':
			print(line)
			print(f"Wyruszasz na zwiad\n")
			x = random.random()
			# print(x)
			if x < 0.1:  # 10%
				n = namegen(cyklop)
				print(f'Napada cię {n}!')
				print(line)
				walka(cyklop[:], n)
			elif 0.1 <= x and x < 0.63:  # 53%
				n = namegen(goblin)
				print(f'Napada cię {n}!')
				print(line)
				walka(goblin[:], n)
			elif 0.63 <= x and x < 0.7:  # 7%
				gracz[CEBULION] += 30
				print("Podczas ekspedycji znalazłeś 30x cebulion!")
			elif 0.7 <= x and x < 0.9:  # 20%
				n = namegen(troll)
				print(f'Napada cię {n}!')
				print(line)
				walka(troll[:], n)
			elif 0.9 <= x and x < 0.95:  # 5%
				if gracz[ATAK] < 20:
					gracz[ATAK] = 30
					print("Znalazłeś zamrożonego schabowego z kością!\n"
						  "Twój atak wzrósł do 20.\n")
				else:
					gracz[CEBULION] += 30
					print("Znalazłeś zamrożonego schabowego z kością!\n"
						  "Masz już jednego lub posiadasz lepszą broń więc sprzedałeś go za 30 cebulionów.\n")
			elif 0.95 <= x and x <= 1:  # 5%
				if gracz[ARMOR] < 2:
					gracz[ARMOR] += 1
					print("Znalazłeś część zniszczonej palety! Używasz jej jako zbroi.\n"
						  "Twoja obrona wzrosła o 1.\n")
				else:
					gracz[CEBULION] += 30
					print("Znalazłeś kolejną część zniszczonej palety!\n"
						  "Masz już jedną więc sprzedałeś ją za 30 cebulionów.\n")
		elif inp == '2':
			print(line)
			inp = input("SKLEP\n"
						f"1){mikstura_heal[NAZWA]} - {mikstura_heal[CENA]} cebulionów \n"
						f"2){mikstura_maxhp[NAZWA]} - {mikstura_maxhp[CENA]} cebulionów\n"
						f"3)Excalibur (Zadaje 30 HP) - 60 cebulionów\n"
						f"4)Hełm z garnka - (Dodaje 0.5 obrony) - 50 cebulionów\n"
						f"a)Wyjdź\n"
						f"Masz {gracz[CEBULION]}x cebulion")
			if inp == '1':
				if gracz[CEBULION] >= mikstura_heal[CENA]:
					inv.append(mikstura_heal)
					gracz[CEBULION] -= mikstura_heal[CENA]
				else:
					print("Nie masz wystarczająco cebulionów")
					continue
			elif inp == '2':
				if gracz[CEBULION] >= mikstura_maxhp[CENA]:
					inv.append(mikstura_maxhp)
					gracz[CEBULION] -= mikstura_maxhp[CENA]
				else:
					print("Nie masz wystarczająco cebulionów")
					continue
			elif inp == '3':
				if gracz[CEBULION] >= 60:
					gracz[ATAK] = 30
					gracz[CEBULION] -= 60
				else:
					print("Nie masz wystarczająco cebulionów")
					continue
			elif inp == '4':
				if gracz[CEBULION] >= 50:
					if gracz[HELM] == 0:
						gracz[ARMOR] += 0.5
						gracz[HELM] = 1
						gracz[CEBULION] -= 50
					else:
						print("Masz już ten hełm")
				else:
					print("Nie masz wystarczająco cebulionów")
					continue
			if inp == 'a'.lower():
				pass
		elif inp == '3':
			inventory()
		elif inp == '4':
			print('\n' * 10)
			print(line)
			print('Wchodzisz do wielkiej, mrocznej jaskini\n'
				  'Nagle wejście sie za tobą zapada. Nie ma drogi ucieczki\n'
				  'ZZA ROGU WYŁANIA SIĘ DAWID')
			print(line)
			walka(dawid[:], 'DAWID')

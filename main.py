import random
from ctypes import c_uint

import data
import enemies
from enemies import *
from enemies import Enemy
from ui import input_index, choose_target_menu


class Player:
	def __init__(self):
		self.max_hp = 100
		self.hp = 100
		self.hp_regen = 0
		self.mp = 20
		self.max_mp = 20
		self.mp_regen = 2
		self.damage = 10
		self.crit_chance = 0.1
		self.inventory = [data.Small_Heal_Potion()]
		self.spell_inventory = [data.Fireball(), data.Heal()]
		self.gold = 0
		self.upgrade_price_multipliers = [1, 1, 1]

		self.has_consumed_item = False

	def take_damage(self, damage):
		self.hp -= damage
		if self.hp <= 0:
			print('is ded')

	def is_dead(self):
		return self.hp <= 0

	def add_item_to_inventory(self, item, cost):
		if self.gold >= cost:
			self.inventory.append(item)
			self.gold -= cost
			return True
		else:
			print(f'You dont have enough gold!')
			return False

	def use_item(self, index):
		item = self.inventory[index]
		is_item_used_up = item.use(self)
		if is_item_used_up:
			self.inventory.pop(index)
		self.has_consumed_item = True

	def add_spell_to_inventory(self, spell, cost):
		if self.gold >= cost:
			self.spell_inventory.append(spell)
			self.gold -= cost
			return True
		else:
			print(f'You dont have enough gold!')
			return False

	def reduce_mp(self, amount):
		self.mp = max(0, self.mp - amount)

	def calculate_drop_gold(self, enemy_list):
		total_gold_collected = 0
		for enemy in enemy_list:
			drop = random.randint(enemy.gold_drop[0], enemy.gold_drop[1])
			player.gold += drop
			total_gold_collected += drop
		return total_gold_collected


def handle_cooldowns():
	for spell in player.spell_inventory:
		spell.reduce_cooldown()

	def use_spell(self, index, enemy_list):
		spell = self.spell_inventory[index]
		# true = na cooldownie
		if spell.use(self, enemy_list):
			print('=' * 20)
			print('Spell is on cooldown!')
			print('=' * 20)


def cast_spell(enemy_list):
	if not player.spell_inventory:
		print(f'You have not spells yet!')
		print('=' * 20)
		return

	print('=' * 20)

	for i, spell in enumerate(player.spell_inventory, start=1):
		if spell.current_cooldown > 0:
			print(f'{i}. {spell.name} | Cooldown: {spell.current_cooldown}')
		else:
			print(f'{i}. {spell.name}')
	print('=' * 20)
	inp = input_index('', len(player.spell_inventory))
	if player.mp >= player.spell_inventory[inp].mp_cost:
		if player.spell_inventory[inp].is_on_cooldown():
			print('=' * 20)
			print(f'This spell is on cooldown! - Rounds left: {player.spell_inventory[inp].current_cooldown}')
			print('=' * 20)
		else:
			player.spell_inventory[inp].use(player, enemy_list)
			player.spell_inventory[inp].max_out_cooldown()
			player.reduce_mp(player.spell_inventory[inp].mp_cost)
			return player.spell_inventory[inp].is_attack_spell
	else:
		print('=' * 20)
		print(f'You dont have enough mp!')
		print('=' * 20)


def shop():
	inp = input_index(f'''
{'=' * 20}
1. Small Heal Potion | 20 gold      5. exit
2. Big Heal Potion | 60 gold
3. Fireball Spell | 50 gold
4. Heal Spell | 60 gold
{'=' * 20}
''', 5)

	if inp == 0:
		player.add_item_to_inventory(data.Small_Heal_Potion(), 20)
	if inp == 1:
		player.add_item_to_inventory(data.Big_Heal_Potion(), 60)
	if inp == 2:
		player.add_spell_to_inventory(data.Fireball(), 50)
	if inp == 3:
		player.add_spell_to_inventory(data.Heal(), 60)


def upgrade_menu():
	inp = input_index(f'''
----LIFE----             				
1. +10 max HP ({player.max_hp})   | {10 * player.upgrade_price_multipliers[0]} gold      					
2. +2 HP regen ({player.hp_regen})   | {15 * player.upgrade_price_multipliers[0]} gold   					

---ATTACK----
3. +2 damage ({player.damage}   | {20 * player.upgrade_price_multipliers[1]} gold  
4. +2.5% crit chance ({player.crit_chance * 100}%)   | {30 * player.upgrade_price_multipliers[1]} gold  

----MAGIC----
5. +5 max MP ({player.max_mp})   | {10 * player.upgrade_price_multipliers[2]} gold  
6. +4 MP regen ({player.mp_regen})   | {15 * player.upgrade_price_multipliers[2]} gold  ''',
	                  7)

	if inp == 0:
		if player.gold >= 10 * player.upgrade_price_multipliers[0]:
			player.max_hp += 10
			player.gold -= 10 * player.upgrade_price_multipliers[0]
			player.upgrade_price_multipliers[0] += 0.5
		else:
			print('You dont have enough gold!')
	elif inp == 1:
		if player.gold >= 15 * player.upgrade_price_multipliers[0]:
			player.hp_regen += 2
			player.gold -= 15 * player.upgrade_price_multipliers[0]
			player.upgrade_price_multipliers[0] += 0.5
		else:
			print('You dont have enough gold!')
	elif inp == 2:
		if player.gold >= 20 * player.upgrade_price_multipliers[1]:
			player.damage += 2
			player.gold -= 20 * player.upgrade_price_multipliers[1]
			player.upgrade_price_multipliers[1] += 0.5
		else:
			print('You dont have enough gold!')
	elif inp == 3:
		if player.gold >= 30 * player.upgrade_price_multipliers[1]:
			player.crit_chance += 0.025
			player.gold -= 30 * player.upgrade_price_multipliers[1]
			player.upgrade_price_multipliers[1] += 0.5
		else:
			print('You dont have enough gold!')
	elif inp == 4:
		if player.gold >= 10 * player.upgrade_price_multipliers[2]:
			player.max_mp += 5
			player.gold -= 10 * player.upgrade_price_multipliers[2]
			player.upgrade_price_multipliers[2] += 0.5
		else:
			print('You dont have enough gold!')
	elif inp == 5:
		if player.gold >= 15 * player.upgrade_price_multipliers[2]:
			player.mp_regen += 4
			player.gold -= 15 * player.upgrade_price_multipliers[2]
			player.upgrade_price_multipliers[2] += 0.5
		else:
			print('You dont have enough gold!')


def stats_menu():
	print(f'''
{'=' * 20}
Max HP - {player.max_hp}
HP regen - {player.hp_regen}
Max MP - {player.max_mp}
MP regen - {player.mp_regen}
Damage - {player.damage}
Crit Chance - {player.crit_chance * 100}%''')


{'=' * 20}


def inventory():
	if not player.inventory:
		print('Your inventory is empty!')
		print('=' * 20)
		return

	if player.has_consumed_item:
		print("You've already used an item this turn!")
		return

	print('=' * 20)

	for i, item in enumerate(player.inventory, start=1):
		print(f'{i}. {item.name}')
	print('=' * 20)
	inp = input_index('', len(player.inventory))
	player.use_item(inp - 1)


def explore():
	enemy_list = []
	fight_type = random.choices(enemies.fight_types, weights=fight_types_weights)[0]
	if fight_type == 'random':
		enemy_list = []
		enemy_count = random.choices(enemies.amount_of_enemies, weights=amount_of_enemies_weights)
		for i in range(enemy_count[0]):
			enemy_type = random.choices(enemies_list, weights=enemies_list_weights)
			enemy_class = enemy_type[0]
			enemy_list.append(enemy_class())
		return enemy_list
	elif fight_type == 'scenario':
		scenario = random.choices(fight_scenarios, weights=fight_scenarios_weights)[0]
		for enemy in scenario:
			enemy_list.append(enemy())

		return enemy_list
	else:
		raise Exception('invalid fight type')


def game_over():
	print('game over')
	raise SystemExit


def is_fight_over(enemy_list):
	for enemy in enemy_list:
		if not enemy.is_dead():
			return False
	return True


def end_of_fight(enemy_list):
	gold_drop = player.calculate_drop_gold(enemy_list)
	player.mp = min(player.max_mp, player.mp + player.mp_regen)
	player.hp = min(player.max_hp, player.hp + player.hp_regen)
	print('=' * 20)
	print('You win!')
	print(f'You collected {gold_drop} gold!')
	print('=' * 20)


def after_players_action(enemy_list, current_enemy):
	player.take_damage(current_enemy.damage)
	handle_cooldowns()
	player.mp = min(player.max_mp, player.mp + player.mp_regen)
	player.hp = min(player.max_hp, player.hp + player.hp_regen)
	print(f'{"-" * 20}\nYou got hit by {current_enemy.name} for {current_enemy.damage} damage!')
	print('=' * 20)


def print_spell_inventory():
	print('=' * 20)

	if not player.spell_inventory:
		print(f'You have not spells yet!')
		print('=' * 20)

	for i, spell in enumerate(player.spell_inventory, start=1):
		if spell.current_cooldown > 0:
			print(f'{i}. {spell.name} | Cooldown: {spell.current_cooldown}')
		else:
			print(f'{i}. {spell.name}')
	print('=' * 20)


def campfire_menu():
	player.has_consumed_item = False
	player.mp = player.max_mp
	inp = input_index(f'''
{'=' * 20}
{"-" * 6}CAMPFIRE{"-" * 6}
{'=' * 20}
HP: {player.hp} | $: {player.gold}

1. explore      4. spells      7. kick a pebble. (dont)
2. inventory    5. enter shop
3. upgrades     6. stats
''', 7)

	if inp == 0:
		enemy_list = explore()
		show_fight_menu(enemy_list)
		if player.is_dead():
			game_over()
		else:
			end_of_fight(enemy_list)
	elif inp == 1:
		inventory()
	elif inp == 2:
		upgrade_menu()
	elif inp == 3:
		print_spell_inventory()
	elif inp == 4:
		shop()
	elif inp == 5:
		stats_menu()
	elif inp == 6:
		print('\n' * 10)
		print('-' * 20)
		print('The pebble you decided to kick out of boredom suddenly GROWS OUT LIMBS AND ARISES FROM THE GROUND?!')
		print('THE PEBBLE HAS AWOKEN.')
		print('-' * 20)
		show_fight_menu([enemies.The_Pebble()])


def show_fight_menu(enemy_list):
	# A B C D E
	#   ^
	#
	enemy_order = enemy_list[:]
	alive_enemies = enemy_list[:]

	while enemy_order and alive_enemies and not player.is_dead():
		current_enemy = enemy_order.pop(0)
		while enemy_order and current_enemy.is_dead():
			current_enemy = enemy_order.pop(0)

		if fight_turn(alive_enemies, current_enemy):
			player.has_consumed_item = False

		alive_enemies = [enemy for enemy in alive_enemies if not enemy.is_dead()]

		if not enemy_order:
			enemy_order = alive_enemies[:]


def fight_turn(enemy_list, current_enemy):
	damage = player.damage
	print('\n' + '=' * 20)
	for i, enemy in enumerate(enemy_list, start=1):
		print(f'{i}. {enemy.name} | {enemy.hp} HP | {enemy.damage} DMG')
	print('-' * 20)
	inp = input_index(f"""
1. attack      e) exit
2. spell
3. item

{"-" * 20}
HP: {player.hp} | MP: {player.mp} | $: {player.gold}
{'=' * 20}
""", 3)

	if inp == 0:
		crit = random.random()

		if crit <= player.crit_chance:
			damage = damage * 2

		if len(enemy_list) > 1:
			target = choose_target_menu(enemy_list)
			if target:
				target_name = target.name
				target.take_damage(damage)
		else:
			print('=' * 20)

			target_name = current_enemy.name
			current_enemy.take_damage(damage)

		if not crit <= player.crit_chance:
			print(f'{"=" * 20}\nYou hit {target_name} for {damage} damage!')
		else:
			print(f'{"=" * 20}\nYou hit {target_name} for {damage} damage! Critical hit!')

		if not is_fight_over(enemy_list):
			after_players_action(enemy_list, current_enemy)

		return True
	elif inp == 1:
		if cast_spell(enemy_list):
			if not is_fight_over(enemy_list):
				after_players_action(enemy_list, current_enemy)
			return True
		else:
			return False
	elif inp == 2:
		inventory()


# player related stuff


player = Player()

if __name__ == "__main__":
	while True:
		campfire_menu()

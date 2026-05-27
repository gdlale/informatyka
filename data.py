from ui import choose_target_menu


class Item:
	name = None

	def __init__(self):
		pass

	def use(self, player):
		# jezeli zwroci True to przedmiot zostal uzyty i gracz nie powinien uzyc kolejnego
		raise NotImplementedError


class Small_Heal_Potion(Item):
	def __init__(self):
		super().__init__()
		self.name = "Small Heal Potion"

	def use(self, player):
		player.hp = min(player.hp + 20, player.max_hp)
		return True


class Big_Heal_Potion(Item):
	def __init__(self):
		super().__init__()
		self.name = "Big Heal Potion"

	def use(self, player):
		player.hp = min(player.hp + 50, player.max_hp)
		return True


class Spell:
	mp_cost = None
	name = None
	cooldown = 0
	is_attack_spell = None

	def __init__(self):
		self.current_cooldown = 0

	def use(self, player, enemies):
		raise NotImplementedError

	def is_on_cooldown(self):
		if self.current_cooldown == 0:
			return False
		else:
			return True

	def max_out_cooldown(self):
		self.current_cooldown = self.cooldown

	def reduce_cooldown(self):
		self.current_cooldown = max(0, self.current_cooldown - 1)


class Fireball(Spell):
	name = "Fireball"
	mp_cost = 15
	damage = 20
	cooldown = 3
	is_attack_spell = True

	def use(self, player, enemies):
		for target in enemies:
			target.take_damage(self.damage)
		print(f'You hit ALL ENEMIES for {self.damage} damage! ')


class Heal(Spell):
	name = "Heal"
	mp_cost = 20
	heal_amount = 25
	cooldown = 2
	is_attack_spell = False

	def use(self, player, enemies):
		player.hp = min(player.hp + self.heal_amount, player.max_hp)

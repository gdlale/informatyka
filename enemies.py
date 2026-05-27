import random


class Enemy:
	base_name = ''

	def __init__(self):
		self.hp = None
		self.damage = None
		self.gold_drop = []
		self.prefix1 = (
			'BIG', 'SMALL', 'CHUBBY', 'THIN', 'OLD', 'QUICK', 'ENORMOUS', 'TINY', 'SHORT', 'TALL', 'STUMPY', 'WEAK',
			'JACKED', 'SLUGGISH', 'AGILE', 'FRAGILE', 'STIFF')
		self.prefix2 = (
			'MAD', 'RED', 'YELLOW', 'CRAZY', 'BLACK', 'GINGER', 'PALE', 'FILTHY', 'STICKY', 'DUMB',
			'STINKY', 'SLIMY')

		self.name = self.namegen()

	def take_damage(self, damage):
		self.hp -= damage
		if self.hp <= 0:
			print(f'{self.name} is dead!')

	def is_dead(self):
		return self.hp <= 0

	def namegen(self):
		name = []
		name.append(random.choice(self.prefix1))
		name.append(random.choice(self.prefix2))
		name.append(self.base_name)
		return ' '.join(name)


class Slime(Enemy):
	base_name = 'SLIME'

	def __init__(self):
		super().__init__()
		self.hp = 20
		self.damage = 5
		self.gold_drop = [5, 10]


class Goblin(Enemy):
	base_name = 'GOBLIN'

	def __init__(self):
		super().__init__()
		self.hp = 30
		self.damage = 5
		self.gold_drop = [8, 13]


class Skeleton(Enemy):
	base_name = 'SKELETON'

	def __init__(self):
		super().__init__()
		self.hp = 50
		self.damage = 10
		self.gold_drop = [10, 15]


class Troll(Enemy):
	base_name = 'TROLL'

	def __init__(self):
		super().__init__()
		self.hp = 50
		self.damage = 15
		self.gold_drop = [13, 18]


class Rat(Enemy):
	base_name = 'RAT'

	def __init__(self):
		super().__init__()
		self.hp = 10
		self.damage = 5
		self.gold_drop = [3, 7]


class The_Pebble(Enemy):
	base_name = 'SUPRISINGLY DANGEROUS ALIVE SELF CONCIOUS PEBBLE'

	def __init__(self):
		super().__init__()
		self.hp = 100
		self.damage = 30
		self.gold_drop = [50, 150]
		self.name = 'SUPRISINGLY DANGEROUS ALIVE SELF CONCIOUS PEBBLE'


fight_types = ['random', 'scenario']
fight_types_weights = [9, 1]

amount_of_enemies = [1, 2, 3, 4]
amount_of_enemies_weights = [3, 4, 2, 1]

enemies_list = [Rat, Slime, Goblin, Skeleton, Troll]
enemies_list_weights = [3, 2.5, 2.5, 1.5, 1.5]

fight_scenarios = [[Rat, Rat, Rat, Rat, Rat, Rat]]
fight_scenarios_weights = [1]

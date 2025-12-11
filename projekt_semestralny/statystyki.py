HP = 0
ATAK = 1
CEBULION = 2  # tylko do gracza
ARMOR = 3
MAX_HP = 4  # tylko do gracza
DODGE_CHANCE = 5
swiat = 1
IMIE = 4  # tylko do wrogów
HELM = 6  # tylko do gracza
# gracz
gracz = [100, 10, 0, 1, 100, 0.8, 0]  # hp, atak, coiny, zbroja, szansa na unik
inv = []
# przeciwnicy
goblin = [30, 10, 2, 5, 'GOBLIN', 0.9]  # hp, atak, min drop, max drop, nazwa, szansa na unik
troll = [70, 20, 5, 15, 'TROLL', 0.85]
cyklop = [100, 30, 15, 25, 'CYKLOP', 0.8]
dawid = [160, 40, 30, 50, 'DAWID', 0.75]
# itemy
CENA = 2
NAZWA = 0  # tylko do itemow
ITEM_STAT = 1  # np. 50 hp przywraca
mikstura_heal = ('Mikstura leczenia (Przywraca 50HP)', 50, 3)
mikstura_maxhp = ['Mikstura witalności (Zwiększa max. HP o 25. można użyć tylko 2 razy. Leczy do nowego max. HP)', 25,
				  15, 1]
# generowanie nazw
prefix1 = (
	'DUŻY', 'MAŁY', 'GRUBY', 'CHUDY', 'STARY', 'SZYBKI', 'OGROMNY', 'WIELKI', 'MALUTKI', 'PĘKATY', 'NISKI', 'WYSOKI',
	'KRĘPY',
	'SŁABY', 'TĘGI', 'KOŚCIANY', 'NAPAKOWANY', 'POWOLNY', 'ZWINNY', 'WYROŚNIĘTY', 'MOCARNY', 'KRUCHY', 'SZTYWNY',
	'PRZYGARBIONY')

prefix2 = (
	'WŚCIEKŁY', 'CZERWONY', 'ŻÓŁTY', 'SZALONY', 'CZARNY', 'RUDY', 'BLADY', 'BRUDNY', 'LEPKI', 'TĘPY', 'PRYSZCZATY',
	'ŚMIERDZĄCY', 'ŚLISKI', 'KRZYCZĄCY',)
suffix = ('BEZ RĘKI', 'BEZ NOGI', 'BEZ OKA')

# inne
line = '-' * 30

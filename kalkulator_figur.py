import math

print("""
a - pole
b - obwod
c - objetosc
d - pole powierzchni
f - inne""")

inp = input()

if inp == 'a':
	print("""
	a - pole kwadratu
	b - pole prostokatu
	c - pole rownolegloboku
	d - pole trapezu
	e - pole trojkata
	f - pole trojkata rownobocznego
	g - pole kola
	h - pole rombu
	i - pole rombu (przekatne)""")

	inp = input()

	if inp == 'a':
		a = float(input("a = "))
		print(f'pole kwadratu to {a**2}')

	elif inp == 'b':
		a = float(input("a = "))
		b = float(input("b = "))
		print(f'pole prostokatu to {a * b}')

	elif inp == 'c':
		a = float(input("a = "))
		h = float(input("h = "))
		print(f'pole rownolegloboku to {a * h}')
	elif inp == "d":
		a = float(input("a = "))
		b = float(input("b = "))
		h = float(input("h = "))
		print(f'pole trapezu to {((a + b) * h) / 2}')
	elif inp == "e":
		a = float(input("a = "))
		h = float(input("h = "))
		print(f'pole trojkata to {(a* h) / 2}')
	elif inp == "f":
		a = float(input("a = "))
		print(f'pole trojkata rownobocznego to {(a**2 * math.sqrt(3)/4)}')
	elif inp == "g":
		r = float(input("r = "))
		print(f'pole kola to {math.pi * r**2}')
	elif inp == "h":
		a = float(input("a = "))
		h = float(input("h = "))
		print(f'pole rombu to {a*h}')
	elif inp == "i":
		e = float(input("e = "))
		f = float(input("f = "))
		print(f'pole trapezu to {(e*f)/2}')

elif inp == 'b':
	print("""
	a - obwod kwadratu
	b - obwod prostokatu
	c - obwod rownolegloboku
	d - obwod trapezu
	e - obwod trojkata
	f - obwod trojkata rownobocznego
	g - obwod kola
	h - obwod rombu""")

	inp = input()

	if inp == "a":
		a = float(input("a = "))
		print(f'obwod kwadratu to {4*a}')
	elif inp == "b":
		a = float(input("a = "))
		b = float(input("b = "))
		print(f'obwod prostokatu to {2*a + 2*b}')
	elif inp == "c":
		a = float(input("a = "))
		b = float(input("b = "))
		print(f'obwod rownolegloboku to to {2*a + 2*b}')
	elif inp == "d":
		a = float(input("a = "))
		b = float(input("b = "))
		c = float(input("c = "))
		d = float(input("d = "))
		print(f'obwod trapezu to {a+b+c+d}')
	elif inp == "e":
		a = float(input("a = "))
		b = float(input("b = "))
		c = float(input("c = "))
		print(f'obwod trojkota to {a + b + c}')
	elif inp == "f":
		a = float(input("a = "))
		print(f'obwod trojkata rownobocznego to {3*a}')
	elif inp == "g":
		r = float(input("r = "))
		print(f'obwod kola to {2 * math.pi * r}')
	if inp == "h":
		a = float(input("a = "))
		print(f'obwod rombu to {4*a}')

elif inp == 'c':
	print("""
	a - objetosc szescianu
	b - objetosc prostopadloscianu
	c - objetosc graniastoslupa
	d - objetosc ostroslupa
	e - objetosc walca
	f - objetosc stozka
	g - objetosc kuli
	""")

	inp = input()

	if inp == "a":
		a = float(input("a = "))
		print(f'objetosc szescianu to {a**3}')
	elif inp == "b":
		a = float(input("a = "))
		b = float(input("b = "))
		c = float(input("c = "))
		print(f'objetosc szescianu to {a*b*c}')
	elif inp == "c":
		pp = float(input("pp = "))
		h = float(input("h = "))
		print(f'objetosc graniastoslupa to {pp*h}')
	elif inp == "d":
		pp = float(input("pp = "))
		h = float(input("h = "))
		print(f'objetosc ostroslupa to {(pp*h)/3}')
	elif inp == "e":
		r = float(input("r = "))
		h = float(input("h = "))
		print(f'objetosc walca to {math.pi * r**2 * h}')
	elif inp == "f":
		r = float(input("r = "))
		h = float(input("h = "))
		print(f'objetosc stozka to {(math.pi * r**2 * h)/3}')
	elif inp == "g":
		r = float(input("r = "))
		print(f'objetosc kuli to {(math.pi * r**3) * (4/3) }')


elif inp == 'd':
	print("""
	a - pole powierzchni szescianu
	b - pole powierzchni prostopadloscianu
	c - pole powierzchni graniastoslupa
	d - pole powierzchni ostroslupa
	e - pole powierzchni walca
	f - pole powierzchni stozka
	g - pole powierzchni kuli""")

	inp = input()

	if inp == "a":
		a = float(input("a = "))
		print(f'pole powierzchni szescianu to {6 * a**2}')
	elif inp == "b":
		ab = float(input("ab = "))
		ac = float(input("ac = "))
		bc = float(input("bc = "))
		print(f'pole powierzchni prostopadloscianu to {2 * ab + 2 * ac + 2 * bc}')
	elif inp == "c":
		pb = float(input("pb = "))
		pp = float(input("pp = "))
		print(f'pole powierzchni graniastoslupa to {2 * pp + pb}')
	elif inp == "d":
		pb = float(input("pb = "))
		pp = float(input("pp = "))
		print(f'pole powierzchni ostroslupa to {pp + pb}')
	elif inp == "e":
		r = float(input("r = "))
		h = float(input("h = "))
		print(f'pole powierzchni walca to {2*math.pi * r**2 + 2 * math.pi * r * h}')
	elif inp == "f":
		r = float(input("r = "))
		l = float(input("l = "))
		print(f'pole powierzchni stozka to {math.pi * r**2 + math.pi*r*l}')
	elif inp == "g":
		r = float(input("r = "))
		print(f'pole powierzchni kuli to {4 * math.pi * r**2}')

elif inp == 'f':
	print("""
	a - wysokosc trojkata rownobocznego
	b - przekatna kwadratu
	c - twierdzenie pitagorasa""")

	inp = input()

	if inp == "a":
		a = float(input("a = "))
		print(f'wysokosc trojkata rownobocznego to {(a * math.sqrt(3)/2)}')
	elif inp == "b":
		a = float(input("a = "))
		print(f'przekatna kwadratu to {a * math.sqrt(2)}')
	elif inp == "c":
		a = float(input("a = "))
		b = float(input("b = "))
		c = float(input("c = "))
		print(f'dlugosc przeciwprostokatnej to {a**2 + b**2}')


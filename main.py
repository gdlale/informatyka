import random as rand



pola = ['0','1','2','3','4','5','6','7','8']


playercharacter = 'X'
botcharacter = '○'


def plansza():
    print(f"""
    {pola[0]}  {pola[1]}  {pola[2]}
    {pola[3]}  {pola[4]}  {pola[5]}
    {pola[6]}  {pola[7]}  {pola[8]}""")

def botrandommove():
    if plansza_pelna():
        return
    while True:
        botmove = rand.randint(0,8)
        if not pola[int(botmove)].isdigit():
            continue
        else:
            pola[int(botmove)] = botcharacter
            break

def plansza_pelna():
    for x in pola:
        if x.isdigit():
            return False
    return True

def sprawdz_wina():
    for i in range(3):
        p = i * 3
        if pola[p] == pola[p+1] == pola[p+2]:
            print(f'{pola[p]} WYGRYWA')
            return True
    for i in range(3):
        p = i
        if pola[p] == pola[p+3] == pola[p +6]:
            print(f'{pola[p]} WYGRYWA')
            return True
    if (pola[0] == pola[4] == pola[8]) or (pola[2] == pola[4] == pola[6]):
        print(f'{pola[4]} WYGRYWA')
        return True
    return False


def calculate_score(index):

    if not pola[index].isdigit():
        return -1000

    c = index % 3
    r = (index // 3)*3

    col = pola[c::3]
    row = pola[r:r+3]
    plp = ppl = bpl = blp = 0

    if index in (0, 4, 8):
        plp = pola[0::4].count(playercharacter)
        blp = pola[0::4].count(botcharacter)

    if index in (2, 4, 6):
        ppl = pola[2:8:2].count(playercharacter)
        bpl = pola[2:8:2].count(botcharacter)


    pr = row.count(playercharacter)
    pc = col.count(playercharacter)
    bc = col.count(botcharacter)
    br = row.count(botcharacter)

    if pc == 2 or pr == 2 or bc == 2 or br == 2 or plp == 2 or ppl == 2 or bpl == 2 or blp == 2:
        score = 1000 + bc + br +bpl +blp
    else:
        score = (pr + pc + ppl + plp) + (bc + br + blp + bpl) * 2

    return score


def botaimove():
    scores = []

    for i in range(9):
        score = calculate_score(i)
        scores.append(score)

    max_score = max(scores)
    top = []
    for i in range(9):
        if scores[i] == max_score:
            top.append(i)

    pola[rand.choice(top)] = botcharacter


def main():
    print(f'TY: {playercharacter}     BOT: {botcharacter}')

    plansza()
    while True:
        if plansza_pelna():
            break
        move = input(f"twój ruch (jestes {playercharacter}): ")
        try:
            move = int(move)
            if move < 0 or move > 8:
                raise ValueError()
        except ValueError:
            continue

        if not pola[move].isdigit():
            print('To pole jest już zajęte.')
            continue
        else:
            pola[int(move)] = playercharacter
            if sprawdz_wina():
                break
            botaimove()
            if sprawdz_wina():
                break
            plansza()
    plansza()

main()

# plansza, walidacja
# statki, komentarz kiedy jest zatopiony, życie/rozmiar
# strzaly
# zasady umiejscowie, strzałow, kiedy sie konczy,

# 0 1 2 3
#A
#B
import random

tab = []

LETTERS = 'ABCDEFGHIJ'


def board():
    for i in range(10):
        tab2 = []
        for j in range(10):
            tab2.append(LETTERS[i] + str(j))
        tab.append(tab2)


def get_board():
    for i in tab:
        for j in i:
            print(j, end=' ')
        print()
    print()


def shots():
    if 'A0' in tab:
        print('AO')
#sprawdzic, czy jest na zajetym polu = zrobione
#sprawdzic, czy jest inny obok = zrobione
#sprawdzic, czy nie wychodzi za tablice


def ships(x, y, size, direct):
    position_of_letter = LETTERS.find(x.upper())

    if tab[position_of_letter][y] == '# ':
        res = False
        return res
    else:
        res = True
        res = ships_y(x, y, size, direct) and ships_x(x, y, size, direct)
        return res
    print(ships_y(x, y, size, direct))
    print(ships_x(x, y, size, direct))


def ships_y(x, y, size, direct):
    position_of_letter = LETTERS.find(x.upper())
    if y == 9:
        if tab[position_of_letter][y - 1] == '# ':
            res = False
        else:
            tab[position_of_letter][y] = '# '
            res = True
            get_board()
        return res
    if y < 9:
        if tab[position_of_letter][y - 1] == '# ' or tab[position_of_letter][y + 1] == '# ':
            res = False
        else:
            tab[position_of_letter][y] = '# '
            res = True
            get_board()
        return res


def ships_x(x, y, size, direct):
    position_of_letter = LETTERS.find(x.upper())
    if position_of_letter == 9:
        if tab[position_of_letter - 1][y] == '# ':
            res = False
        else:
            tab[position_of_letter][y] = '# '
            res = True
            get_board()
        return res
    if position_of_letter < 9:
        if tab[position_of_letter - 1][y] == '# ' and tab[position_of_letter + 1][y] == '# ':
            res = False
        else:
            tab[position_of_letter][y] = '# '
            res = True
            get_board()
        return res


def get_ships():
    i = 0
    while i < 50:
        x = LETTERS[random.randint(0, 9)]
        y = random.randint(0, 9)
        result = ships(x, y, 1, 'up')
        if result:
            i += 1

    i = 0
    while i < 3:
        x = LETTERS[random.randint(0, 9)]
        y = random.randint(0, 9)
        result = ships(x, y, 2, 'up')
        if result:
            i += 1

    i = 0
    while i < 2:
        x = LETTERS[random.randint(0, 9)]
        y = random.randint(0, 9)
        result = ships(x, y, 3, 'up')
        if result:
            i += 1

    i = 0
    while i < 1:
        x = LETTERS[random.randint(0, 9)]
        y = random.randint(0, 9)
        result = ships(x, y, 4, 'up')
        if result:
            i += 1

board()
get_ships()
#shots()

#ships('j', 5, 1, 'up')
#ships('a', 7, 1, 'up')
#ships('b', 3, 1, 'up')
#get_board()
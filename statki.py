# plansza, walidacja
# statki, komentarz kiedy jest zatopiony, życie/rozmiar
# strzaly
# zasady umiejscowie, strzałow, kiedy sie konczy,
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


def is_cord_valid(cord):
    return 0 <= cord <= 9


def is_pos_taken(x, y):
    return tab[x][y] == '# '


def is_pos_valid(x, y):
    if is_cord_valid(x) is False or is_cord_valid(y) is False:
        return False
    if is_pos_taken(x, y) is True:
        return False
    if is_cord_valid(x - 1) is True:
        if is_pos_taken(x - 1, y) is True:
            return False
    if is_cord_valid(x + 1) is True:
        if is_pos_taken(x + 1, y) is True:
            return False
    if is_cord_valid(y - 1) is True:
        if is_pos_taken(x, y - 1) is True:
            return False
    if is_cord_valid(y + 1) is True:
        if is_pos_taken(x, y + 1) is True:
            return False
    if is_cord_valid(x - 1) is True and is_cord_valid(y - 1) is True:
        if is_pos_taken(x - 1, y - 1) is True:
            return False
    if is_cord_valid(x + 1) is True and is_cord_valid(y - 1) is True:
        if is_pos_taken(x + 1, y - 1) is True:
            return False
    if is_cord_valid(x + 1) is True and is_cord_valid(y + 1) is True:
        if is_pos_taken(x + 1, y + 1) is True:
            return False
    if is_cord_valid(x - 1) is True and is_cord_valid(y + 1) is True:
        if is_pos_taken(x - 1, y + 1) is True:
            return False
    return True


def free_place():
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            if is_pos_valid(i, j):
                return True
    return False


def get_ships():
    for i in range(15):
        if free_place():
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            while not is_pos_valid(x, y):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
            tab[x][y] = '# '


    # i = 0
    # while i < 3:
    #     x = LETTERS[random.randint(0, 9)]
    #     y = random.randint(0, 9)
    #     result = ships(x, y, 2, 'up')
    #     if result:
    #         i += 1
    #
    # i = 0
    # while i < 2:
    #     x = LETTERS[random.randint(0, 9)]
    #     y = random.randint(0, 9)
    #     result = ships(x, y, 3, 'up')
    #     if result:
    #         i += 1
    #
    # i = 0
    # while i < 1:
    #     x = LETTERS[random.randint(0, 9)]
    #     y = random.randint(0, 9)
    #     result = ships(x, y, 4, 'up')
    #     if result:
    #         i += 1

board()
get_ships()
get_board()
free_place()
#shots()

#ships('j', 5, 1, 'up')
#ships('a', 7, 1, 'up')
#ships('b', 3, 1, 'up')
#get_board()
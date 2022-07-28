# statki: 2,3,4 polowe. dodanie wielkosci i kierunku gdzie go postawic. sprawdzenie czy da sie go postawic
# strzały: wybranie pola podanego przez gracza i sprawdzenie czy jest tam statek
# zasady gry: gracz ma 10 strzałow, jesli trafi w statek ma kolejny strzal, jesli nie trafi traci 1 zycie
# jesli bezdie to statek 1 polowy, przy pierwszym strzale jest zatopiony
# reszta musi dac jakis znak ze nie jest zatopiona i dalej zyje a jak sie zatopi to tez jakis znak
# plansza wyswietlenie: musi byc cala druga plansza pusta i gracz ma strzelac w nia, po strzale wyswietla pole czy jest
# trafione czy nie + wyswietla ilosc pozostalychstrzalow


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


def choose_random():
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    return x, y


def ship_direction(x, y):
    directions = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    random_cord = random.choice(directions)
    if random_cord == (x - 1, y):
        return 'Down'
    if random_cord == (x + 1, y):
        return 'Up'
    if random_cord == (x, y - 1):
        return 'Left'
    if random_cord == (x, y + 1):
        return 'Right'


def get_ships():

    for i in range(4):
        if free_place():
            x, y = choose_random()
            while not is_pos_valid(x, y):
                x, y = choose_random()
            tab[x][y] = '# '

    for i in range(3):
        x, y = choose_random()
        random_cord = ship_direction(x, y)
        if random_cord == 'Down':
            while not is_pos_valid(x, y) or not is_pos_valid(x - 1, y):
                x, y = choose_random()

            tab[x][y] = '# '
            tab[x - 1][y] = '# '
        if random_cord == "Up":
            while not is_pos_valid(x, y) or not is_pos_valid(x + 1, y):
                x, y = choose_random()

            tab[x][y] = '# '
            tab[x + 1][y] = '# '
        if random_cord == "Left":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y - 1):
                x, y = choose_random()

            tab[x][y] = '# '
            tab[x][y - 1] = '# '
        if random_cord == "Right":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y + 1):
                x, y = choose_random()

            tab[x][y] = '# '
            tab[x][y + 1] = '# '

    for i in range(2):
        x, y = choose_random()
        random_cord = ship_direction(x, y)
        if random_cord == 'Down':
            while not is_pos_valid(x, y) or not is_pos_valid(x - 1, y) or not is_pos_valid(x - 2, y):
                x, y = choose_random()

            tab[x][y] = '# '
            tab[x - 1][y] = '# '
            tab[x - 2][y] = '# '
        if random_cord == "Up":
            while not is_pos_valid(x, y) or not is_pos_valid(x + 1, y) or not is_pos_valid(x + 2, y):
                x, y = choose_random()

            tab[x][y] = '# '
            tab[x + 1][y] = '# '
            tab[x + 2][y] = '# '
        if random_cord == "Left":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y - 1) or not is_pos_valid(x, y - 2):
                x, y = choose_random()

            tab[x][y] = '# '
            tab[x][y - 1] = '# '
            tab[x][y - 2] = '# '
        if random_cord == "Right":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y + 1) or not is_pos_valid(x, y + 2):
                x, y = choose_random()

            tab[x][y] = '# '
            tab[x][y + 1] = '# '
            tab[x][y + 2] = '# '

    # up = x - 1, y
    # down= x + 1, y
    # right = x, y + 1
    # left = x, y - 1
    #
    # up = x - 1, y, x - 2, y
    # down = x + 1, y, x + 2, y,
    # right = x, y + 1, right = x, y + 2
    # left = x, y - 1, x, y - 2,
    #
    # up = x - 1, y up = x - 2, y up = x - 3, y
    # down = x + 1, y  down = x + 2, y  down = x + 3, y
    # right = x, y + 1 right = x, y + 2 right = x, y + 3
    # left = x, y - 1 left = x, y - 2 left = x, y - 3



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
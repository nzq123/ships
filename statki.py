import random

tab = []

game_tab = []

ship_tab = []

LETTERS = 'ABCDEFGHIJ'

SHIP_SYMBOL = '🔥 '

SHIP_MISS = 'X '


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


def game_board():
    for i in range(10):
        tab2 = []
        for j in range(10):
            tab2.append(LETTERS[i] + str(j))
        game_tab.append(tab2)


def get_game_board():
    for i in game_tab:
        for j in i:
            print(j, end=' ')
        print()
    print()


def ships_left():
    res = 0
    for i in ship_tab:
        for j in i:
            if len(j) != 0:
                res += 1
    return res != 0


def is_cord_valid(cord):
    return 0 <= cord <= 9


def is_pos_taken(x, y):
    return tab[x][y] == SHIP_SYMBOL


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


def shots(x, y):
    if game_tab[x][y] == SHIP_MISS or game_tab[x][y] == SHIP_SYMBOL:
        print("Już strzelałeś w te pole")
        return True
    elif is_pos_taken(x, y):
        return True
    else:
        print('Pudło')
        return False


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

    for i in range(1):
        x, y = choose_random()
        random_cord = ship_direction(x, y)
        if random_cord == 'Down':
            while not is_pos_valid(x, y) or not is_pos_valid(x - 1, y) or not is_pos_valid(x - 2, y) \
                    or not is_pos_valid(x - 3, y):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x - 1][y] = SHIP_SYMBOL
            tab[x - 2][y] = SHIP_SYMBOL
            tab[x - 3][y] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x - 1, y), (x - 2, y), (x - 3, y)])
        if random_cord == "Up":
            while not is_pos_valid(x, y) or not is_pos_valid(x + 1, y) or not is_pos_valid(x + 2, y) \
                    or not is_pos_valid(x + 3, y):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x + 1][y] = SHIP_SYMBOL
            tab[x + 2][y] = SHIP_SYMBOL
            tab[x + 3][y] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x + 1, y), (x + 2, y), (x + 3, y)])
        if random_cord == "Left":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y - 1) or not is_pos_valid(x, y - 2) \
                    or not is_pos_valid(x, y - 3):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x][y - 1] = SHIP_SYMBOL
            tab[x][y - 2] = SHIP_SYMBOL
            tab[x][y - 3] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x, y - 1), (x, y - 2), (x, y - 3)])
        if random_cord == "Right":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y + 1) or not is_pos_valid(x, y + 2) \
                    or not is_pos_valid(x, y + 3):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x][y + 1] = SHIP_SYMBOL
            tab[x][y + 2] = SHIP_SYMBOL
            tab[x][y + 3] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x, y + 1), (x, y + 2), (x, y + 3)])

    for i in range(2):
        x, y = choose_random()
        random_cord = ship_direction(x, y)
        if random_cord == 'Down':
            while not is_pos_valid(x, y) or not is_pos_valid(x - 1, y) or not is_pos_valid(x - 2, y):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x - 1][y] = SHIP_SYMBOL
            tab[x - 2][y] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x - 1, y), (x - 2, y)])
        if random_cord == "Up":
            while not is_pos_valid(x, y) or not is_pos_valid(x + 1, y) or not is_pos_valid(x + 2, y):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x + 1][y] = SHIP_SYMBOL
            tab[x + 2][y] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x + 1, y), (x + 2, y)])
        if random_cord == "Left":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y - 1) or not is_pos_valid(x, y - 2):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x][y - 1] = SHIP_SYMBOL
            tab[x][y - 2] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x, y - 1), (x, y - 2)])
        if random_cord == "Right":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y + 1) or not is_pos_valid(x, y + 2):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x][y + 1] = SHIP_SYMBOL
            tab[x][y + 2] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x, y + 1), (x, y + 2)])

    for i in range(3):
        x, y = choose_random()
        random_cord = ship_direction(x, y)
        if random_cord == 'Down':
            while not is_pos_valid(x, y) or not is_pos_valid(x - 1, y):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x - 1][y] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x - 1, y)])
        if random_cord == "Up":
            while not is_pos_valid(x, y) or not is_pos_valid(x + 1, y):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x + 1][y] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x + 1, y)])
        if random_cord == "Left":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y - 1):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x][y - 1] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x, y - 1)])
        if random_cord == "Right":
            while not is_pos_valid(x, y) or not is_pos_valid(x, y + 1):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            tab[x][y + 1] = SHIP_SYMBOL
            ship_tab.append([(x, y), (x, y + 1)])

    for i in range(4):
        if free_place():
            x, y = choose_random()
            while not is_pos_valid(x, y):
                x, y = choose_random()
            tab[x][y] = SHIP_SYMBOL
            ship_tab.append([(x, y)])

    get_board()
    print()


board()
game_board()
get_ships()
free_place()


num_shots = 10
while num_shots > 0 and ships_left() is True:
    get_game_board()
    x = int(input("Podaj pierwsze współrzędne: "))
    y = int(input("Podaj drugie współrzędne: "))
    if shots(x, y) is True:
        for i in ship_tab:
            for j in i:
                if j[0] == x and j[1] == y:
                    game_tab[x][y] = SHIP_SYMBOL
                    ship_tab[ship_tab.index(i)].remove((x, y))
                    if len(i) != 0:
                        print('Trafiony')
                    else:
                        print('Zatopiony')
    else:
        game_tab[x][y] = SHIP_MISS
        num_shots -= 1
        print(f"Zostało Ci {num_shots} strzałów")

if ships_left() is False:
    print("Wygrałeś")
else:
    print("Przegrałeś")


import random

def rnd():
    return random.randint(0, 1)

def player():
    while True:
        num = input('Возьмите не более 28 конфет: ')
        if num.isdigit():
            if 0 < int(num) < 29:
                return int(num)

def pvp():
    candy = 2021
    player1 = input('Введите имя игрока 1: ')
    player2 = input('Введите имя игрока 2: ')
    if rnd():
        p1 = player1
        p2 = player2
    else:
        p1 = player2
        p2 = player1
    while candy > 0:
        print(f'Осталось {candy} конфет.')
        print(f'Ходит {p1}')
        candy -= player()
        if candy < 29:
            print(f'Осталось {candy} конфет. Игрок {p2} победил.')
            break
        print(f'Осталось {candy} конфет')
        print(f'Ходит {p2}')
        candy -= player()
        if candy < 29:
            print(f'{p1} победил.')
            break

def pvb():
    candy = 2021
    p = input('Введите свое имя: ')
    name_bot = 'Бот'

    while candy > 0:
        bot = random.randint(1, 28)
        print(f'Осталось {candy} конфет.')
        print(f'Ходит {name_bot}. Берет {bot} конфет')
        candy -= bot
        if candy < 29:
            print(f'Осталось {candy} конфет. Игрок {p} победил.')
            break
        print(f'Осталось {candy} конфет')
        print(f'Ходит {p}')
        candy -= player()
        if candy < 29:
            print(f'{name_bot} победил.')
            break
    while candy > 0:

        bot = random.randint(1, 28)

        print(f'Осталось {candy} конфет.')
        print(f'Ходит {name1}. Берет {player1} конфет')
        candy -= player1
        if candy < 29:
            print(f'Осталось {candy} конфет. Игрок {name2} победил.')
            break
        print(f'Осталось {candy} конфет')
        print(f'Ходит {name2}')
        candy -= player2
        if candy < 29:
            print(f'{player1} победил.')
            break


def p_v_ii():
    candy = 2021
    p = input('Введите свое имя: ')
    name_bot = 'ИИ'
    n = 28
    while candy > 0:
        ii = candy % (n + 1)
        if ii == 0:
            ii = random.randint(1, 28)
        print(f'Осталось {candy} конфет.')
        print(f'Ходит {name_bot}. Берет {ii} конфет')
        candy -= ii
        if candy < 29:
            print(f'Осталось {candy} конфет. Игрок {p} победил.')
            break
        print(f'Осталось {candy} конфет')
        print(f'Ходит {p}')
        candy -= player()
        if candy < 29:
            print(f'{name_bot} победил.')
            break

def game():
    start = True
    while start:

        print('''На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
Выберете с кем будете играть:
    Введите 1 если игра на 2 игроков
    Введите 2 если игра с компьютером на легкой сложности
    Введите 3 если игра с компьютером на тяжелой сложности
    Введите 0 чтобы выйти из игры''')

        mode = input('Выберите режим игры: ')
        if mode.isdigit():
            if 0 <= int(mode) < 4:
                mode = int(mode)

        if mode == 1:
            pvp()
        elif mode == 2:
            pvb()
        elif mode == 3:
            p_v_ii()
        elif mode == 0:
            start = False
    return f'До скорой встречи!'


print(game())
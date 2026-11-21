import math
import random

gameloop = True

einzeln = []

abcde = ['a', 'b', 'c', 'd', 'e']

feld = [
    [4, 2, 2, 2, 2],
    [4, 8, 8, 2, 4],
    [2, 2, 8, 8, 8],
    [128, 8, 2, 8, 2], 
    [4, 16, 16, 32, 64]
]

farben = ['1 gibt es nicht', '\033[30;42m', '\033[30;105m', '\033[30;101m', '\033[30;45m', '\033[30;46m', '\033[43m', '\033[47m']

def zufaelliges_feld():
    for y in range(len(feld)):
        for x in range(len(feld[y])):
            feld[y][x] = 2**random.randint(1, 4)

def farbe(n):
    if n == '':
        return '\033[0m'
    exponent = int(math.log(n) / math.log(2))
    farbe = farben[exponent]
    return farbe

def zahl(n):
    if len(str(n)) < 3:
        return ' ' + str(n).ljust(2, ' ')
    else:
        return str(n)

def ausgeben(feld):
    print('    A   B   C   D   E')
    for y in range(len(feld)):
        print('   -------------------')
        print(y + 1, end= ' ')
        for x in range(len(feld[y])):
            print('|' + farbe(feld[y][x]) + zahl(feld[y][x]), end= '\033[0m')
        print('|')
    print('   -------------------')

def auswerten():
    feld[y_koordinate][x_koordinate] = ''

def is_valid(inp):
    global einzeln
    einzeln = []
    if len(inp) != 2:
        print('Du kannst nur ein Kästchen auswählen.')
        return False
    for i in inp:
        einzeln.append(i)
    einzeln.sort()
    if not einzeln[0].isnumeric():
        print('Bitte gib die Zeile als Zahl ein.')
        return False
    if not einzeln[1].isalpha():
        print('Bitte gib die Spalte als Buchstabe ein.')
        return False
    if not einzeln[1] in abcde:
        print('Du kannst nur die Buchstaben a, b, c, d oder e eingeben.')
        return False
    if not 0 < int(einzeln[0]) < 6:
        print('Du kannst nur Zahlen zwischen 1 und 5 eingeben.')
        return False
    print(f'Du wählst das Feld: {einzeln[1]}{einzeln[0]}')
    return True

def user_input():
    global x_koordinate, y_koordinate
    eingabe = input('Welches Feld möchtest du auswählen? >> ').lower()
    while not is_valid(eingabe):
        eingabe = input('Welches Feld möchtest du auswählen? >> ').lower()
    x_koordinate = abcde.index(einzeln[1])
    y_koordinate = int(einzeln[0]) - 1

def spiel():
    ausgeben(feld)
    user_input()
    auswerten()


zufaelliges_feld()
while gameloop:
    spiel()

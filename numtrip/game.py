import math
import random

gameloop = True

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
    print('    1   2   3   4   5')
    for y in range(len(feld)):
        print('   -------------------')
        print(y + 1, end= ' ')
        for x in range(len(feld[y])):
            print('|' + farbe(feld[y][x]) + zahl(feld[y][x]), end= '\033[0m')
        print('|')
    print('   -------------------')

def auswerten():
    feld[y_koordinate][x_koordinate] = ''

def user_input_auswertung(n):
    global gameloop
    return int(n) - 1

def user_input():
    global x_koordinate, y_koordinate
    x_koordinate = user_input_auswertung(input('Gib die x (Links/Rechts) Koordinate ein (1-5): '))
    y_koordinate = user_input_auswertung(input('Gib die y (Hoch/Runter) Koordinate ein (1-5): '))

def spiel():
    user_input()
    auswerten()
    ausgeben(feld)


zufaelliges_feld()
ausgeben(feld)
while gameloop:
    spiel()
    

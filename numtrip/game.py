import math

feld = [
    [4, 2, 2, 2, 2],
    [4, 8, 8, 2, 4],
    [2, 2, 8, 8, 8],
    [8, 8, 2, 8, 2], 
    [4, 16, 16, 8, 4]
]

farben = ['1 gibt es nicht', '\033[30;42m', '\033[30;105m', '\033[30;101m', '\033[30;45m', '\033[30;46m']

def farbe(n):
    exponent = int(math.log(n) / math.log(2))
    farbe = farben[exponent]
    return farbe

def zahl(n):
    if len(str(n)) < 3:
        return str(n).rjust(2, ' ') + ' '
    else:
        return str(n)

def ausgeben(feld):
    print('     1   2   3   4   5')
    for y in range(len(feld)):
        print('   -------------------')
        print(y + 1, end= ' ')
        for x in range(len(feld[y])):
            print('|' + farbe(feld[y][x]) + zahl(feld[y][x]), end= '\033[0m')
        print('|')
    print('   -------------------')

ausgeben(feld)

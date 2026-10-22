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
    r = farbe + str(n) + '\033[0m'
    return r

def ausgeben(feld):
    print('     1   2   3   4   5')
    for y in range(len(feld)):
        print('    -------------------')
        print(y + 1, end= '  ')
        for x in range(len(feld[y])):
            print('|', end= '')
            if len(str(feld[y][x])) == 3:
                e = ''
            elif len(str(feld[y][x])) == 2:
                e = ' '
            elif len(str(feld[y][x])) == 1:
                e = ' '
                print(' ', end= '')
            print(farbe(feld[y][x]), end= e)
        print('|')

ausgeben(feld)

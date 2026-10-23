import math

def durchgehend(breite):  
    print('*' * breite)

def unterbrochen(breite):
    print('*' + ' ' * (breite - 2) + '*')

def main(breite, höhe):
    breite = int(math.sqrt(breite**2))
    höhe = int(math.sqrt(höhe**2))
    durchgehend(breite)
    for i in range(höhe -2):
        unterbrochen(breite)
    durchgehend(breite)

main(-10, -5)
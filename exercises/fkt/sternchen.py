def durchgehend(breite):  
    print('*' * breite)

def unterbrochen(breite):
    print('*' + ' ' * (breite - 2) + '*')

def main(breite, höhe):
    durchgehend(breite)
    for i in range(höhe -2):
        unterbrochen(breite)
    durchgehend(breite)

main(5, 10)
import zufallsworte as zufall
import random

wort = zufall.zufallswoerter(1)[0]  # gibt ein Zufallswort zurück
gesucht = wort.lower()

ja = ['y', 'j', 'ja', 'yes']
nein = ['n', 'nein', 'no']

gefunden = []
falsch_geraten = []

out_zuviel = ['Du kannst nur einen Buchstaben eingeben!', 'Übertreibe nicht! Nur einen Buchstabe.', 'Bitte schreibe keinen Roman, nur ein Zeichen pro Eingabe.']

out_zeichen = ['Bitte nur Buchstaben eingeben.', 'Soll das Französisch sein?!? Ich verstehe nur Buchstaben.', 'Ich bin faul, also schreib mir gefälligst nur Buchstaben.']

out_wiederholung = ['Du hast bereits diesen Buchstaben geraten!', 'Sei etwas Kreativer. Diesen Buchstaben hattest du bereits geraten.', 'Diesen Buchstaben kenne ich bereits. Wähle einen anderen.']

HANGMANS_RAW = ''' 18 Zeichen ergeben ein Bild...
                                         __________        __________        __________        __________        __________        __________        __________        __________        __________     
                       |                 |                 |/                |/        |       |/        |       |/        |       |/        |       |/        |       |/        |       |/        |    
                       |                 |                 |                 |                 |         O       |         O       |         O       |         O       |         O       |         O    
                       |                 |                 |                 |                 |                 |         |       |        -|       |        -|       |        -|-      |        -|-   
                       |                 |                 |                 |                 |                 |                 |                 |          \      |          \      |        / \   
                       |                 |                 |                 |                 |                 |                 |                 |                 |                 |  GAME OVER   
    _________         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______         _|_______     
___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ ___/         \___ 
'''.split('\n')[1:-1] # ohne erste und letzte Zeile

# enthält 11 ASCII-Bilder, für jeden Spiel-Zustand einen
HANGMANS = ['\n'.join([line[i : i + 18] for line in HANGMANS_RAW]) for i in range(0, 11 * 18, 18)]

def get_hangman(nr):
    '''
    nr: int values from 0 to 10
    '''
    return HANGMANS[nr]

# Generiert die Ausgabe im Terminal. Einigermassen grafisch dargestellt.
def show():
    print('Falsche Buchstaben:', falsch_geraten)
    for buchstabe in gesucht:
        if buchstabe in gefunden:
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print()
    print(get_hangman(len(falsch_geraten)))

# Der Benutzer gibt immer nur valide Inputs. Deshalb gibt diese Funktion immer True zurück.
def is_valid(inp):
    if len(inp) != 1:
        print(out_zuviel[random.randint(0, len(out_zuviel)-1)])
        return False
    elif not inp.isalpha():
        print(out_zeichen[random.randint(0, len(out_zeichen)-1)])
        return False
    elif inp in falsch_geraten or inp in gefunden:
        print(out_wiederholung[random.randint(0, len(out_wiederholung)-1)])
        return False
    else:
        return True

# Diese Funktion fragt nach einem Input und returnt den input mit alles kleinen Zeichen.
def eingabe():
    buchstabe = input('Buchstabe? ')
    while not is_valid(buchstabe):
        buchstabe = input('Buchstabe? ')
    return buchstabe.lower()

# Diese Funktion wertet den Input für das Programm aus und fügt den Input in die Jeweilige Liste.
def auswerten(valid_inp):
    if valid_inp in gesucht:
        gefunden.append(valid_inp)
    else:
        falsch_geraten.append(valid_inp)

# Diese Funktion überprüft, ob man nicht gewonnen hat.
def gewonnen():
    for buchstabe in gesucht:
        if buchstabe not in gefunden:
            return False
    return True

def game_over():
    if gewonnen() or len(falsch_geraten) >= 10:
        return True
    else:
        return False

def wiederholen():
    global gesucht
    antwort = input('Möchtest du eine Runde "Hangman" spielen?').lower()
    if antwort.isalpha():
        if antwort in ja:
            print('Super, ich überlege mir ein neues Wort!')
            wort = zufall.zufallswoerter(1)[0]  # gibt ein Zufallswort zurück
            gesucht = wort.lower()
            return True
        elif antwort in nein:
            print('Schade... :-(')
            return False
        else:
            print('Das habe ich leider nicht verstanden. ')
            return False

def play():
    global gefunden, falsch_geraten
    while not game_over():
        show()
        auswerten(eingabe())

    show()
    if gewonnen():
        print('GEWONNEN')
        gefunden = []
        falsch_geraten = []
    else:
        print('!!!!!!!GAME OVER!!!!!!!')

while wiederholen():
    print(wort)
    play()
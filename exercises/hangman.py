# Variablen
gesucht = 'test'

gefunden = []
falsch_geraten = []

# Generiert die Ausgabe im Terminal. Einigermassen grafisch dargestellt.
def show():
    print('Falsche Buchstaben:', falsch_geraten)
    for buchstabe in gesucht:
        if buchstabe in gefunden:
            print(buchstabe, end=' ')
        else:
            print('_', end=' ')
    print('')

# Der Benutzer gibt immer nur valide Inputs. Deshalb gibt diese Funktion immer True zurück.
def is_valid(inp):
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
    pass

def play():
    pass

play()
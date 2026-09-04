import png # Paket png importieren

def write(temp):
    for i in range(faktor):
        big_smiley.append(temp)

faktor = 2

smiley = [
    [000, 000, 000, 000, 000, 000],
    [000, 255, 000, 000, 255, 000],
    [000, 000, 000, 000, 000, 000],
    [000, 255, 000, 000, 255, 000],
    [000, 000, 255, 255, 000, 000],
    [000, 000, 000, 000, 000, 000]
]
# Erzeuge ein Graustufen-Bild (0=Schwarz, 255=Weiss)

big_smiley = []

temp = []

for zeile in smiley:
    for pixel in zeile:
        for i in range(faktor):
            temp.append(smiley[zeile][pixel])
        write(temp)


png.from_array(smiley, 'L').save('small_smiley.png')
import png # Paket png importieren

def write(temp):
    for i in range(faktor):
        big_smiley.append(temp)

faktor = 10

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
    z = 1
    for pixel in zeile:
        p = 1
        for i in range(faktor):
            temp.append(smiley[z][p])
        write(temp)
        p = p + 1
    z = z + 1


png.from_array(smiley, 'L').save('big_smiley.png')
import png # Paket png importieren

def write(temp):
    for i in range(faktor):
        big_smiley.insert((len(big_smiley)),temp)

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

z = 0
p = 0

for zeile in smiley:
    for pixel in zeile:
        for i in range(faktor):
            temp.append(smiley[z][p])
        p = p + 1
    write(temp)
    temp = []
    p = 0
    z = z + 1
z = 0

# print(big_smiley)

png.from_array(big_smiley, 'L').save('big_smiley.png')
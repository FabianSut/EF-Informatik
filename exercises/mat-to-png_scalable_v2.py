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


# v2

big_smiley_v2 = []

big_smiley_v2_temp = []

matrix = []

tempm = []

n = 0

for y in range(len(big_smiley)):
    tempm = []
    for x in range(len(big_smiley[y])):
        n = 1 - n
        tempm.append(n)
    matrix.append(tempm)

    if y % 2 == 0:
        for i in range(len(matrix[y])):
            matrix[y][i] = 1 - matrix[y][i]

for y in range(len(big_smiley)):
    for x in range(len(big_smiley[y])):
        big_smiley_v2_temp.append(big_smiley[y][x] * matrix[y][x])
    big_smiley_v2.append(big_smiley_v2_temp)
    big_smiley_v2_temp = []


png.from_array(big_smiley_v2, 'L').save('big_smiley_v2.png')
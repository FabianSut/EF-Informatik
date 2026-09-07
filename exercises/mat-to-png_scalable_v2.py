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

matrix = []

n = 0

while len(big_smiley[0]) != len(matrix):
    if n == 0:
        matrix.append(0)
        n = 1
    elif n == 1:
        matrix.append(1)
        n = 0


for y in range(len(big_smiley)):
    for x in range(len(big_smiley[0])):
        big_smiley[y][x] = big_smiley[y][x] * matrix[x]




png.from_array(big_smiley, 'L').save('big_smiley_v2.png')
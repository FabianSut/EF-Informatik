
zehn = list(0 for i in range(10))

hundert = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

n = 1

p = 2

hundert_prim = list(range(2, 101))

primzahlen = list(range(2, 101))

for n in hundert_prim:
    for m in primzahlen:
        if m % n == 0 and m != n:
            primzahlen.pop(primzahlen.index(m))

for p in primzahlen:
    for y in range(10):
        for x in range(10):
            n = y * 10 + x + 1
            if n % p == 0 and hundert[y][x] == 0:
                hundert[y][x] = p
                print(p)
    n = 1


print(len(primzahlen))

print(hundert)
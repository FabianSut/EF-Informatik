hundert = list(range(2, 101))

primzahlen = list(range(2, 101))

for n in hundert:
    for m in primzahlen:
        if m % n == 0 and m != n:
            primzahlen.pop(primzahlen.index(m))

print(primzahlen)
Code:
```
matrix = []

zeile = [0, 1, 0]
for i in range(3):
    matrix.append(zeile)

print(matrix)

matrix[1][1] = 0 # nur den Wert in Zeile 1 in der Mitte auf 0 Setzen

print(matrix)
```

Output:
```
[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

Weil das ```matrix[1][1] = 0``` die Variable ```zeile``` und ändert, ist jede der drei Zeilen in der zweiten Matrix ```[0, 0, 0]```.
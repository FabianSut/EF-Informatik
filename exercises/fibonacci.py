fibonacci = [1, 1]

for i in range(20000):
    fibonacci.append(fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2])

print(fibonacci)

print('Länge des letzten Glieds: ' + str(len(str(fibonacci[-1]))))
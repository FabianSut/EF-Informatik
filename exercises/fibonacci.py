fibonacci = [1, 1]

for i in range(100):
    fibonacci.append(fibonacci[len(fibonacci) - 1] + fibonacci[len(fibonacci) - 2])

print(fibonacci)
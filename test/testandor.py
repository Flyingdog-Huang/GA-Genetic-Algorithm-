import random

x = [random.randint(0, 1) for i in range(5)]
print(x)
for i in range(len(x)):
    x[i] = x[i] ^ 1
print(x)

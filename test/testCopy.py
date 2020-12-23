import copy

a = {0: 1, 1: 2, 2: 3}
# b = a.copy()
b = a
# b = copy.deepcopy(a)

b[0] = 0
print(a)
print(b)

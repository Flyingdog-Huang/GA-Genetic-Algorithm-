n = [0 for i in range(8)]  # 支配i的个体数目

n1 = [1, 2, 3, 4, 5, 6]
n2 = [4, 5, 6, 7, 8, 9]


def addpop(pop):
    pop_new = pop
    pop_new.append(3)
    pop_new.append(3)
    pop_new.append(3)
    return pop_new


n3 = [0] * 12
print(n2[:3])

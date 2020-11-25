# 父代交叉生成子代
import random
from NSGA2.Mutation import mutation


def crossover(pop, gene_length, pc, pm):
    """
    父代交叉生成子代--二进制单点交叉
    :param pop:
    :param gene_length:
    :param pc:
    :param pm:
    :return:
    """
    pop_son = []
    for X in pop:
        if random.random() < pc:
            mother = pop[random.randint(0, len(pop)-1)]
            if X != mother:
                cpoint = random.randint(1, gene_length - 2)  # 生成随机交叉单点
                X_son = []
                for i in range(len(X)):
                    x_fa = X[i]
                    x_mo = mother[i]
                    x_son = []
                    x_son.extend(x_fa[:cpoint])
                    x_son.extend(x_mo[cpoint:])
                    X_son.append(x_son)
                pop_son.append(X_son)

    pop_son = mutation(pop_son, gene_length, pm)  # 子代变异
    return pop_son

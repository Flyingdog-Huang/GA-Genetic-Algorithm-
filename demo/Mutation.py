# 变异（变异算子在此修改）--取反
# 基因在交叉后的新基因上变异?

import random

from CalobjValue import calobjValue


def mutation(pop, pm, chrom_length, max_value):
    """
    基因突变
    :param pop:二进制种群
    :param pm: 变异概率
    :return: 变异后新种群，适应度
    """
    px = len(pop)
    py = len(pop[0])
    for i in range(px):
        if random.random() < pm:
            m = random.randint(1, py)  # 随机变异m个点
            for j in range(m):
                point = random.randint(0, py - 1)  # 随机生成变异点位置
                if pop[i][point] == 1:
                    pop[i][point] = 0
                else:
                    pop[i][point] = 1
    return pop, calobjValue(pop, chrom_length, max_value)


def mutation10(pops, vars_rang, pm, iti):
    n = len(pops)
    m = len(pops[0])
    for i in range(n):
        if random.random() < pm:
            pop_new = []
            for j in range(m):
                ui = random.random()
                b1 = (pops[i][j] - vars_rang[j][0]) / (vars_rang[j][1] - vars_rang[j][0])
                b2 = (vars_rang[j][1] - pops[i][j]) / (vars_rang[j][1] - vars_rang[j][0])
                bi = 1 - (2 * (1 - ui) + 2 * (ui - 0.5) * ((1 - b2) ** (iti + 1))) ** (1 / (iti + 1))
                if ui <= 0.5:
                    bi = (2 * ui + (1 - 2 * ui) * ((1 - b1) ** (iti + 1))) ** (1 / (iti + 1)) - 1
                new_pop = pops[i][j] + bi * (vars_rang[j][1] - vars_rang[j][0])
                if vars_rang[j][0] <= new_pop <= vars_rang[j][1]:
                    pop_new.append(new_pop)
                elif new_pop > vars_rang[j][1]:
                    pop_new.append(vars_rang[j][1])
                elif new_pop < vars_rang[j][0]:
                    pop_new.append(vars_rang[j][0])
            pops.append(pop_new)
    return pops

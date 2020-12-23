# 交叉（交叉算子在此处修改）--精英单点交叉

import random
from Selection import selection
from CalobjValue import calobjValue


def findMoFa(pop, fit_value, chrom_length, max_value):
    """
    寻找最精英的父母（常用轮盘选择出父母基因）
    :param pop:种群
    :param fit_value:种群适应度
    :return: 父，母基因
    """
    # maxValue = max(fit_value)
    # faValue = min(fit_value)
    # moIndex = fit_value.index(maxValue)
    # mo = pop[moIndex]
    # fa = pop[fit_value.index(faValue)]
    # for i in range(len(fit_value)):
    #     if i != moIndex and fit_value[i] > faValue:
    #         faValue = fit_value[i]
    # fa = pop[fit_value.index(faValue)]
    mofa, fit = selection(pop, fit_value, 2, chrom_length, max_value)
    mo, fa = mofa
    return mo, fa


def crossover(pop, pc, fit_value, chrom_length, max_value):
    """

    :param pop: 二进制种群
    :param pc: 交配概率
    :param fit_value:
    :param chrom_length: 编码基因长度
    :param max_value: 最大值限制
    :return: 交叉后新种群，新种群适应度
    """
    pop_len = len(pop)
    for i in range(pop_len):
        if random.random() < pc:
            mother, father = findMoFa(pop, fit_value, chrom_length, max_value)
            cpoint = random.randint(1, len(pop[0]) - 2)  # 随机交叉点（单点交叉策略）
            temp1 = []
            temp2 = []
            temp1.extend(mother[0:cpoint])
            temp1.extend(father[cpoint:chrom_length])
            temp2.extend(father[0:cpoint])
            temp2.extend(mother[cpoint:chrom_length])
            pop.append(temp1)
            pop.append(temp2)
            fit_value = calobjValue(pop, chrom_length, max_value)
    return pop, fit_value


def crosspops10(pops, pc, iti, vars_rang):
    n = len(pops)
    for i in range(n):
        if random.random() < pc:
            j = random.randint(0, n - 1)
            while j == i:
                j = random.randint(0, n - 1)
            ui = random.random()
            bi = (1 / (2 * (1 - ui))) ** (1 / (iti + 1))
            if ui <= 0.5:
                bi = (2 * ui) ** (1 / (iti + 1))
            popi_new = []
            popj_new = []
            for z in range(len(pops[i])):
                # for xi, xj, x_rang in zip(pops[i], pops[j], vars_rang):
                xi = pops[i][z]
                xj = pops[j][z]
                x_rang = vars_rang[z]
                xi_new = 0.5 * ((1 + bi) * xi + (1 - bi) * xj)
                xj_new = 0.5 * ((1 - bi) * xi + (1 + bi) * xj)
                if x_rang[0] <= xi_new <= x_rang[1]:
                    popi_new.append(xi_new)
                if x_rang[0] <= xj_new <= x_rang[1]:
                    popj_new.append(xi_new)
            if len(popi_new) == len(pops[0]):
                pops.append(popi_new)
            if len(popj_new) == len(pops[0]):
                pops.append(popj_new)
    return pops

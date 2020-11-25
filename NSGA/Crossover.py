# 交叉（交叉算子在此处修改）--精英单点交叉
# 作用在于局部最优

import random
from Selection import selection
from CalobjValue import calobjValue
from CalfitValue import calfitValue
from Best import best


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
            # mother, father = findMoFa(pop, fit_value, chrom_length, max_value)
            mother, mother_fit = best(pop, fit_value)
            father = pop[i]
            cpoint = random.randint(0, chrom_length - 1)  # 随机交叉点（单点交叉策略）
            new_one1 = []
            new_one2 = []
            for j in range(len(mother)):
                temp1 = []
                temp2 = []
                temp1.extend(mother[j][0:cpoint])
                temp1.extend(father[j][cpoint:chrom_length])
                temp2.extend(father[j][0:cpoint])
                temp2.extend(mother[j][cpoint:chrom_length])
                new_one1.append(temp1)
                new_one2.append(temp2)
            pop.append(new_one1)
            pop.append(new_one2)
            pop = calfitValue(pop, chrom_length, max_value)
            fit_value = calobjValue(pop, chrom_length, max_value)
    return pop, fit_value

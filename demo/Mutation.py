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

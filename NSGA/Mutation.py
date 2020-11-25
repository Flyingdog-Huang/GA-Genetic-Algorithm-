# 变异（变异算子在此修改）--取反
# 基因在交叉后的新基因上变异?
# 作用在于全局搜索

import random
from CalfitValue import calfitValue
from CalobjValue import calobjValue


def mutation(pop, pm, chrom_length, max_value):
    """
    基因突变
    :param pop:二进制种群
    :param pm: 变异概率
    :return: 变异后新种群，适应度
    """
    pop_size = len(pop)
    type_num = len(pop[0])
    for i in range(pop_size):
        if random.random() < pm:
            # x = random.randint(0, type_num)  # 随机变异的基因组下标
            x = i  # 随机变异的基因组下标
            for j in range(type_num):
                m = random.randint(1, chrom_length)  # 变异点个数
                for z in range(m):
                    point = random.randint(0, chrom_length - 1)  # 随机生成变异点位置
                    if pop[x][j][point] == 1:
                        pop[x][j][point] = 0
                    else:
                        pop[x][j][point] = 1
    pop = calfitValue(pop, chrom_length, max_value)
    return pop, calobjValue(pop, chrom_length, max_value)

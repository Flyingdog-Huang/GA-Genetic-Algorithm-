# 初始化 - 随机生成种群编码
import random


def geneEncoding(pop_size, chrom_length):
    """

    :param pop_size: 种群规模
    :param chrom_length:  编码长度
    :return: 二进制编码种群
    """
    pop = []
    for i in range(pop_size):
        temp = []
        for j in range(chrom_length):
            temp.append(random.randint(0, 1))
        pop.append(temp)

    return pop


def genepop10(vars_num, pops_size, vars_rang):
    """
    生成实数编码种群
    :param vars_num:变量个数
    :param pops_size: 种群规模
    :param vars_rang: 每个变量范围的集合
    :return:
    """
    pops = []
    for i in range(pops_size):
        pop = []
        for j in range(vars_num):
            pop.append(random.uniform(vars_rang[j][0], vars_rang[j][1]))
        pops.append(pop)
    return pops
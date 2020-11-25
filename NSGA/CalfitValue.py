# 筛选淘汰（过滤规则在这里修改）
from CalobjValue import decodechrom


def calfitValue(pop, chrom_length, max_value):
    """
    约束条件筛选
    :param pop: 种群
    :param chrom_length:基因编码长度
    :param max_value: 最大值
    :return: 过滤后种群
    """
    new_pop = []

    for x in pop:
        if decodechrom(x[0], chrom_length, max_value) != 0 and decodechrom(x[1], chrom_length, max_value) != 0:
            new_pop.append(x)

    return new_pop


def boolcondition(x):
    c = 0
    num = len(x[0])
    for i in range(num):
        if x[0][i] == 1 or x[1][i] == 1:
            c = 1
            break
    if c == 0:
        return False
    return True

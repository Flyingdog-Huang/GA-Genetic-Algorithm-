# 初始化 - 随机生成种群编码
import random
from CalfitValue import boolcondition


def genex(chrom_length, type_num):
    """
    生成基因组
    :param chrom_length:
    :param type_num:
    :return:
    """
    x = []  # 生成每个基因组
    for z in range(type_num):
        temp = []  # 生成每条基因
        for j in range(chrom_length):
            temp.append(random.randint(0, 1))
        x.append(temp)
    return x


def geneEncoding(pop_size, chrom_length, type_num):
    """

    :param pop_size: 种群规模
    :param chrom_length: 编码长度
    :param type_num: 变量数量
    :return: 二进制编码种群
    """
    """

    :param pop_size: 
    :param chrom_length:  
    :return: 
    """
    pop = []  # 二进制编码种群
    while pop_size > 0:
        x = genex(chrom_length, type_num)
        if boolcondition(x):
            pop_size -= 1
            pop.append(x)

    # for i in range(pop_size):
    #     x = []  # 生成每个基因组
    #     for z in range(type_num):
    #         temp = []  # 生成每条基因
    #         for j in range(chrom_length):
    #             temp.append(random.randint(0, 1))
    #         x.append(temp)
    #     pop.append(x)
    return pop

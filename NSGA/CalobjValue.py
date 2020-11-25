# 解码并计算目标函数
import math
import Function


def decodechrom(individual, chrom_length, max_value):
    """
    解码（二进制=>十进制）
    :param individual: 二进制编码单个基因
    :param chrom_length:二进制编码长度
    :param max_value:变量上界
    :return:单个基因的十进制
    """
    t = 0.0
    # chrom_length = len(individual)
    for j in range(chrom_length):
        if individual[j] == 1:
            t += (2 ** (chrom_length - 1 - j))
    t = t * max_value / (2 ** chrom_length - 1)

    return t


def calobjValue(pop, chrom_length, max_value):
    """
    目标函数计算
    :param pop: 二进制种群
    :param chrom_length: 编码长度
    :param max_value: 变量上界
    :return: 种群适应度值
    """

    fit_value = []

    for i in range(len(pop)):
        x = [decodechrom(j, chrom_length, max_value) for j in pop[i]]
        fit_value.append(1/Function.function_3(x))

    return fit_value

# 解码并计算目标函数
import math
import Function


def decodechrom(individual, chrom_length, max_value):
    """
    解码（二进制=>十进制）
    :param pop: 二进制编码的
    :param chrom_length: 二进制编码长度
    :param max_value: 变量上界
    :return:  十进制种群
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

    obj_value = []
    for i in range(len(pop)):
        x = decodechrom(pop[i], chrom_length, max_value)
        obj_value.append(Function.function_1(x))

    return obj_value


def calpopfit(pops):
    """
    因变量值计算
    :param pops:
    :return:
    """
    pops_fit = []
    for x in pops:
        fit = Function.function_4(x)
        pops_fit.append(fit)
    return pops_fit

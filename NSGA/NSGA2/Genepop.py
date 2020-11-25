# 生成种群
import random
from NSGA2.Filtpop import filtpop  # 约束条件过滤
from NSGA2.Decodechrom import binary2decimal


def genepop(pop_size, genes_num, gene_length):
    """
    生成二进制种群基因集合
    :param pop_size:
    :param gene_lenth:
    :return:
    """
    pop = []
    while len(pop) < pop_size:
        n = pop_size - len(pop)
        for i in range(n):
            X = []
            for j in range(genes_num):
                x = [random.randint(0, 1) for j in range(gene_length)]
                X.append(x)
            pop.append(X)
        pop = filtpop(pop)
    if len(pop) == pop_size:
        return pop


def pop2to10(pop, min_value, max_value):
    """
    二进制种群转换成十进制
    :param pop:
    :param min_value:
    :param max_value:
    :return:
    """
    pop10 = []
    for X in pop:
        genes = []
        for x in X:
            genes.append(binary2decimal(x, min_value, max_value))
        pop10.append(genes)
    return pop10

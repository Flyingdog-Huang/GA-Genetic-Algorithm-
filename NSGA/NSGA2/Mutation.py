# 变异算子--交叉生成的子代变异
import random


def mutation(pop_son, gene_length, pm):
    """
    子代变异--二进制单点取反
    :param pop_son:
    :param gene_length:
    :param pm:
    :return:
    """
    for X_son in pop_son:
        if random.random() < pm:
            mpoint = random.randint(0, gene_length - 1)  # 生成突变基因位置
            for x_son in X_son:
                x_son[mpoint] = x_son[mpoint] ^ 1
    return pop_son

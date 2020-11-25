# 选择算子在这里修改--轮盘选择
import random

from CalobjValue import calobjValue
from Best import best


def cumsum(fit_value):
    """
    累加种群适应度概率
    :param fit_value:适应度概率
    :return:适应度概率累加
    """
    n = len(fit_value)
    min_fit = min(fit_value)
    sum_fit = 0.0  # 适应度总和
    new_fit = []  # 新适应度
    # 计算总和
    for i in fit_value:
        dis = i - min_fit
        if dis == 0.0:
            dis = 0.000000001
        new_fit.append(dis)
        sum_fit += dis

    for i in range(n):
        new_fit[i] = new_fit[i] / sum_fit

    for i in range(1, n):
        new_fit[i] = new_fit[i] + new_fit[i - 1]

    new_fit[n - 1] = 1
    return new_fit


def selection(pop, fit_value, pop_size, chrom_length, max_value):
    """

    :param pop:
    :param fit_value:
    :return:
    """
    n = len(pop)
    max_p, max_fit = best(pop, fit_value)
    newpop = []  # 选择后新种群
    newpop.append(max_p)

    # print(len(newpop))

    # 概率累加计算
    newfit_value = cumsum(fit_value)
    # 轮盘选择
    for i in range(pop_size - 1):
        choose = random.random()
        for j in range(n):
            if newfit_value[j] >= choose:
                newpop.append(pop[j])
                break
    return newpop, calobjValue(newpop, chrom_length, max_value)

    # ms = []
    # pop_len = len(pop)
    # for i in range(pop_len):
    #     ms.append(random.random())
    # ms.sort()
    # fitin = 0
    # newin = 0
    # newpop = pop
    # 轮盘选择策略
    # while newin < pop_len:
    #     if ms[newin] < newfit_value[fitin]:
    #         newpop[newin] = pop[fitin]
    #         newin += 1
    #     else:
    #         fitin += 1
    # pop = newpop

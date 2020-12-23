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


def filter(pops, midlle_value, midlle_rang):
    '''
    根据中间值过滤
    :param pops:
    :param midlle_value:
    :param midlle_rang:
    :return:
    '''
    new_pops = []
    for i in range(len(pops)):
        label_i = 0
        for j in range(len(midlle_value[i])):
            if midlle_rang[j][0] > midlle_value[i][j] or midlle_value[i][j] > midlle_rang[j][1]:
                label_i = 1
                break
        if label_i == 0:
            new_pops.append(pops[i])
    return new_pops


def isdomain(y1, y2, y_rules):
    '''
    判断支配关系
    :param y1:
    :param y2:
    :param y_rules:
    :return:
    '''
    m = len(y1)
    for i in range(m):
        if y_rules[i] == 0:
            if y1[i] >= y2[i]:
                return False
        if y_rules[i] == 1:
            if y1[i] <= y2[i]:
                return False
    return True


def selectpops10(pops, pops_fit, fits_rules, pops_size):
    '''
    非支配快速排序算法
    :param pops:
    :param pops_fit:
    :param fits_rules:
    :param pops_size:
    :return:
    '''
    new_pops = []
    class_num = 0
    n = len(pops)
    pops_class = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            if isdomain(pops_fit[i], pops_fit[j], fits_rules):
                pops_class[j] += 1
            if isdomain(pops_fit[j], pops_fit[i], fits_rules):
                pops_class[i] += 1
    while len(new_pops) < pops_size:
        for z in range(n):
            if pops_class[z] == class_num:
                new_pops.append(pops[z])
        class_num += 1
    return new_pops[:pops_size]

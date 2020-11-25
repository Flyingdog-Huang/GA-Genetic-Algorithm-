import math
import numpy as np
from NSGA2.Calaimvalue import calaimvalue  # 引入目标值计算函数


def isdominate(x1, x2, min_value, max_value):
    """
    x1基因组是否对x2形成支配关系--支配规则
    :param x1:
    :param x2:
    :return:
    """
    y1 = calaimvalue(x1, min_value, max_value)
    y2 = calaimvalue(x2, min_value, max_value)
    aimvalue_lengh = len(y1)
    # bool_lable=0 # 支配判断标记
    for i in range(aimvalue_lengh):
        if y1[i] <= y2[i]:  # 全部对应解均大于对方
            return False
    return True


def isanybig0(n):
    for i in n:
        if i > 0:
            return True
    return False


def fastnondominatedsort(pop, min_value, max_value):
    """
    非支配层级生成
    :param pop:
    :param min_value:
    :param max_value:
    :return:
    """
    pop_size = len(pop)  # 种群个数
    dom = [0 for i in range(pop_size)]  # 排序支配层级
    n = [0 for i in range(pop_size)]  # 支配i的个体数目
    now_class = 1  # 目前层级
    for i in range(pop_size):
        for j in range(pop_size):
            if i != j:
                if isdominate(pop[j], pop[i], min_value, max_value):
                    n[i] += 1
        if n[i] == 0:
            dom[i] = now_class
    now_class += 1
    while isanybig0(n):
        lab_classadd = 0
        for i in range(pop_size):
            n[i] -= 1
            if n[i] == 0 and dom[i] == 0:
                dom[i] = now_class
                lab_classadd = 1
        if lab_classadd == 1:
            now_class += 1
    return dom

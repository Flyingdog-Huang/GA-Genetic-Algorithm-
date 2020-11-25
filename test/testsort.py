import random
import math


def findnum(x, listx):
    """
    在数组中找指定元素的下标
    :param x:
    :param listx:
    :return:
    """
    for i in range(len(listx)):
        if listx[i] == x:
            return i
    return -1


def sortbyfit(pop, fit_value):
    """
    根据适应度从小到大进行种群排序
    :param pop:种群
    :param fit_value:单值虚拟适应度
    :return:
    """
    pop_sort = []
    fit_sort = []
    num = len(pop)
    for i in range(num):
        index_min = fit_value.index(min(fit_value))
        # index_min = findnum(min(fit_value), fit_value)
        pop_sort.append(pop[index_min])
        fit_sort.append(fit_value[index_min])
        fit_value[index_min] = math.inf
    return pop_sort, fit_sort


pop = [i for i in range(10)]
fit_value = [random.randint(1, 10) for i in range(10)]
print(pop, fit_value)
print(sortbyfit(pop, fit_value))

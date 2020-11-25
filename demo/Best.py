# 找出最优解与最优结果(最大值)

def best(pop, fit_value):
    """
    寻找最优基因与适应度
    :param pop:二进制种群
    :param fit_value:对应适应度
    :return:最优基因与适应度
    """
    best_individual = pop[0]
    best_fit = fit_value[0]
    for i in range(len(fit_value)):
        if fit_value[i] > best_fit:
            best_individual = pop[i]
            best_fit = fit_value[i]

    return best_individual, best_fit

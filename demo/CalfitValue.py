# 筛选淘汰（过滤规则在这里修改）

def calfitValue(obj_value):
    """

    :param obj_value:  种群适应度
    :return: 过滤后种群适应度
    """
    fit_value = []
    c_min = 0
    for i in range(len(obj_value)):
        if obj_value[i] + c_min > 0:
            temp = c_min + obj_value[i]
        else:
            temp = 0.0
        fit_value.append(temp)
    return fit_value


def rule_3(pops):
    new_pop = []
    for pop in pops:
        if pop >= 0:
            new_pop.append(pop)
    return new_pop

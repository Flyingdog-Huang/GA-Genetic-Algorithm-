# 保存较优结果
from NSGA2.Calaimvalue import calaimvalue
from NSGA2.Decodechrom import binary2decimal


def saveres(pop, dom, min_value, max_value):
    aim_class = 1
    pop_class1 = []
    for i in range(len(pop)):
        if dom[i] == aim_class:
            pop_class1.append(pop[i])
    value_class1 = []
    for x in pop_class1:
        value_class1.append(calaimvalue(x, min_value, max_value))
    X = []
    result = []
    for x in pop_class1[0]:
        X.append(binary2decimal(x, min_value, max_value))
    result.append(X)
    result.append(value_class1[0])
    return result

    # y1=[value_class1[i][0] for i in range(len(value_class1))]
    # y2=[value_class1[i][1] for i in range(len(value_class1))]
    # y1min=min(y1)
    # y1max=max(y1)
    # y1dis=y1max-y1min
    # y2min = min(y2)
    # y2max = max(y2)
    # y2dis = y2max-y2min
    # for i in range(len(y1)):
    #     y1[i]=y1[i]-y1min
    #     y1[i]=y1[i]/y1dis
    #     y2[i] = y2[i] - y2min
    #     y2[i] = y2[i] / y2dis

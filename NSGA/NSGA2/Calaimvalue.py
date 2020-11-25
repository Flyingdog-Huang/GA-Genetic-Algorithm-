# 计算虚拟适应度

import Function as fc  # 引入目标函数
from NSGA2.Decodechrom import binary2decimal  # 引入解码函数


def calaimvalue(X, min_value, max_value):
    """
    计算目标函数值
    :param X:
    :return:
    """
    Y = []  # 目标函数值集合
    X_de = []  # 十进制解集
    for x in X:
        it = binary2decimal(x, min_value, max_value)
        X_de.append(it)

    Y.append(fc.function_1(X_de))
    Y.append(fc.function_2(X_de))

    return Y

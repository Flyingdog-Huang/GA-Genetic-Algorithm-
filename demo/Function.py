# 在此处修改目标函数
import math


def function_1(x):
    return 10 * math.sin(5 * x) + 7 * math.cos(4 * x)


def function_2(x1, x2, x3, x4):
    return abs(x1 ** 2 / (x2 + x3) - x1 * x3 + x2 - x4)


def function_3(x):
    res = []
    if x[0] == 0:
        x[0] = 0.000001
    res.append(x[0] ** 2 + 54 / x[0])
    return res

def function_4(x):
    res = []
    res.append((x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2)
    return res
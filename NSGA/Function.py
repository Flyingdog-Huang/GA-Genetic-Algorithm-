# 在此处修改目标函数
import math


def function_1(x):
    # print('y = 10 * math.sin(5 * x) + 7 * math.cos(4 * x)')
    return 10 * math.sin(5 * x[0]) + 7 * math.cos(4 * x[1])


def function_2(x):
    # print('y = abs(x1 ** 2 / (x2 + x3) - x1 * x3 + x2 - x4)')
    return abs(x[0] ** 2 / (x[1] + x[2]) - x[0] * x[2] + x[1] - x[3])


def function_3(x):
    return (x[0] ** 2 + x[1] - 11) ** 2 + (x[0] + x[1] ** 2 - 7) ** 2

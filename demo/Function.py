# 在此处修改目标函数
import math


def function_1(x):
    return 10 * math.sin(5 * x) + 7 * math.cos(4 * x)


def function_2(x1, x2, x3, x4):
    return abs(x1 ** 2 / (x2 + x3) - x1 * x3 + x2 - x4)

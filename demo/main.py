# 遗传算法模型主入口
from GeneEncoding import genepop10  # 实数编码生成种群
from CalobjValue import calpopfit  # 计算目标函数值
import numpy as np
import matplotlib.pyplot as plt
from Crossover import crosspops10  # 实数编码交叉算子
from Mutation import mutation10  # 实数编码变异算子
from Selection import selectpops10  # 实数编码选择算子


def popschange(pops):
    pops_change = []
    n = len(pops)
    m = len(pops[0])
    for i in range(m):
        pops_change_i = []
        for j in range(n):
            pops_change_i.append(pops[j][i])
        pops_change.append(pops_change_i)
    return pops_change


# 关键参数确定
pops_size = 100  # 种群规模
iteration = int(input('迭代次数：'))  # 迭代次数
pc = 0.6  # 交叉概率
pm = 0.1  # 变异概率

vars_num = int(input('自变量个数：'))  # 自变量数量
vars_rang = []  # 自变量边界[xi_min,xi_max]
# 输入自变量边界
for i in range(vars_num):
    xi_rang = []
    xi_min = float(input(f'第{i + 1}个自变量的最小值：'))
    xi_rang.append(float(xi_min))
    xi_max = float(input(f'第{i + 1}个自变量的最大值：'))
    xi_rang.append(float(xi_max))
    vars_rang.append(xi_rang)

midlle_value = []  # 中间计算值——过滤条件
midlle_num = int(input('中间值个数：'))
midlle_rang = []  # 中间值范围
for i in range(midlle_num):
    xi_rang = []
    xi_min = float(input(f'第{i + 1}个中间值的最小值：'))
    xi_rang.append(float(xi_min))
    xi_max = float(input(f'第{i + 1}个中间值的最大值：'))
    xi_rang.append(float(xi_max))
    midlle_rang.append(xi_rang)

fits_num = int(input('因变量个数：'))  # 因变量数量
pops_fit = []  # 自变量值
print('请输入每个因变量的取值策略，取最大请输入1，取最小请输入0')
fits_rules = []  # 取值策略
for i in range(fits_num):
    rule_i = int(input(f'第{i + 1}个因变量的取值策略：'))
    fits_rules.append(rule_i)

# 实数编码生成初始种群
pops = genepop10(vars_num, pops_size, vars_rang)
print('初始种群：', pops)
pops_change = popschange(pops)
print('改变形态为：', pops_change)

# 自变量计算
pops_fit = calpopfit(pops)
print('目标函数值：', pops_fit)

# # 标准函数绘制
# x_stand = []
# x_s = np.arange(0.1, 11, 0.01)
# for i in x_s:
#     xi = []
#     xi.append(i)
#     x_stand.append(xi)
# y_stand = calpopfit(x_stand)
# plt.plot(x_stand, y_stand)
#
# 储存每代最优值
x_res = []
y_res = []
# x_res.append(0)
# y_res.append(pops_fit[0][0])

# 迭代遗传
for i in range(1, iteration):
    # 交叉
    # pops = crosspops10(pops, pc, i, vars_rang)
    pops = crosspops10(pops, pc, 1, vars_rang)
    print(f'第{i}代交叉后种群：', pops)

    # 变异
    # pops = mutation10(pops, vars_rang, pm, i)
    pops = mutation10(pops, vars_rang, pm, 1)
    print(f'第{i}代变异后种群：', pops)

    # 选择
    pops_fit = calpopfit(pops)
    pops = selectpops10(pops, pops_fit, fits_rules, pops_size)
    print(f'第{i}代选择后种群：', pops)

    # 储存每代最优值
    pops_fit = calpopfit(pops)
    x_res.append(i)
    y_res.append(pops_fit[0][0])

# 最优结果
print('迭代最优自变量：', pops[0])
print('迭代最优因变量：', pops_fit[0])

# 绘制迭代结果
plt.plot(x_res, y_res)
# plt.plot(pops[0][0], pops_fit[0][0], 'r*')
plt.show()

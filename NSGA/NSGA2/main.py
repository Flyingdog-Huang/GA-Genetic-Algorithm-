# 主程序
from NSGA2.Genepop import genepop  # 引入种群生成函数
from NSGA2.Genepop import pop2to10
from NSGA2.Calaimvalue import calaimvalue  # 引入目标计算函数
from NSGA2.Crossover import crossover  # 引入交叉算子
from NSGA2.Fastnondominatedsort import fastnondominatedsort  # 快速非支配排序
from NSGA2.Selection2 import selection2  # 引入选择函数
from NSGA2.Saveres import saveres  # 引入保存较优解集函数
import matplotlib.pyplot as plt
from NSGA2.Decodechrom import binary2decimal

import Function as func

# 确定关键参数

pop_size = 10  # 种群规模N
pop = []  # 种群集合
gene_length = 7  # 染色体长度
genes_num = 4  # 基因组中基因个数
max_value = 50  # 基因中允许出现的最大值
min_value = 0  # 基因中允许出现的最小值

pc = 0.6  # 交配概率
pm = 0.01  # 变异概率

iterations = 500  # 迭代进化次数

results = []  # 结果保存【X=xi，Y=yi】
# results_class1 = []

# dominate_dis = []  # 支配层级与参考点距离--数据结构【dom，dis】

# aimvalue = []  # 目标函数值集合
# aimvalue_size = 2  # 目标函数数目

# 生成初始父代N个
pop = genepop(pop_size, genes_num, gene_length)  # 二进制种群
# pop10 = pop2to10(pop, min_value, max_value)  # 十进制种群
# print(len(pop))

for i in range(iterations):
    print('第', i, '代')
    # 交叉生成子代并变异
    son_pop = crossover(pop, gene_length, pc, pm)
    # print(len(son_pop))

    # 合并父代子代
    for x_son in son_pop:
        pop.append(x_son)
    # print(len(pop))

    # 生成非支配层级
    dom = fastnondominatedsort(pop, min_value, max_value)
    # print(dom)

    result_class1 = []
    count = 0
    dom_len = len(dom)
    for class_bool in range(dom_len):
        if dom[class_bool] == 1:
            count += 1
            res_class1 = []
            for x in pop[class_bool]:
                res_class1.append(binary2decimal(x, min_value, max_value))
            result_class1.append(res_class1)
            result_class1.append(calaimvalue(pop[class_bool], min_value, max_value))
    class1 = count / dom_len
    print(result_class1)

    # 储存解集
    # results.append(saveres(pop, dom, min_value, max_value))
    results.append(class1)

    # 选择出新的种群
    pop = selection2(pop, dom, pop_size, min_value, max_value)
    # print(pop)

# print(results[len(results) - 1])

X = []
Y = []
for i in range(iterations):
    X.append(i)
    Y.append(results[i])
    # Y.append(results[i][1][0] + results[i][1][1])

plt.plot(X, Y)
plt.show()

# 生成非支配层级和参考点距离
# dominate_dis=genedomdis(pop)


# 计算目标函数集合
# aimvalue = [calaimvalue(x, min_value, max_value) for x in pop]

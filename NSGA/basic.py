# 简单遗传算法模型主体
import matplotlib.pyplot as plt

from Best import best  # 找出最优解与最优结果(最大值)
from CalfitValue import calfitValue  # 筛选淘汰（过滤规则在这里修改）
from CalobjValue import decodechrom as decoding  # 解码（二进制=>十进制）
from CalobjValue import calobjValue  # 目标函数(适应度)计算
from Crossover import crossover  # 交叉（交叉算子在此处修改）--单点交叉
from GeneEncoding import geneEncoding  # 初始化 - 随机生成种群编码
from Mutation import mutation  # 变异（变异算子在此修改）--取反
from Selection import selection  # 选择算子在这里修改--轮盘选择

pop_size = 100  # 种群数量
type_num = 2  # 变量数量
iterations = 100  # 迭代进化次数
max_value = 50  # 基因中允许出现的最大值
min_value = 0  # 基因中允许出现的最小值
chrom_length = 7  # 染色体长度
pc = 0.6  # 交配概率
pm = 0.3  # 变异概率
results = []  # 每代最优解集
fit_value = []  # 个体适应度

pop = geneEncoding(pop_size, chrom_length, type_num)  # 初始化二进制种群基因编码

for i in range(iterations):
    # print('NO. ', i + 1)
    pop = calfitValue(pop, chrom_length, max_value)  # 筛选淘汰
    fit_value = calobjValue(pop, chrom_length, max_value)  # 适应度计算
    # print('初始', fit_value)
    best_indiviual, best_fit = best(pop, fit_value)  # 最优解集
    best_indiviual_ten = [decoding(j, chrom_length, max_value) for j in best_indiviual]  # 最优解集进制转换
    results.append([best_indiviual_ten, 1/best_fit])
    pop, fit_value = selection(pop, fit_value, pop_size, chrom_length, max_value)
    # print('选择', fit_value)
    pop, fit_value = crossover(pop, pc, fit_value, chrom_length, max_value)
    # print('交叉', fit_value)
    pop, fit_value = mutation(pop, pm, chrom_length, max_value)
    # print('变异', fit_value)

print(results[iterations-1][0], results[iterations-1][1])

X = []
Y = []
for i in range(iterations):
    X.append(i)
    Y.append(results[i][1])

plt.plot(X, Y)
plt.show()

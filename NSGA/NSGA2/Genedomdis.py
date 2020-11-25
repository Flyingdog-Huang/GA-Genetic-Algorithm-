# 生成种群对应的支配层dom和参考距离dis
from NSGA2.Fastnondominatedsort import fastnondominatedsort # 引入快速非支配排序法

def genedomdis(pop):
    dom=fastnondominatedsort(pop)
    dis=[]
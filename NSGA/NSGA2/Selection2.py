# 在原始NSGA-II中，具有--较大拥挤距离--的解会优先被选择
# 拥挤距离度量并不适合求解 高维多目标优化问题（三个及更多目标的多目标优化问题）
# 在选择前先进行非支配排序(精英策略+快速非支配排序算法)
# 其本质为精英保留策略，先分层级，在同层级之间再分优劣，父代和子代一起竞争
from NSGA2.Fastnondominatedsort import fastnondominatedsort  # 引入非支配快排
from NSGA2.Genedis import genedis  # 引入距离函数


def selection2(pop, dom, pop_size, min_value, max_value):
    now_size = len(dom)  # 目前种群规模
    new_pop = []
    now_class = 1
    while len(new_pop) < pop_size:
        findnum = pop_size - len(new_pop)
        classpop = []
        for i in range(now_size):
            if dom[i] == now_class:
                classpop.append(pop[i])
        if len(classpop) <= findnum:
            for x in classpop:
                new_pop.append(x)
            now_class += 1
        elif len(classpop) > findnum:
            for i in range(findnum):
                new_pop.append(classpop[i])
            # # 根据距离选择
            # dis = genedis(classpop, min_value, max_value)
            # while findnum > 0:
            #     max_dis = max(dis)
            #     for j in range(len(dis)):
            #         if dis[j] == max_dis:
            #             new_pop.append(classpop[j])
            #             findnum -= 1
            #             dis[j] = 0
            #             break
    if len(new_pop) == pop_size:
        return new_pop

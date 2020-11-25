# 生成参考点距离
from NSGA2.Calaimvalue import calaimvalue  # 引入目标值计算函数


def genedis(pop, min_value, max_value):
    aim_value = []
    for X in pop:
        aim_value.append(calaimvalue(X, min_value, max_value))
    length = len(aim_value)

    y1 = [aim_value[i][0] for i in range(length)]
    y2 = [aim_value[i][1] for i in range(length)]
    y1min = min(y1)
    y1max = max(y1)
    y1dis = y1max - y1min
    y2min = min(y2)
    y2max = max(y2)
    y2dis = y2max - y2min
    y1min = y1min - y1dis / length
    y1max += y1dis / length
    y2min -= y2dis / length
    y2max += y2dis / length
    y1dis = y1max - y1min
    y2dis = y2max - y2min

    for i in range(len(y1)):
        y1[i] = y1[i] - y1min
        if y1dis == 0:
            y1[i] = 1
        else:
            y1[i] = y1[i] / y1dis
        y2[i] = y2[i] - y2min
        if y2dis == 0:
            y2[i] = 1
        else:
            y2[i] = y2[i] / y2dis
        aim_value[i][0] = y1[i]
        aim_value[i][1] = y2[i]

    dis = []
    n = len(pop)
    for i in range(n):
        dis_i = 0
        for j in range(n):
            if i != j:
                dis_i += (aim_value[i][0] - aim_value[j][0]) ** 2
                dis_i += (aim_value[i][1] - aim_value[j][1]) ** 2
        dis.append(dis_i)

    return dis

    # idea_point = aim_value[0]
    #
    # # 计算理想点
    # for i in range(len(aim_value)):
    #     if aim_value[i][0] > idea_point[0]:
    #         idea_point[0] = aim_value[i][0]
    #     if aim_value[i][1] > idea_point[1]:
    #         idea_point[1] = aim_value[i][1]
    #
    # # 计算相对点
    # for i in range(len(aim_value)):
    #     aim_value[i][0] = idea_point[0] - aim_value[i][0]
    #     aim_value[i][1] = idea_point[1] - aim_value[i][1]

    # 计算极值点

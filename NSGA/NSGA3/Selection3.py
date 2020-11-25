#  NSGA-III通过所提供的参考点，对 St中的个体进行更加系统地分析，以选择部分解进入 Pt+1。
# 算法步骤如下：
#    1. 分支配排序、分层
#    2. 生成参考点
#    3. 计算理想点: 即求解这一代种群所有目标每个维度的的最小值。
#    比如A三个目标值是（2，3，5），B的三个目标是（4，3，5），C的三个目标是（3，3，4），那么 ideal point为（2，3，4）。
#    4. 将解空间零点挪到上述理想点
#    5. 找出极值点:
#    --找出各个轴的极值点，就能构建超平面（对于上图只有两个个体的情况，超平面其实就是通过两个点的直线），
#    --超平面和坐标轴的交点即可得到截距，有多少个坐标轴，就有多少个截距，
#    --把所有个体点除包含所有截距的向量，就是个体的归一化，个体即映射到参考点所在的归一化平面上。
#    6、将所有个体关联到参考点（根据参考点和个体之间的欧几里得距离或其他距离）
#    7.依据参考点的小生境从F8层提取10个个体加入到下一代种群中。
#    8.迭代往复进行，直至达到收敛条件。
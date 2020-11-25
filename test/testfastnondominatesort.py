def fast_nondominated_sort( P ):
    F = [ ]
    for p in P:
        Sp = [ ]
         np = 0
         for q in P:
             if p > q:                #如果p支配q，把q添加到Sp列表中
                 Sp.append( q )
             else if p < q:        #如果p被q支配，则把np加1
                 np += 1

        if np == 0:
            p_rank = 1        #如果该个体的np为0，则该个体为Pareto第一级
      F1.append( p )
    F.append( F1 )
    i = 0
    while F[i]:
        Q = [ ]
        for p in F[i]:
            for q in Sp:        #对所有在Sp集合中的个体进行排序
                nq -= 1
                if nq == 0:     #如果该个体的支配个数为0，则该个体是非支配个体
                    q_rank = i+2    #该个体Pareto级别为当前最高级别加1。此时i初始值为0，所以要加2
                    Q.append( q )
        F.append( Q )
        i += 1
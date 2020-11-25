import random


def geneEncoding(pop_size, chrom_length):
    """

    :param pop_size: 种群规模
    :param chrom_length:  编码长度
    :return: 二进制编码种群
    """
    pop = [[]]
    for i in range(pop_size):
        temp = []
        for j in range(chrom_length):
            temp.append(random.randint(0, 1))
        pop.append(temp)

    return pop

pop=geneEncoding(50,10)
print(pop)
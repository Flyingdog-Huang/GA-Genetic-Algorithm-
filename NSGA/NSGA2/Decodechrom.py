# 单个基因解码

def binary2decimal(singlegene, min_value, max_value):
    """
    二进制转十进制
    :param x:
    :return:
    """
    chrom_length = len(singlegene)  # 基因长度
    decimalvalue = 0.0  # 十进制数值

    for j in range(chrom_length):
        if singlegene[j] == 1:
            decimalvalue += (2 ** (chrom_length - 1 - j))

    dis = max_value - min_value
    decimalvalue = decimalvalue * dis / (2 ** chrom_length - 1) + min_value

    return decimalvalue

def isok(num):
    if num < 10:
        return True
    if num >= 10:
        numlist = []
        while num >= 10:
            numlist.append(num % 10)
            num = num // 10
        numlist.append(num)
        l = 0
        for i in range(len(numlist) - 1):
            if numlist[i] < numlist[i + 1]:
                l = 1
                break
        if l == 0:
            return True
        else:
            return False


N = 612312
while isok(N) is False:
    N -= 1
print(N)

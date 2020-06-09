# for循环会遍历in后面的可迭代对象，每次将其中的元素赋值给i，知道遍历完，结束循环。
for i in range(100, 1000):
    # 取出i的个位，十位和百位上的数字 - //表示地板除，%表示取余数。
    hundred = i // 100
    ten = ((i // 10) % 10)
    one = i % 10

    # 计算各个数字的立方和
    sum = hundred **3 + ten **3 + one **3

    # 判断i是否为水仙数
    if i == sum:
        print(i,"是水仙数。", end=" ")

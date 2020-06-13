"""
内置函数 range()可以用于遍历一个数字序列，它生产一个算术级数
"""
for i in range(5):
    print(i)

# range可以以另一个数字开头，或者以指定的幅度增加（甚至是负数；有时这也被叫做'步进'）
range(5, 10)   # 5, 6, 7, 8, 9
range(0, 10, 3)   # 0, 3, 6, 9
range(-10, -100, -30)   # -10, -40, -70

# 将range()和len()组合，可以以序列的索引来迭代
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

# 从一个指定范围内获取一个列表
b = list(range(5))
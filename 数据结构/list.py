"""
Python 中可以通过组合一些值得到多种 复合 数据类型。其中最常用的 列表 ，可以通过方括号括起、
逗号分隔的一组值（元素）得到。一个 列表 可以包含不同类型的元素，但通常使用时各个元素类型相同。
"""

import sys
import dis

# 一个列表的示例
list = [1, 4, 9, 16, 25]

# 列表也支持索引和切片
print(list[0])
print(list[-3:0])

# 所有的切片操作都返回一个包含所请求元素的新列表。 这意味着以下切片操作会返回列表的一个浅拷贝
a = list[:]

# 列表同样支持拼接操作
a = list + [36, 49, 65, 81, 100]
print(a)

# 列表的元素可以通过索引赋值的方式进行改变
a[7] = 64
print(a)

# 列表支持对切片进行赋值，来改变列表的内容
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 1. 替换某些元素
letters[2:5] = 'C, D, E'
print(letters)
# 2. 删除某些元素
letters[2:5] = []
print(letters)
# 3. 清空列表
letters[:] = []
print(letters)

# 内置函数len()也可以作用到列表上
letters = ['a', 'b', 'c']
print(len(letters))

# 列表也可以嵌套列表 (创建包含其他列表的列表)
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])
print(x[0][1])


# 列表的常用方法
name_list = ["zhangsan", "lisi", "wamgwu"]
# 1.取索引 - 知道数据内容，确定其索引值
# 使用idex方法需要注意，如果传入数据不在列表中，程序会报错
print(name_list.index('lisi'))

# 2.增加数据
# append方法可以向列表的末尾增加数据
name_list.append('王小二')
# insert方法会在索引值所在的位置增加数据
name_list.insert(1, "小美")
# extend方法在列表的末尾追加其他列表得到全部数据
temp = ["xiaohuang", "小明"]
name_list.extend(temp)

# 3.删除数据
# remove方法可以从列表中删除指定数据
name_list.remove('wamgwu')
# pop方法在默认情况下，删除列表最后一个数据
name_list.pop()
# pop可以删除指定索引位置的数据
name_list.pop(3)
# clear方法可以清空整个列表
name_list.clear()
# del关键字删除列表中的数据 - 本质上是将一个变量从内存中删除
# 删除数据建议使用列表提供的方法
name_list = ["zhangsan", "wangwu", "lisi", "wamgwu"]
del name_list[1]

# 4.计数
# count方法可以统计列表中某个数据出现的次数
count = name_list.count("wangwu")

# 5.排序
name_list = ["zhangsan", "wangwu", "lisi", "wangxiaoer"]
num_list = [2, 1, 0, 3]
# # 升序
# name_list.sort()
# num_list.sort()
# # 降序
# name_list.sort(reverse=False)
# num_list.sort(reverse=False)
# 逆序
name_list.reverse()
num_list.reverse()

# 列表的循环遍历
name_list = ["zhangsan", "wangwu", "lisi", "wangxiaoer"]
for name in name_list:
    print('my name is %s' % name)

# 不同列表创建方式内存占用情况
sys.getsizeof([0] * 3)   # 80
sys.getsizeof([0, 0, 0])  # 120
sys.getsizeof([0 for _ in range(3)])   # 88

# 转换为字节码
dis.dis("[0] * 3")  # BINARY_MULTIPLY -> list_repeat
dis.dis("[0, 0, 0]")  # LIST_EXTEND
dis.dis("[0 for _ in range(3)]")  # LIST_APPEND

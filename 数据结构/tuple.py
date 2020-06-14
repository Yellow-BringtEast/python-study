"""
元组与列表类似，但元祖中的元素不能修改。
"""

# 一个元组的示例
info_tuple = ('zhangsan', 18, 1.75, 1.75)

# 创建一个空元组
empty_tuple = ()

# 创建只包含一个元素的元祖
single_tuple = (5, )

# 元祖的常用方法
# 1. 取值和索引
print(info_tuple[0])
print(info_tuple.index(18))

# 2. 统计计数
print(info_tuple.count(1.75))
# 统计元组中的元素数量
print(len(info_tuple))

# 循环遍历 - 实际开发中针对元组循环遍历的情况较少，因为元组多保存不同类型的数据
for i in info_tuple:
    print(i)

# 格式化字符串后面的'()'本质上就是一个元组
info_tuple = ('小明', 18, 1.75)
print('%s 年龄是 %d , 身高是 %.2f' % info_tuple)

# 元组与列表之间的转换
num_list = [1, 2, 3, 4]
print(type(num_list))

# 1. 列表转换为元组 - tuple()
num_tuple = tuple(num_list)
print(type(num_tuple))

# 2. 元组转为列表 - list()
num2_list = list(num_tuple)
print(type(num2_list))


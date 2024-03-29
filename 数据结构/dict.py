"""
字典是除列表以外python中最灵活的数据类型
字典同样可以储存多个数据
字典使用键值对存储数据
字典是无序的数据集合
"""
from objprint import op

# 一个字典的示例
xiaoming = {"name": "小明",
            "age": 18,
            "gender": "male",
            "height": 1.75}

# 使用print函数输出时，输出的顺序和定义的顺序是不同的
print(xiaoming)

# 字典的常用方法
# 1. 取值 - 指定key，而非索引值
print(xiaoming["name"])

# 2. 增加/修改 - key不存在，新增键值对；key存在，修改键值对
xiaoming["weight"] = 75.5
xiaoming["name"] = "小黄"

# 3. 删除
xiaoming.pop("weight")

# 4. 统计建值对的数量
print(len(xiaoming))

# 5. 合并字典 - 如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
temp_dict = {"weight": 75.5,
             "age": 20}
xiaoming.update(temp_dict)

# 6. 清空字典
xiaoming.clear()

# 循环遍历
xiaoming = {"name": "小明",
            "age": 18,
            "gender": "male",
            "height": 1.75}

# k是每一次循环中获取到的键值对的key
for k in xiaoming:
    print("%s - %s" % (k, xiaoming[k]))


# 字典的键可以用自定义类型的对象
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # 重载__eq__和__hash__可以让自定义类型在实例化相同的情况下被视为字典的同一个key
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        return self.x == other.x and \
            self.y == other.y


# key是判断的是内存上的id
d = {}
pos = Position(0, 1)
d[pos] = 1
op(d)
pos2 = Position(0, 1)
d[pos2] = 2
op(d)

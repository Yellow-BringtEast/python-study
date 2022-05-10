"""
生成器 - 特殊的生成器
gen: 生成器函数 - 当函数体有yield关键词时，python解释器会给该函数打上一个生成器函数的标签
g: 生成器对象 - 调用生成器函数会生成一个生成器对象
"""


# 简单实现
def gen(num):
    while num > 0:
        yield num
        num -= 1
    return


# 不会返回以一个函数值，而是返回一个生成器对象保存在g中
g = gen(5)
# for i in g:
#     print(i)

# 生成器也可以使用next函数，但对生成对象使用next函数时，才会运行函数体
f = next(g)

for i in g:
    print(i)


# 链表 - 生成器实现
class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next


node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)

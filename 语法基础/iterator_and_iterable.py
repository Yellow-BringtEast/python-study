"""
iterable：可迭代对象，可以一个一个的返回（return）他的成员，例如list, str 和 tuple;
iterator: 迭代器，一个表示数据流的对象，可以调用next()函数，不断从这个对象中获取新的数据数据；
区别：
high-level: iterable - 数据保存者（container），可以没有状态，他不需要知道iterator数到哪里了，
只需要有能力产生一个iterator; 而iterator一定是有状态的，但他并不需要实现一个container。
实现上：iterable要么有__iter__这个method，要么是个Sequence，有__getitem__这个method，
才能保证它在iter()函数的作用下返回一个iterator。而iterator必须要有__next__这个method，
这个method保证它在被next()作用的时候可以返回一下iterable里面的值
"""

import dis

s = """
lst = [0, 1, 2, 3,4]
for i in lst:
    print(i)
"""

# GET_ITER:从栈顶的iterable里拿出他所对应的iterator
# 在进行for loop前，lst会先被取一个iter的值：iter(lst)
dis.dis(s)


# 链表的实现 - iterator and iterable
class NodeIter:
    def __init__(self, node: 'Node') -> None:
        self.curr_node = node

    def __next__(self) -> 'Node':
        if self.curr_node is None:
            raise StopIteration
        node, self.curr_node = self.curr_node, self.curr_node.next
        return node

    def __iter__(self):
        return self


class Node:
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self) -> 'NodeIter':
        return NodeIter(self)


node1 = Node('node1')
node2 = Node('node2')
node3 = Node('node3')
node1.next = node2
node2.next = node3

for node in node1:
    print(node.name)

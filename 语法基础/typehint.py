from typing import List, Sequence, Union


# typehint
def f(a: int, b: int) -> int:
    return a + b


print(f(1, 2))


# 自定义数据类型
class A:
    name = 'A'


def get_name(o: A) -> str:
    return o.name

get_name(A)
get_name(A())


# 当类型对象为自身时，加引号解决循环依赖的问题
class Node:
    def __init__(self, prev: 'Node') -> None:
        self.prev = prev
        self.next = None


# 内置数据结构 - 一般使用Sequence替代List等序列化的数据结构
def my_sum(lst: Sequence[int]) -> int:
    total = 0
    for i in lst:
        total += i
    return total


my_sum([0, 1, 2])
my_sum(1)


# 传入参数有2个及以上类型时
def f(x: Union[int, None]) -> int:
    if x is None:
        return 0
    return x


f(None)
f(0)

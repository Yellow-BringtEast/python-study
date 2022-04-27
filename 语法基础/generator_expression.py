# 普通列表
lst = [1, 2, 3, 4, 5]

# 生成器表达式
g = (n for n in lst if n in lst)
lst = [0, 1, 2]
print(list(g))  # [1, 2]

# 等价写法
lst = [1, 2, 3, 4, 5]


def __g(it):
    for n in it:
        if n in lst:
            yield n


g = __g(iter(lst))

lst = [0, 1, 2]
print(list(g))

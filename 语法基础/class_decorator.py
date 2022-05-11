"""
在一个函数上做装饰器就等价于这个函数名等于装饰器调用这个函数
"""

import time


class Timer:
    def __init__(self, func):
        self.func = func

    # 让所有这个类的实例都变成callable
    def __call__(self, *args, **kwargs):
        start = time.time()
        ret = self.func(*args, **kwargs)
        print(f'Time: {time.time() - start}')
        return ret


@Timer
def add(a, b):
    return a + b


print(type(add))

# 等价于
add = Timer(add)

print(add(1, 3))

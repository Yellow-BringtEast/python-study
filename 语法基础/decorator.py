import time


# 函数也是一个普通的object,可以被当做参数传入另一个函数
def double(x):
    return x * 2


def triple(x):
    return x * 3


def calc_number(func, x):
    print(func(x))


calc_number(double, 3)
calc_number(triple, 3)


# 函数本身也可以作为一个返回值被一个函数返回
def get_multiple_func(n):
    def multiple_func(x):
        return n * x

    return multiple_func


double = get_multiple_func(2)
triple = get_multiple_func(3)

print(double(3))
print(triple(3))


# decorator本身可以理解为一个函数
def dec(f):
    pass


# 完全等价于 dou = dec(dou)
@dec
def dou(x):
    return x * 2


# 装饰器示例
def timeit(f):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = f(*args, **kwargs)
        print(time.time() - start)
        return ret

    return wrapper


@timeit
def my_func(x):
    time.sleep(x)


my_func(1)


# 装饰器含有参数
def timeit(iteration):
    def inner(f):
        def wrapper(*args, **kwargs):
            start = time.time()
            for _ in range(iteration):
                ret = f(*args, **kwargs)
            print(time.time() - start)
            return ret

        return wrapper

    return inner


@timeit(100)
def double(x):
    return x * 2


# 等价于
# inner = timeit(100)
# double = inner(double)
double(2)

# 合法变量名由字母、数字及下划线组成且第一个字符不能为数字
# wrong: 1a = 2
import random

abc_123 = 0

# python3支持中文变量名
你好 = 'hello'
print(你好)

# 好变量名
# 内容：变量名尽可能多的传递有效信息
# username更好
n = 'Bob'
name = 'Bob'
username = 'Bob'

# 但需要平衡变量名长度和有效信息
# wrong:
the_username_from_my_database_on_aws = 'Bob'

# 形式：
# 变量（除常量和类外）：lower_underscore
# 常量：UPPER_UNDERSCORE
# 类：双驼峰
car_nums = 10

DEFAULT_INIT = 1


class MyClass:
    pass


# 前置下划线
# 单下划线：_ - 当做占位符
for _ in range(10):
    print(random.random())

# 一个前置下划线
# 弱私有：语义上表达private，约定俗成的，可以强行调用
_data_cache: dict = {}


def calculate(x):
    if x in _data_cache:
        return _data_cache[x]
    return x ** 2


class MyClass:
    @staticmethod
    def _get_raw():
        print('oh no')


o = MyClass()
o._get_raw()


# 类中的2个前置下划线
# 强私用（防君子不防小人，可用MyClass1._MyClass1__get_raw()
class MyClass1:
    @staticmethod
    def __get_raw():
        print('oh no')


o = MyClass1()
MyClass1._MyClass1__get_raw()
o.__get_raw()

# 命名时千万不要覆盖 builtin functions
# wrong: list = [1, 2, 3]

# 文件名不要与内置的 module 重名

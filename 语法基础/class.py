import dis

s = """
class A:
    name = 'qqq'

    def f(self):
        print(1)
"""

# 字节码
dis.dis(s)
"""
当我们定义了一个新的class时，首先相当于运行了所有定义在class里面的代码，
然后把产生的所有局部变量的名字及其对应的值，都保存在class.__dict__里面，
然后创建了一个type，赋值给这个class的名字的变量（A）；
建立一个类需要三个过程:第一类的名字，第二类的父类（默认为object）,
第三class.__dict__,最后可以使用type()动态的去创建一个类。
"""


class A:
    name = 'qqq'

    def f(self):
        print(1)


# class的type都是type
print(type(A))


# 上面的定义方法等价于
def f(self):
    print(1)


d = {
    "name": "qqq",
    "f": f
}

A = type('A', (), d)
print(A.__dict__)

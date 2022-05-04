# staticmethod
class A:
    @staticmethod
    def f(x):
        print(x)


# staticmethod可以被类及其对象调用
A.f(2)
A().f(1)


# classmethod
class B:
    @classmethod
    def f(cls, x):
        print(cls, x)


# classmethod也是如此
B.f(1)
B().f(2)

# 类中的staticmethod修饰的函数本质上是一个staticmethod object
print(A.f)
print(A.__dict__['f'])

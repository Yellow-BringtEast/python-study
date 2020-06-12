"""
python中数字类型包括整型int、浮点float、复数complex，还支持包括十进制小数decimal以及分数fraction等类型
"""

from decimal import Decimal
from fractions import Fraction

# 除法永远返回一个浮点数
a = 8 / 5
print(type(a))

# 地板除 // - 得到比结果小的第一个整数
a = 9 // -2    # 结果为-5

# 取余数 %
a = 7 % 2

# 乘方 **
a = 5 ** 2

# 包含多种混合类型运算数的运算会把整数转换为浮点数
a = 4 * 3.75 - 1
print(a)
print(type(a))

# 复数
a = 5 + 6j

# python中计算精度的一个示例
a = 1
b = 9

print("a/b:", a / b)
print("Decimal(a/b):", Decimal(a / b))
print("Decimal(a):", Decimal(a))
print("Decimal(b):", Decimal(b))
print('Decimal(a)/Decimal(b):', Decimal(a) / Decimal(b))
print('Fraction(a,b)',Fraction(a,b))

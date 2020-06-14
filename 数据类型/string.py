"""
字符串有多种形式，可以使用单引号（'...'），双引号（"..."）都可以获得同样的结果 。反斜杠可以用来转义
"""
# 单引号
string = 'hello word'

# 当字符串中有引号时
# 1. 用\转义引号 - \'表示'仅仅是个单引号，不与前面的单引号构成一组'...'
string = 'don\'t'
string = "\"Yes,\" they said."

# 2. 或者使用不同的引号
string = "don't"
string = '"Yes," they said.'

# 原始字符串 - 引号前添加r，不希望前置了\的字符转义成特殊字符
print('C:\some\name')
print(r'C:\some\name')

# 字符串可以跨行连续输入
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")  # 字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个\即可

# 字符串可以用 + 进行连接（粘到一起），也可以用 * 进行重复
print("3 * un + ium")

# 相邻的两个或多个字符串（引号引起来的字符）将会自动连接到一起
print('Py''thon')

# 把很长的字符串拆开分别输入的时候尤其有用
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

# 只能对两个字面值这样操作，变量或表达式不行
# prefix = 'Py'
# print(prefix'thon')

# 连接变量，或者连接变量和字面值，可以用+号
prefix = 'Py'
print(prefix + 'thon')

# 字符串可以被索引，第一个字符的索引为0
string = 'hello word'
print(string[0])
print(string[-1])  # 索引为负数时，表示从右边开始数，由于-0 = 0，所以右边第一个为-1

# 字符串还支持切片，索引可以得到单个字符，而切片可以获取子字符串
print(string[0:2])  # 切片的开始总是包括在结果中的，而结束不被包括

# 切片的索引有默认值；省略开始索引时默认为0，省略结束索引时默认为到字符串的结束
print(string[:2])
print(string[2:])

# 试图使用过大的索引会产生一个错误，切片中的越界索引会被自动处理
# print(string[42])
print(string[4::42])

# Python中的字符串不能被修改，向字符串的某个索引位置赋值会产生一个错误
# string[0] = 'J'

# 内建函数 len() 返回一个字符串的长度
a = len(string)
print(a)

# 循环遍历
str1 = "hello python"

for char in str1:
    print(char)

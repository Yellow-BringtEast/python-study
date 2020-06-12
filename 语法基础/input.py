# python 3.x 中input()函数接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。
temp = input("请输入您的姓名:")

# type()如果你只有第一个参数则返回对象的类型
type(temp)

print("你好，" + temp + "!")

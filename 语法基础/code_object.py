def f(a, b=3, /,  *args, **kwargs):
    """
    /前的参数必须是 positional only 的
    """
    pass


print(f.__code__)
print(dir(f.__code__))


code = f.__code__

# 保存二进制的byte code
print(code.co_code)

# metadata:
print(code.co_name)  # 名称
print(code.co_filename)  # 文件
print(code.co_lnotab)  # mapping

# run time虚拟机需要的数据
print(code.co_flags)  # bit map
print(code.co_stacksize)  # 栈空间大小

# 输入参数的数量 - 函数重载的基础
print(code.co_argcount)  # 参数数量，不包含 keyword only arguments, * 或者 **args
print(code.co_posonlyargcount)  # positional only arguments 的数量
print(code.co_kwonlyargcount)  # keyword only arguments 的数量，不包含 **args

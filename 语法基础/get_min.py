# bif - min()的实现
# x为包括一系列数字的列表
def min(x):
    # 取出列表中的第一个元素
    least = x[0]
    # 取出列表中每一个元素
    for i in x:
        # 判断它与第一个元素的大小，如它小，则把它赋值给least。
        if i < least:
            least = i
    # 返回least的值
    return least

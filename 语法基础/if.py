# if方法进行判断
temp = input("请输入1到100之间的数字：")
guess = int(temp)

# 最简单的if语法
if 1 <= guess <= 100:
    print("你妹好漂亮!")
else:
    print("你大爷好丑!")

# 进阶版 - 条件成立时执行 if 条件 else 条件不成立时执行
print("你妹好漂亮!（进阶版）") if 1 <= guess <= 100 else print("你大爷好丑!（进阶版）")

# 多个判断条件时
if 1 <= guess < 30:
    print('30以下')
elif 30 <= guess < 50
    print('30~50之间')
else:
    print('50~100之间')


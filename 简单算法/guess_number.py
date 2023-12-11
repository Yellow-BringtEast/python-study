import random

c = 3
# randint随机生成1~10之间的一个整数
answer = random.randint(1, 10)

while c > 0:
    temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
    # 判断输入的字符串是否为整数
    while not temp.isdigit():
        temp = input("抱歉，您的输入有误，请输入一个整数：")

    # 将输入的字符串转换为整型
    guess = int(temp)

    # 判断用户输入与随机生成的数是否相等
    if guess == answer:
        print("你是小甲鱼的蛔虫嘛？！")
        print("哼，猜中了也没奖励")
        break
    else:
        if guess < answer:
            print("小啦~")
        else:
            print("大啦~")
        c = c - 1

# 相同类型的数据可以使用+号进行连接
print('正确答案是' + str(answer) + '啦！')

print("游戏结束，不玩啦")

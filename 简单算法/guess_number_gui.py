from easygui import *
import random
answer = random.randint(1,10)
c = 3

while c > 0:
    # 整型输入，要求用户填写一个整数，返回值为该数。如果输入不为整型，返回一个错误警告，要求用户输入整型。
    temp = integerbox(msg='不妨猜一下小甲鱼现在心里想的是哪个数（1~10）', title='数字小游戏', lowerbound=1, upperbound=10)
    if temp == answer:
        msgbox("你是小甲鱼的蛔虫嘛？！")
        msgbox("哼，猜中了也没奖励")
        break
    else:
        if temp < answer:
            msgbox("小啦~")
        else:
            msgbox("大啦~")
        c = c-1

msgbox('正确答案是'+str(answer)+'啦！')

msgbox("游戏结束，不玩啦")
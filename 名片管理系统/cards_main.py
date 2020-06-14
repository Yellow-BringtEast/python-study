from cards_tools import *

# 无限循环，由用户决定什么时候退出
while True:
    # 显示功能菜单
    show_menu()

    action = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action)

    # 1, 2, 3 针对名片的操作
    if action in ["1", "2", "3"]:

        # 新增名片
        if action == "1":
            new_card()

        # 显示名片
        elif action == "2":
            show_all()

        # 查询名片
        elif action == "3":
            search_card()

    # 0 退出系统
    elif action == "0":
        print("欢迎再次使用【名片管理系统】")
        break

    # 其他内容输入错误，需要提醒重新输入
    else:
        print("您输入的内容不正确，请重新选择。")
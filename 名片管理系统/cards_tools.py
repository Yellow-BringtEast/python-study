# 所有名片记录的列表
card_list = []

# 分隔线符号重复次数
char_num = 50

def show_menu():
    """显示菜单"""
    print("*" * char_num)
    print("欢迎使用【名片管理系统】 V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("")
    print("0. 退出系统")
    print("*" * char_num)

def new_card():
    """新增名片"""
    print("-" * char_num)
    print("新增名片")

    # 1. 提示用户输入名片的详细信息
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话：")
    qq_str = input("请输入qq：")
    email_str = input("请输入邮箱：")

    # 2. 使用用户输入的信息建立一个名片字典
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}

    # 3. 将名片字典添加到列表中
    card_list.append(card_dict)

    # 4. 提示用户添加成功
    print("添加 %s 的名片成功！" % name_str)

def show_all():
    """显示名片"""
    print("-" * char_num)
    print("显示所有名片")

    # 判断是否存在名片记录
    if len(card_list) == 0:
        print("当前没有任何名片记录，请使用新增名片功能添加名片！")

        # return 下方代码不会执行
        return

    # 打印表头
    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t\t")

    print("")

    # 打印分隔线
    print("=" * char_num)

    # 遍历名片列表，依次输出信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                        card_dict["phone"],
                                        card_dict["qq"],
                                        card_dict["email"]))

def search_card():
    """搜索名片"""
    print("-" * char_num)
    print("搜索名片")

    # 1. 提示用户要输入的姓名
    find_name = input("请输入要搜索的姓名：")

    # 2. 遍历名片列表，查询需要搜索的信息
    for card_dict in card_list:

        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                                card_dict["phone"],
                                                card_dict["qq"],
                                                card_dict["email"]))

            # 修改/删除查找到的名片
            deal_card(card_dict)

            break

    else:
        print("抱歉，没有找到 %s" % find_name)

def deal_card(find_dict):
    """
    处理查找到的名片
    @param find_dict:查找到的名片
    """
    action = input("请选择要执行的操作"
                   "（1.修改，2.删除，0.返回上级菜单）：")

    if action == 1:

        find_dict["name"] = input_card_info(find_dict["name"], "修改姓名（回车不修改）")
        find_dict["phone"] = input_card_info(find_dict["phone"], "修改电话（回车不修改）")
        find_dict["qq"] = input_card_info(find_dict["qq"], "修改QQ（回车不修改）")
        find_dict["email"] = input_card_info(find_dict["email"], "修改邮箱（回车不修改）")

        print("修改名片成功！")

    elif action == 2:

        card_list.remove(find_dict)

        print("删除名片成功！")

def input_card_info(dict_value, tip_message):
    """
    处理名片信息
    @param dict_value:原有名片字典中的值
    @param tip_message:提示信息
    @return:如果用户有输入就返回用户输入的值，如果没有输入就返回名片字典原有的值
    """
    # 1. 提示用户输入内容
    result_str = input(tip_message)

    # 2. 根据用户输入的内容进行判断
    if len(result_str) > 0:

        return result_str

    # 3. 如果没有输入内容，返回原有的值
    else:

        return dict_value
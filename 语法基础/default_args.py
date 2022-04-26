# wrong
# class Player:
#     # python在初始化参数时，只会对默认参数求一次值，此时items为一个空列表
#     def __init__(self, name, items=[]):
#         self.name = name
#         self.items = items
#         print(id(self.items))


# correct
class Player:
    def __init__(self, name, items=None):
        self.name = name
        if items is None:
            self.items = []
        else:
            self.items = items
        print(id(self.items))


# 实例化对象时， p1和p2共享了同一个空的list
p1 = Player('Alice')
p2 = Player('Bob')
p3 = Player('Tim', ['sword'])

# 对实例p1,p2新增属性时，items的引用指向同一个内存地址
p1.items.append('armor')
p2.items.append('sword')

print(p1.items)  # ['armor', 'sword']

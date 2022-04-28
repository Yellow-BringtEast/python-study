a = None

if a:
    print('not none')

if a == None:
    print('None')

if a is None:
    print("None")

lst = [[], {}, None, False]

# __bool__()可能被重载
for i in lst:
    if i:
        print(i)

# __eq__()可能被重载
for i in lst:
    if i == None:
        print(i)

# 最优解
for i in lst:
    if i is None:
        print(i)

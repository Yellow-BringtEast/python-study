# 一个简单的密码验证器，限定3次机会
c = 3
password = '714376214'

while c:
    psd = input('请输入密码：')
    if psd == password:
        print('密码正确，欢迎回来。')
        break
    elif '*' in psd:
        print('密码中不能含有“*”号！您还有', c, '次机会！', end = ' ')
        continue
    else:
        print('密码输入错误！您还有', c-1, '次机会！', end=' ')
    c -= 1

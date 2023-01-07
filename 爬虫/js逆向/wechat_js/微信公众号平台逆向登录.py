import execjs


# 明文密码加密
def encrypt_pwd(pwd):
    return execjs.compile(open('./pwd_encrypt.js', 'r', encoding='utf8').read()).call('getPWD', pwd)

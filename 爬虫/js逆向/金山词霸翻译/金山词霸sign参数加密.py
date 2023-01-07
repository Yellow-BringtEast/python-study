import requests
import hashlib


class JinFY:
    def __init__(self, word):
        self.url = 'https://ifanyi.iciba.com/index.php?c=trans&m=fy&client=6&auth_user=key_web_fanyi&sign='
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54'
        }
        self.word = word
        self.data = {
            'from': 'auto',
            'to': 'auto',
            'q': self.word
        }

    # md5加密获得sign
    def md5_encrypt(self):
        sign = hashlib.md5(f'6key_web_fanyiifanyiweb8hc9s98e{self.word}'.encode('utf8')).hexdigest()[:16]
        url = self.url + sign
        return url

    # 获取翻译结果
    def get_data(self):
        res = requests.post(url=self.md5_encrypt(), headers=self.header, data=self.data).json()
        print(res['content']['out'])


if __name__ == '__main__':
    while True:
        word = input('需要翻译的词语: ')
        if word.lower() == 'q':
            break
        fanyi = JinFY(word)
        fanyi.get_data()

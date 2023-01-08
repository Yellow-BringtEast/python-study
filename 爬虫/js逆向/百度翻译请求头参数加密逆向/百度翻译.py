import requests
import execjs
import re


class BaiduFY:
    def __init__(self, word=None):
        self.word = word
        self.header = {
            'Cookie': 'BAIDUID=B03EDE0CCFE1CC05458FADBAF639C2F8:FG=1; BAIDUID_BFESS=B03EDE0CCFE1CC05458FADBAF639C2F8:FG=1; APPGUIDE_10_0_2=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1673098781; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1673098781; ab_sr=1.0.1_ZjRmNGRlZmY5NzY0NzYyOWQ5ZDY4ODFkZjUyNTMwNGNmYzk1YmE3Njk4YTYzNzg1YjUxN2I0ZGI1ZTQ2MDkxYTkxNWRhNzVkOTM1OTlmMjc5N2RjNzA4NWIxNDM2NmZiY2YzZGE1YjQ1ZGM1YzQyODk3NzM1NjU1ZWNkNjZiZDkwYzFhYzc1YzQ4NzY2YmJkZDZjNDBmYjc1ZmJjY2RmYQ==',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54',
        }

    def get_token(self):
        url = 'https://fanyi.baidu.com/'
        res = requests.get(url, headers=self.header).text
        token_comp = re.compile("token: '(?P<token>.*?)'", re.S)
        token = token_comp.search(res).group(1)
        return token

    def get_sign(self):
        return execjs.compile(open('./baidu_encrypt.js', 'r', encoding='utf8').read()).call('encrypt', self.word)

    def get_data(self):
        url = 'https://fanyi.baidu.com/v2transapi'
        data = {
            'from': 'auto',
            'to': 'auto',
            'query': self.word,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': self.get_sign(),
            'token': self.get_token(),
            'domain': 'common'
        }
        print(data)
        res = requests.post(url=url, headers=self.header, data=data).json()
        return res


if __name__ == '__main__':
    while True:
        word = input("需要翻译的句子：")
        if word.lower() == 'q':
            break
        fy = BaiduFY(word)
        res = fy.get_data()
        print(res)

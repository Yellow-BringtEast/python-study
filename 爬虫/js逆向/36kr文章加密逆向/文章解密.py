import requests
from lxml import etree
import json

# 解决execjs.call报错
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs

# 从html文件中获取文章加密数据
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43'
}

url = 'https://36kr.com/p/2305564636474629'

res = requests.get(url=url, headers=headers)
html = etree.HTML(res.text)
encrypt_data = json.loads(html.findall('*//script')[-3].text.replace('window.initialState=', ''))['state']

# js解密
decrypt = execjs.compile(open('./decrypt.js', 'r', encoding='utf8').read())
data = decrypt.call('decrypt', encrypt_data)
content = json.loads(data)['articleDetail']['articleDetailData']['data']['widgetContent']
print(content)


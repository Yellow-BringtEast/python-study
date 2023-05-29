import requests
import json

# 解决execjs.call报错
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding='utf-8')

import execjs


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50'
}

url = 'https://jzsc.mohurd.gov.cn/APi/webApi/dataservice/query/staff/list?pg=0&pgsz=15&total=0'

res = requests.get(url=url, headers=header).text

decrypt = execjs.compile(open('./decrypt.js', 'r', encoding='utf8').read())
data = json.loads(decrypt.call('h', res))

print(data)

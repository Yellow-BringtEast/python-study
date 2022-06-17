import toools
from configparser import ConfigParser

config = ConfigParser()
config.read('./config.cfg')

# 腾讯云api调用凭证
key = config['tencent_cloud']['key']
secret = config['tencent_cloud']['secret']

if __name__ == '__main__':
    img_list = toools.cut_pic('1.png')
    for img in img_list:
        toools.img_to_excel(img.split('.')[0], img, key, secret)

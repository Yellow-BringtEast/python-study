"""
通过网易云接口获取某位歌手的歌词，并生成词云
"""

import time
from wordcloud import WordCloud
import jieba
from selenium import webdriver


# 得到指定歌手的页面，热门前50首歌曲的ID，歌曲名; 许嵩-artist_id='5771'
def get_songs(artist_id='5771'):
    # 歌手个人页面
    page_url = 'https://music.163.com/#/artist?id=' + artist_id

    # 使用selenium获取iframe内歌手的热门曲目url及歌名
    browser = webdriver.Edge()
    browser.get(page_url)
    time.sleep(3)

    # 进入iframe内获取对应元素的属性值
    browser.switch_to.frame('g_iframe')
    song_urls = browser.find_elements(by='xpath', value='//*[@id="hotsong-list"]//span/a')
    song_names = browser.find_elements(by='xpath', value='//*[@id="hotsong-list"]//span/a/b')

    url_list = []
    name_list = []

    for url_element, name_element in zip(song_urls, song_names):
        url = url_element.get_attribute('href')
        url_list.append(url)

        name = name_element.get_attribute('title')
        name_list.append(name)

    return url_list, name_list


# 得到某首歌的歌词
def get_lyric(song_url):
    # 使用selenium获取iframe内的歌词
    browser = webdriver.Edge()
    browser.get(song_url)
    time.sleep(1)

    # 进入iframe内获取歌词
    browser.switch_to.frame('g_iframe')
    res = browser.find_element(by='xpath', value='//*[@id="lyric-content"]').text.strip('展开').strip('\n')
    browser.find_element(by='id', value='flag_ctrl').click()
    res_more = browser.find_element(by='xpath', value='//*[@id="lyric-content"]/div').text
    lyric = res + res_more

    return lyric


# 去掉停用词
def remove_stop_words(f):
    stop_words = ['作词', '作曲', '编曲', 'Arranger', '录音', '混音', '人声', 'Vocal', '弦乐', 'Keyboard', '键盘', '编辑',
                  '助理', 'Assistants', 'Mixing', 'Editing', 'Recording', '音乐', '制作', 'Producer', '发行', 'produced',
                  'and', 'distributed', '许嵩']

    for stop_word in stop_words:
        f = f.replace(stop_word, '')
    return f


# 生成词云
def create_word_cloud(f):
    f = remove_stop_words(f)
    cut_text = " ".join(jieba.cut(f, cut_all=False, HMM=True))
    jieba.setLogLevel(jieba.logging.INFO)
    wc = WordCloud(
        font_path='simsun.ttc',
        max_words=100,
        width=2000,
        height=1200
    )
    wordcloud = wc.generate(cut_text)

    # 写词云图片
    wordcloud.to_file('./wordcloud.jpg')


if __name__ == '__main__':
    urls, names = get_songs()

    # 所有歌词
    all_word = ''
    for url, name in zip(urls, names):
        lyric = get_lyric(url)
        all_word = all_word + ' ' + lyric
        print(name)
    with open('./all_word.txt', 'w', encoding='utf-8') as f:
        f.write(all_word)
        f.close()

    print('开始创建词云')

    create_word_cloud(all_word)

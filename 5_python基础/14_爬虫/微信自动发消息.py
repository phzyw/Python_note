import requests
from lxml import etree
import time
import random
import os 
import keyboard  # 导入keyboard库
from wxauto import *

def fetch_and_send_weibo_hotsearch():
    # 请求的 URL 和头信息
    url = 'https://s.weibo.com/top/summary'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
        'referer': 'https://s.weibo.com/',
        'cookie': 'SINAGLOBAL=8795647830130.211.1724637477073; SUB=_2AkMRhbS1f8NxqwFRmf0QyG_gao1-wwHEieKn2UVuJRMxHRl-yT8XqnNetRB6OgWaWrhk6W3RJLV4EK2CFFfamKC6rFSw; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WWLJokng_k2WTXpa-eCppPT; _s_tentry=passport.weibo.com; Apache=9472618530068.941.1725512578444; ULV=1725512578466:2:1:1:9472618530068.941.1725512578444:1724637477076; UOR=,,www.baidu.com'
    }

    # 发送请求获取网页内容
    html_str = requests.get(url=url, headers=headers)

    # 解析网页内容
    xpath_str = etree.HTML(html_str.text)
    trs = xpath_str.xpath('/html/body/div[1]/div[2]/div/div[2]/div[1]/table/tbody/tr')

    def getText(list):
        try:
            return list[0].strip()
        except:
            return ''

    # 获取当前用户的桌面路径
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')
    file_path = os.path.join(desktop_path, '微博热搜top10.txt')

    # 打开文件准备写入数据
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('-'*12 + "微博热搜Top10" + '-'*12 + '\n')

        # 遍历表格行
        for tr in trs:
            id = getText(tr.xpath('./td[1]/text()'))  # 获取热搜 ID
            title = getText(tr.xpath('./td[2]/a/text()'))  # 获取热搜标题
            number = getText(tr.xpath('./td[2]/span/text()'))  # 获取热度

            # 获取前10条数据
            if id.isdigit() and int(id) <= 10:
                file.write(id + '.  ' + title + '\n')

    # 等待 1 到 3 秒
    time.sleep(random.randint(1, 3))
    print('写入成功')

    # 读取 .txt 文件内容
    with open(file_path, 'r', encoding='utf-8') as file:
        msg = file.read()  # 读取文件内容

    # 获取当前微信客户端
    wx = WeChat()
    # 向某人发送消息（以`文件传输助手`为例）
    who = '文件传输助手'
    wx.SendMsg(msg, who)  # 向`文件传输助手`发送消息，内容为.txt文件的内容

# 定时任务，每隔 20 秒执行一次
while True:
    if keyboard.is_pressed('space'):  # 检查空格键是否按下
        print("程序已停止")
        break  # 停止循环，结束程序

    fetch_and_send_weibo_hotsearch()  # 执行爬取和发送任务
    time.sleep(20)  # 每隔20秒运行一次

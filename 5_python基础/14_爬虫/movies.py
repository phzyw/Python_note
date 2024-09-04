
# 爬取豆瓣数据
https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=
import random
import time
import requests
import json

# 1.获取抓取的页数
pages = int(input('请输入你想抓取的数据页数：'))
# print(pages,type(pages))

# 2.定义用户代理
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# 3.根据输入的抓取页数来决定循环次数
for i in range(pages):
    # 4.定义请求的url链接
    url = f'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start={i*20}&limit=20'
    # 5.发送网络请求，获取相应对象
    response = requests.get(url,headers = headers)

    json_data = response.json()
    
    for json in json_data:
        # 6.将获取到的字典数据保存到文件中
        with open(f'C:/Users/CJJ/Desktop/douban_movie.txt','a',encoding='utf-8') as f:
            f.write(str(json) + ',\n')
                

    # 7.提示下载成功，同时随机休眠几秒，避免被检测为爬虫
    print(f'第{i+1}页下载成功')
    # secondes  = random.randint(3,6)
    secondes  = round(random.uniform(3,6),1)
    time.sleep(secondes)
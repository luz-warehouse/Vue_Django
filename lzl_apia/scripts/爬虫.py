import requests
import re

header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}

url = 'https://quanxiaoshuo.com'

url2 = 'https://quanxiaoshuo.com/top/%s/'

url1 = 'https://quanxiaoshuo.com/top/1/'

res = requests.get(url1,headers=header)

# print(res.text)
from bs4 import BeautifulSoup

soup = BeautifulSoup(res.text,'html.parser')

ul_list = soup.find_all(name='li',class_='cc2')

for ul in ul_list:
    # print(ul)
    a_tag = ul.find(name='a')
    if a_tag:
        # print(a_tag['href'])
        # 拿到每个小说的ID
        article_id = a_tag['href']

        # 获取每个小说的名字
        name=a_tag.text

        url_now = url + article_id

        req = requests.get(url_now,headers=header,)

        soup1 = BeautifulSoup(req.text,'html.parser')


        # 拿到每本书的简介
        desc = soup1.find(class_='desc').text

        # 拿到所有的a标签，并且有title属性的
        list1 = soup1.find_all('div',class_='chapter')[:300]
        for a in list1:
            a_tag = a.find(name='a')
            if a_tag:

                # 拿到文章的标签ID
                biaoqian_id = a_tag['href']

                # 拿到所有的文章的章节名字
                zhangjie_name = a_tag.text

                content_url = url + biaoqian_id

                nr = requests.get(content_url,headers=header)
                # print(nr.text)
                soup2 = BeautifulSoup(nr.text,'html.parser')
                print(soup2.find(id='content').text)
                # 拿到章节的内容
                content = soup2.find(id='content').text
                # zhangjie_content=re.findall('<br/>(.*?)<br/>',nr.text)
                # print(re.findall('<br/>(.*?)<br/>',nr.text)[0])
                break
                # print(zhangjie_name)
        # print()
        # print(soup1.find_all(title=True,name='a'))
        break












# import requests
# from bs4 import BeautifulSoup
#
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'read.settings.dev')
#
# import django
# django.setup()
#
# from apps.home.models import Book,BookZhangjie,ZhangjieDetail
#
# def name(proxies):
#
#
#     url = 'http://book.zongheng.com/store/c1/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html'
#     cook = 'ZHID=E9D5B576526FAF593F9256438860A74A; ver=2018; zh_visitTime=1628317697306; v_user=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D3TabsGqEby3ks6gaT-9MqTGDnp5Ss94NPs2ztcdrqHEH6A67Ue9BiuL7DppszE99%26wd%3D%26eqid%3Dc7aa57ea0008edf400000004610e27ff%7Chttp%3A%2F%2Fwww.zongheng.com%2F%7C42221202; Hm_up_c202865d524849216eea846069349eb9=%7B%22uid_%22%3A%7B%22value%22%3A%22E9D5B576526FAF593F9256438860A74A%22%2C%22scope%22%3A1%7D%7D; rSet=1_3_1_14; zhffr=www.baidu.com; Hm_lvt_c202865d524849216eea846069349eb9=1628317697,1628511827,1628604719,1628664374; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217b1f4c45685e-0999624e616bc6-7a697e6d-1049088-17b1f4c456910%22%2C%22%24device_id%22%3A%2217b1f4c45685e-0999624e616bc6-7a697e6d-1049088-17b1f4c456910%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; zh_rba=true; JSESSIONID=abcH8xeJvYBXl-S7ma0Sx; platform=H5; PassportCaptchaId=e574977e6a05463f7613c35e68e538e7; AST=16286765570487296cc8a3a; Hm_lpvt_c202865d524849216eea846069349eb9=1628669407'
#
#     header = {
#         'Cookie': cook,
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
#     }
#
#     res = requests.get(url, headers=header, proxies=proxies)
#
#     # print(res.text)
#     soup = BeautifulSoup(res.text, 'html.parser')
#     # print(soup)
#     book_div = soup.find_all(attrs={'class': 'bookimg'})
#
#     # print(book_div)
#     import random
#     for books in book_div:
#         # print('for')
#         # print(books)
#         # print(type(books))
#         # print('-*********************-')
#         # print(books.next_sibling.next_sibling.find(attrs={'class': 'bookintro'}).text)
#         # print(type(books.next_sibling.next_sibling))
#
#         # 书的简介
#         desc = books.next_sibling.next_sibling.find(attrs={'class': 'bookintro'}).text
#         # print(desc)
#
#         # 拿到书的url   ###########################################
#         book_url = books.a['href']
#
#         book = books.a.img
#
#         # 书名    ###########################################
#         book_name = book['alt']
#         # 书的图片
#         book_img = book['src']
#
#         # print(book_url)
#         # print(type(book_url))
#         book_url = book_url.replace('book/', 'showchapter/')
#
#         requ = requests.get(book_url, headers=header, proxies=proxies)
#
#         # print(requ.text)
#
#         soup1 = BeautifulSoup(requ.text, 'html.parser')
#
#         ul = soup1.find_all(attrs={'class': 'col-4'})
#
#         book_dic = {
#             'name': book_name,
#             'book_img': book_img,
#             'desc': desc,
#             'click_num': random.randint(200, 1000),
#             'zhangjie': random.randint(200, 2000),
#             'author_id': random.randint(1, 26),
#             'tag_id': random.randint(1, 6),
#             'gender_type_id': random.randint(1, 2)
#         }
#
#         book_obj = Book.objects.create(**book_dic)
#
#         for u in ul:
#             a = u.a
#
#             # 拿到章节的标题   ###########################################
#             a_tag = a.text
#
#             # 拿到章节href内容    ###########################################
#             a_href = a['href']
#             # print(a_href)
#             # print(a_tag)
#             reque = requests.get(a_href, headers=header, proxies=proxies)
#             # print(reque.text)
#             soup2 = BeautifulSoup(reque.text, 'html.parser')
#
#             # 章节的具体内容   ###########################################
#             content = soup2.find(attrs={'class': 'content'}).text
#
#             detail_obj = ZhangjieDetail.objects.create(content=content)
#
#             zhangjie_dic = {
#                 'name': a_tag,
#                 'book': book_obj,
#                 'detail': detail_obj
#             }
#
#             zhangjie_obj = BookZhangjie.objects.create(**zhangjie_dic)
#
# if __name__ == '__main__':
#
#     proxies = {
#         'https': 'https://60.168.81.102:1133',
#     }
#
#     name(proxies)
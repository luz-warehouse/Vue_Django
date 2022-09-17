
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'read.settings.dev')
    import django
    django.setup()

    from home import models

    import requests
    from bs4 import BeautifulSoup

    url = 'http://www.530p.com/dushi/tashenshangyoutiaolong-175288/'

    pj_url = 'http://www.530p.com'


    header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67',
    }

    res = requests.get(url,headers = header)
    resa = str(res.content,encoding='gbk')

    soup = BeautifulSoup(resa,'html.parser')

    cls = soup.find_all(attrs={
        'class':'clc'
    })

    for num,i in enumerate(cls[0:500]):

        # print(num,i)


        '''
        这是循环
        aaa
        '''

        a = i.find('a')['href']

        zhegeurl = pj_url + a

        request = requests.get(zhegeurl,headers=header)

        cp_content = str(request.content,encoding='gbk')

        soup1 = BeautifulSoup(cp_content,'html.parser')

        soup2 = soup1.find(id='cp_content')

        # print(str(soup2))

        obj = models.ZhangjieDetail.objects.filter(pk=num+1)

        if obj:
            obj.update(content = str(soup2))

        # obj.update(content = str(soup2))
        # obj.content = str(soup2)

        # obj.save()




if __name__ == '__main__':

    main()
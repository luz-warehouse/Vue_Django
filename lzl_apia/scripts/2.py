# import requests
# from bs4 import BeautifulSoup
#
# obj = requests.get('http://www.530p.com/dushi/tashenshangyoutiaolong-175288/')
# soup=BeautifulSoup(obj.text,'html.parser')
#
# book_list = soup.find_all(name='div',class_='clc')
# for x in book_list:
#     print(x.__dict__)
#     break

def Singleton(cls):
    instance = None

    def _singleton(*args, **kargs):
        nonlocal instance
        # print(instance)
        if not instance:
            instance = cls(*args, **kargs)

        return instance

    return _singleton


@Singleton
class A(object):
    def __init__(self, x=0):
        self.x = x


a1 = A(2)
a2 = A(3)
print(a1.x)
print(a2.x)

print(a1 is a2)
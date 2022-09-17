

import requests
from bs4 import BeautifulSoup
url = 'https://quanxiaoshuo.com/211749/'
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67'}

req = requests.get(url,headers=header)

# print(req.text)

soup = BeautifulSoup(req.text,'html.parser')

desc = soup.find(class_ = 'desc')
print(desc.text)

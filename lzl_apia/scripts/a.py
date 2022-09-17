
from celery_task import app

msg = 'http://book.zongheng.com/book/1039009.html'

res = msg.replace('book/','aaa/')

print(res)



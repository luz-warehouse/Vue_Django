
from celery import Celery

import os,sys
# base_dir = os.path.dirname(os.path.dirname(__file__))
# print(base_dir)
# # sys.path.append(base_dir)
# sys.path.append(os.path.dirname(base_dir))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'read.settings.dev')

backend = 'redis://127.0.0.1:6379/1'  # 结果存储
broker = 'redis://127.0.0.1:6379/2'  # 消息中间件
app = Celery('test', broker=broker, backend=backend, include=[
    'read.utils.sms_send.sms_main', # 异步短信发送
    'read.utils.send_mail',         # 异步邮箱发送
    'read.apps.home.home_task'
])
# 修改时区配置
# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False

from datetime import timedelta
from celery.schedules import crontab
app.conf.beat_schedule = {
    # 定时任务一，每隔3秒做一次
    'update_banner': {
        'task': 'read.apps.home.home_task.update_banner',
        'schedule': timedelta(seconds=86400),  # 86400秒后（一天）
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        'args': '',
    },

}

